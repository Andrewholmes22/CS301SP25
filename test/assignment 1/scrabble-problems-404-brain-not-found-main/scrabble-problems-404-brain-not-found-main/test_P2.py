#################################
### DO NOT EDIT THIS FILE !!! ###
#################################
"""
Do not edit this file; it is used
by the autograder.  However, you
are welcome and encouraged to
write your own testing code in 
the main file or in your own file.
"""

from scrabble import ValidWord

######  Problem #2 #########################

def test_P2_valid_word():
    assert ValidWord("wrinkly") == True

def test_P2_invalid_word():
    assert ValidWord("wrinkeley") == False
    
