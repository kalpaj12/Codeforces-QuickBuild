# Codeforces-QuickBuild for VS Code (linux)
This is a parser - buildtool for codeforces.


Currently supports C and C++
![Screenshot](Screenshots/1.png?raw=true "Title")
# Functionalities
1) Inbuilt parser that scrapes input and output test-cases of all questions of a particular contest.
![Screenshot](Screenshots/2.png?raw=true "Title")
![Screenshot](Screenshots/3.png?raw=true "Title")


2) Displays compiler and run time errors on Output.txt.
![Screenshot](Screenshots/4.png?raw=true "Title")


3) code can be compiled and tested against all provided input test-cases (scraped) to check for correctness. This is shown in Output.txt
![Screenshot](Screenshots/5.png?raw=true "Title")


4) Provide custom input test cases.


# Procedure
1) Clone this repo.


2) Open this folder as work-space in VS Code. (`code .` in terminal)


3) Make necessary changes to template.cpp ( present inside .vscode ). This acts as your default .cpp file for all problems of a contest.


4) Now, use the keybinding `ctrl+shift+b`, and select Create Files.


5) Use ``` ctrl+shift+` ``` to open integrated terminal in vs code. Here type in `./parse.py (contest_name)` (eg.`./parse.py 4`) to download all the test-cases (input and output) of that particular contest.


6) To open codespace for question A, using the keybindings `ctrl+p` and type in A.cpp


7) To open Output.txt by using the keybindings `ctrl+p` and type Output.txt


8) To build and test-run code on given test-cases, use `ctrl+shift+b` and select codeforces builder.


9) Custom test-cases can be provided on Input.txt. Follow step 7 and instead of Output.txt, search for Input.txt


Special thanks to johnathan79717 for the [parser.](https://github.com/johnathan79717/codeforces-parser)
