#!/usr/bin/env python3

""" Graded Lab #1 for Inf1340, Fall 2015 """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def vowel_or_consonant():

    vowel = list("aeiou")
    letter = raw_input("Please enter a letter of the alphabet: ")
    if letter == "a":
        print ("vowel")
    elif letter == "e":
        print ("vowel")
    elif letter == "i":
        print ("vowel")
    elif letter == "o":
        print ("vowel")
    elif letter == "u":
        print ("vowel")
    elif letter == "y":
        print ("sometimes a vowel, sometimes a consonant")
    else:
        print("consonant")
