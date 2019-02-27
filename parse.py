#!/usr/bin/python

# Python 2->3 libraries that were renamed.
try:
    from urllib2 import urlopen
except:
    from urllib.request import urlopen
try:
    from HTMLParser import HTMLParser
except:
    from html.parser import HTMLParser

# Other libraries.
from sys import argv
from subprocess import call
from functools import partial, wraps
import re
import argparse

language_params = {
        'c++14' : {
            'TEMPLATE'    : 'main.cc',
            'DEBUG_FLAGS' : '-DDEBUG',
            'COMPILE_CMD' : 'g++ -g -std=c++14 -Wall $DBG',
            'RUN_CMD'     : './a.out'
            },
        }

SAMPLE_INPUT='input'
SAMPLE_OUTPUT='output'

# Do not modify these!
RED_F='\033[31m'
GREEN_F='\033[32m'
BOLD='\033[1m'
NORM='\033[0m'
TIME_CMD='`which time` -o time.out -f "(%es)"'
TIME_AP='`cat time.out`'

# Problems parser.
class CodeforcesProblemParser(HTMLParser):

    def __init__(self, folder):
        HTMLParser.__init__(self)
        self.folder = folder
        self.num_tests = 0
        self.testcase = None
        self.start_copy = False

    def handle_starttag(self, tag, attrs):
        if tag == 'div':
            if attrs == [('class', 'input')]:
                self.num_tests += 1
                self.testcase = open(
                    '%s/%s%d' % (self.folder, SAMPLE_INPUT, self.num_tests), 'wb')
            elif attrs == [('class', 'output')]:
                self.testcase = open(
                    '%s/%s%d' % (self.folder, SAMPLE_OUTPUT, self.num_tests), 'wb')
        elif tag == 'pre':
            if self.testcase != None:
                self.start_copy = True

    def handle_endtag(self, tag):
        if tag == 'br':
            if self.start_copy:
                self.testcase.write('\n'.encode('utf-8'))
                self.end_line = True
        if tag == 'pre':
            if self.start_copy:
                if not self.end_line:
                    self.testcase.write('\n'.encode('utf-8'))
                self.testcase.close()
                self.testcase = None
                self.start_copy = False

    def handle_entityref(self, name):
        if self.start_copy:
            self.testcase.write(self.unescape(('&%s;' % name)).encode('utf-8'))

    def handle_data(self, data):
        if self.start_copy:
            self.testcase.write(data.strip('\n').encode('utf-8'))
            self.end_line = False

# Contest parser.
class CodeforcesContestParser(HTMLParser):

    def __init__(self, contest):
        HTMLParser.__init__(self)
        self.contest = contest
        self.start_contest = False
        self.start_problem = False
        self.name = ''
        self.problem_name = ''
        self.problems = []
        self.problem_names = []

    def handle_starttag(self, tag, attrs):
        if self.name == '' and attrs == [('style', 'color: black'), ('href', '/contest/%s' % (self.contest))]:
                self.start_contest = True
        elif tag == 'option':
            if len(attrs) == 1:
                regexp = re.compile(r"'[A-Z]'") # The attrs will be something like: ('value', 'X')
                string = str(attrs[0])
                search = regexp.search(string)
                if search is not None:
                    self.problems.append(search.group(0).split("'")[-2])
                    self.start_problem = True

    def handle_endtag(self, tag):
        if tag == 'a' and self.start_contest:
            self.start_contest = False
        elif self.start_problem:
            self.problem_names.append(self.problem_name)
            self.problem_name = ''
            self.start_problem = False

    def handle_data(self, data):
        if self.start_contest:
            self.name = data
        elif self.start_problem:
            self.problem_name += data

# Parses each problem page.
def parse_problem(folder, contest, problem):
    url = 'http://codeforces.com/contest/%s/problem/%s' % (contest, problem)
    html = urlopen(url).read()
    parser = CodeforcesProblemParser(folder)
    parser.feed(html.decode('utf-8'))
    # .encode('utf-8') Should fix special chars problems?
    return parser.num_tests

# Parses the contest page.
def parse_contest(contest):
    url = 'http://codeforces.com/contest/%s' % (contest)
    html = urlopen(url).read()
    parser = CodeforcesContestParser(contest)
    parser.feed(html.decode('utf-8'))
    return parser

# Generates the test script.
def generate_test_script(folder, language, num_tests, problem):
    param = language_params[language]

# Main function.
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--language', '-l', default="c++14", help="The programming language you want to use "
            "(c++14, go)")
    parser.add_argument('contest', help="")
    args = parser.parse_args()

    contest = args.contest
    language = args.language

    # Find contest and problems.
    print ('Parsing contest %s for language %s, please wait...' % (contest, language))
    content = parse_contest(contest)
    print (BOLD+GREEN_F+'*** Round name: '+content.name+' ***'+NORM)
    print ('Found %d problems!' % (len(content.problems)))

    # Find problems and test cases.
    TEMPLATE = language_params[language]["TEMPLATE"]
    for index, problem in enumerate(content.problems):
        print ('Downloading Problem %s: %s...' % (problem, content.problem_names[index]))
        folder = '%s-%s/%s/' % (contest, language, problem)
        call(['mkdir', '-p', folder])
        call(['cp', '-n', TEMPLATE, '%s/%s.%s' % (folder, problem, TEMPLATE.split('.')[1])])
        num_tests = parse_problem(folder, contest, problem)
        print('%d sample test(s) found.' % num_tests)
        generate_test_script(folder, language, num_tests, problem)
        print ('========================================')

if __name__ == '__main__':
    main()
