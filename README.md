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


# Procedure
1) Clone this repo.


2) Open this folder as work-space in VS Code. (`code .` in terminal)


3) Make necessary changes to main.cc. This acts as your default main file for all problems of a particular contest.


4) use ``` ctrl+shift+` ``` to open a new terminal from vs code. Here type in `./parse.py 4` to download all the test-cases (input and output) of that particular contest.


5) Navigate to A.cc using the keybindings `ctrl+p` and type in A.cc


6) Open Output.txt by using the keybindings `ctrl+p` and type Output.txt


7) To build and test-run with given test-cases, use `ctrl+shift+b` and select C++ builder.


Special thanks to johnathan79717 for the [parser.](https://github.com/johnathan79717/codeforces-parser)
