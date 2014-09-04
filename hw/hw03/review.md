Review
=====================

Style Guide Evaluation
----------------------
Source code appears to abide by the specification of the Google Python Style Guide. The comment blocks are organized accurately, all functions are names using the lower_with_underscore theme, and classes are named with the CapWords theme. One difference I noticed was the naming convention for the stateParserhw02.py file. According to the style guide, packages and modules should be named using the lower_with_underscore theme. This way, when importing the module from the main driver progam, it will appear something like "import state_parser_hw02". Also, in the hw02main.py file, the file input is stored in the variable 'f', and the style guide discourages against one letter variable names.

Code Evaluation
---------------
The code is well written, organized, and easily readable. The output file, however, does not write each state one line at a time as the comment indicates. It seemed to not include any newline characters, but I'm not sure if that was something with the way I was viewing it. Also, when I tried to run the code from the terminal, I was getting an error that the """ comment lines were not indented correctly, I never thought this was an issue, but it kept the code from running initially. Also, I got an error with the way the imported module was being referenced. The import line was "import stateParserhw02" and when the linked list object was created, the line was "linked_list = stateParser2.LinkedList()". There was an error because they two module names didn't match.