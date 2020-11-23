# CS 565 HW3: Poker Playing

This project contains a .py file titled VaughnWeirens.py which will play poker with the PyPokerMain script written by Dr. Monica Anderson.

This file contains a class titled VaughnWeirens, which has two main functions: student_function and card_counter. 

## Class Attributes

### student_Name
a string containing the name of the student (Vaughn Weirens)
### student_Hand
an array to be populated with cards that student_function will determine to either keep or discard.
### card_values
an array of characters containing the values that cards can have
### card_suits
an array of characters containing the suits that cards can have

## Class Functions

### student_function

This function will take a hand of 5 standard playing cards, and determine which ones should be kept or discarded according to the poker game of Five Card Draw. The function always keeps what it determines are 'winning hands' i.e. royal flushes, straight flushes, full houses, flushes and straights. When presented with four of a kind, three of a kind, two pair, and pair, it will always keep the multiple cards present and discard the odd cards out. When only a high card is present, the function will keep the highest card in its hand and discard the other four cards. The function will attempt to acquire a flush if it has at least 4 cards of the same suit in its hand. The function then returns a boolean array of cards it wishes to exchange, with 'True' indicating cards to be exchanged and 'False' indicating cards to keep.

### card_counter

This function will count the number of cards in a given suit or value, for the purpose of determining pairs, three of a kind, four of a kind, and flushes. It returns two arrays, card_count which provides the number of each value of card, and suit_count, which returns the number of each suit present in the hand.

