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
import pytest
from lists import Deque

######  Problem #3 #########################

def test_P3_create_empty_deque():
    d = Deque()
    assert d.isEmpty() == True

def test_P3_create_noempty_deque():
    d = Deque()
    d.addFront("test")
    assert d.isEmpty() == False

def test_P3_one_element_deque_front():
    d = Deque()
    d.addFront("test")
    assert d.removeFront() == "test"

def test_P3_one_element_deque_Rear():
    d = Deque()
    d.addRear("test")
    assert d.removeRear() == "test"

def test_P3_one_element_deque_f2b():
    d = Deque()
    d.addFront("test")
    assert d.removeRear() == "test"

def test_P3_one_element_deque_b2f():
    d = Deque()
    d.addRear("test")
    assert d.removeFront() == "test"



def test_P3_remove_element():
    d = Deque()
    d.addFront("test")
    d.removeRear()
    assert d.isEmpty() == True

def test_P3_removefront_from_empty():
    d = Deque()
    with pytest.raises(Exception):
        d.removeFront()

def test_P3_removeRear_from_empty():
    d = Deque()
    with pytest.raises(Exception):
        d.removeRear()

def test_P3_size():
    d = Deque()
    d.addFront(2)
    d.addFront(1)
    d.addRear(3)
    d.addRear(4)
    d.removeRear()
    assert d.size() == 3

def test_P3_remove_from_correct_end1():
    d = Deque()
    d.addFront(2)
    d.addFront(1)
    d.addRear(3)
    d.addRear(4)
    assert d.removeFront() == 1

def test_P3_remove_from_correct_end2():
    d = Deque()
    d.addFront(2)
    d.addFront(1)
    d.addRear(3)
    d.addRear(4)
    d.removeRear()
    assert d.removeRear() == 3





