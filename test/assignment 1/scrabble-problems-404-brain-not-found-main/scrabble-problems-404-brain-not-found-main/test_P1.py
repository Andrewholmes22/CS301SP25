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

from scrabble import SumInt

######  Problem #1 #########################

def test_P1_small_input():
    assert SumInt(3) == 6

def test_P1_big_input():
    assert SumInt(2000) == 2001000

