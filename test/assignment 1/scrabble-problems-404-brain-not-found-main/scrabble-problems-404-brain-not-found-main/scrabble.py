##########################################################################
##########################################################################
###                                                                    ###
###                       UNC CS301  Spring 2025                       ###
###                             Assignment 1                           ###
###                          Scrabble Problems                         ###
###                                                                    ###
##########################################################################
##########################################################################

""" For this and other assignments in CS301,
    replace the lines
         # TODO:  Implement me!
         pass
    in the given stencil code with your own solutions.
    Don't change the names of the given functions
    or else the autograder won't be able to evaluate
    your code.  The autograder will automatically
    evaluate your code each time you commit it to
    GitHub.  You may submit it as may times as
    you want before the submission deadline.
"""

######  Helper Functions ###################
""" importwords reads all of the words from
    the file words.txt and places them in
    a single large python list."""

def importwords():
    wordlist = []
    fin = open('words.txt')
    for line in fin:  
        word = line.strip()
        wordlist.append(word)
    return wordlist

wordlist = importwords()

import time
""" benchmark(testfunction, inputvalue) measures
    how long it takes to run the given function
    on the given input. """

def benchmark(testfunction, inputvalue):
    start = time.perf_counter()
    testfunction(inputvalue)
    stop = time.perf_counter()
    return stop-start



######  Problem #1 #########################
""" SumInt should input a positive integer n
    and return the sum of all integers
    from 1 to n. """


def SumInt(n):
  if n<=0:
    return "must be a positive integer"
  else:
     return (n*(n+1))//2
  

######  Problem #2 #########################
""" ValidWord should output True if the
    given word is in the word list from
    words.txt and False if not."""

def ValidWord(input_word):
  return input_word in wordlist
  pass

######  Problem #3 #########################
""" CanBeMadeFrom should input two strings
    representing a word and a set of tiles.
    It should return True if the word can
    be made from the tiles, and False
    otherwise."""

def CanBeMadeFrom(input_word, input_tiles):
  # TODO:  Implement me!
  pass

######  Problem #4 #########################
""" AllWords should input a string
    representing a set of tiles and should
    output a list of all of the words from
    the word list that can be made from
    those tiles. """

def AllWords(input_tiles):
  # TODO:  Implement me!
  pass

######  Problem #5 #########################
""" SpellingBee should input a center letter
    and a string representing the other
    given letters from a Spelling Bee
    puzzle.  It should output a list of
    words that are valid solutions for the
    Spelling Bee puzzle.  These words must be
    at least 5 letters long, must contain
    the center letter at least once, and
    may only contain the center letter and
    the other letters. """

def SpellingBee(centerletter, otherletters):
  # TODO:  Implement me!
  pass

######  Problem #6 #########################
""" BestBingoLetters should be a function
    with no inputs, and should return a
    list of strings.  Each string in the
    list should represent one solution to
    the problem. The problem is to find
    the set(s) of 8 tiles that can be
    rearranged into the most words. If
    is only one such set, your list should
    only have one element; if there is
    more than one, your list should
    have one element per set.  This
    problem is extra credit."""

def BestBingoLetters():
  # TODO:  Implement me!
  pass



