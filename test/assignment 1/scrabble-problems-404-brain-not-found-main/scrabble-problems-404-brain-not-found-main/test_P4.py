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

from scrabble import AllWords

######  Problem #4 #########################

def test_P4_no_match():
    assert AllWords("dkjfd") == []

def test_P4_one_match():
    assert AllWords("hello") == ["hello"]


def test_P4_multiple_match():
    l = AllWords("read")
    l.sort()
    assert l == ["dare","dear","read"]
