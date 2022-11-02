<h1>Final exercise repository</h1>

<h2>Usage</h2>

<h3>A basic application that prints out hello world</h3>
<p>Go to terminal and run helloworld.py to recieve the message Hello World!</p>

<h3>App to convert roman numerals to integers and integers to roman numerals</h3>
<p>
Go to terminal and run roman_numeral_converter.py to see output for hardcoded values.<br />
These functions have also been implemented via click which allows them to take input via cli.<br />

click_function1.py --num=<ARABIC NUMBER> returns roman numeral for that number<br />
click_function2.py --s=<ROMAN NUMERAL> return aranic integer for input roman numeral string in caps<br />
</p>

<h3>Black set up</h3>
<p><br />
Linting is run via IDE and black runs every time git commit is called as a pre commit hook<br />
There is a Makefile present which gives the option to run flask server. <br />
<b>Usage</b><br />
make init - initializes venv<br />
make test - runs black and then runs pytest for all test files present<br />
make serve - runs flask server at port 5000<br />
</p>

<h3>Testing</h3>
<p>Test_file.py has been created containing test cases. Run pytest test_file.py to run tests over the code and see it passed.<br />
It contains 10 unit tests cases for the roman_numeral_converter functions and a integration tests which runs a test client of flask server and checks the status code is 200.
</p>

<h3>Flask Server</h3>
<p>main.py file creates the code to run flask server. the /home path will take you to the WEB UI where you can enter integers to convert and on pressing submit the server returns the converted values</p>

