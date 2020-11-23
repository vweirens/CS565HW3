# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 11:03:26 2020

@author: Vaughn Weirens
"""


class VaughnWeirens:

    # Hand values
    # 1 - High card
    # 2 - Pair
    # 3 - Two pair
    # 4 - Three of a kind
    # 5 - Straight
    # 6 - Flush
    # 7 - Full house
    # 8 - Four of a kind
    # 9 - Straight flush
    # 10 - Royal flush

    student_Name = "Vaughn Weirens"
    student_Hand = []
    card_values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    card_suits = ['s', 'c', 'd', 'h']
    # student function uses student Hand and return a boolean list to exchange cards
    def student_function(self):

        # Dummy data from student function
        if not self.student_Hand:
            print('Please deal a hand')
            return
        # print hand for bug fixing
        #print('My initial hand is: ', self.student_Hand)
        #initialize dummy values
        hand_value = 0 #how good is our hand
        pair_count = 0 #how many pairs do we have
        three_count = 0 #do we have a three of a kind
        keep_card_type = [] #the type of card we aim to keep
        keep_suit_type = None
        max_suits = 0
        #Count the types of each card in hand
        [card_count, suit_count] = self.card_counter()
        
        for c in range(0, len(card_count)):
            if card_count[c] >= 1:
                high_card = self.card_values[c]
        
        #check for multiple occurrences of cards
        for card in range(0, len(card_count)):
            if card_count[card] >= 2:
                if card_count[card] == 3:
                    hand_value = 4
                    keep_card_type.append(self.card_values[card])
                    three_count = 1
                elif card_count[card] == 4:
                    hand_value = 8
                    keep_card_type.append(self.card_values[card])
                else:
                    hand_value = 2
                    pair_count = pair_count + 1
                    keep_card_type.append(self.card_values[card])
        
        #check if we have two pair or full house
        if pair_count > 1 and three_count < 1:
            hand_value = 3
        elif pair_count == 1 and three_count == 1:
            hand_value = 7
            return [False, False, False, False, False]
        
        #check for flushes
        for suit in range(0, len(suit_count)):
            if suit_count[suit] > 3:
                #always keep flushes, straight flushes, royal flushes
                max_suits = suit_count[suit]
                if suit_count[suit] == 5 and hand_value < 6:
                    hand_value = 6
                    return [False, False, False, False, False]
                else:
                    keep_suit_type = self.card_suits[suit]
         
        #check for straights
        for card in range(0, len(card_count)-4):
            #always keep straights
            if card_count[card] == 1 and card_count[card+1] == 1 and card_count[card+2] == 1 and card_count[card+3] == 1 and card_count[card+4] == 1:
                hand_value = 5
                return [False, False, False, False, False]
        
        # if you only have high card
        if hand_value < 1:
            hand_value = 1
        
        #print values for bug fixing
        #print('hand value: ', hand_value)
        #print('card type kept: ', keep_card_type)
        #print('suits count:' ,suit_count)
        #print('suit type kept:', keep_suit_type)
        #determine which cards we keep
        keep_array = []
        for card in self.student_Hand:
            #print(card)
            if hand_value == 1:
                if max_suits > 3:
                    if card[1] == keep_suit_type:
                        keep_array.append(False)
                elif card[0] == high_card:
                    keep_array.append(False)
                else:
                    keep_array.append(True)
            elif hand_value == 2:
                if card[0] == keep_card_type[0]:
                    keep_array.append(False)
                else:
                    keep_array.append(True)
            elif hand_value == 3:
                if (card[0] == keep_card_type[0]) or (card[0] == keep_card_type[1]):
                    keep_array.append(False)
                else:
                    keep_array.append(True)
            elif hand_value == 4:
                if card[0] == keep_card_type[0]:
                    keep_array.append(False)
                else:
                    keep_array.append(True)
            elif hand_value == 5:
                keep_array.append(False)
            elif hand_value == 6:
                keep_array.append(False)
            elif hand_value == 7:
                keep_array.append(False)
            elif hand_value == 8:
                if card[0] == keep_card_type[0]:
                    keep_array.append(False)
                else:
                    keep_array.append(True)
            elif hand_value == 9:
                keep_array.append(False)
            elif hand_value == 10:
                keep_array.append(False)
        #print cards kept for bug fixing
        #print('keeping:', keep_array)
        return keep_array
        #test case
        #return [True,True,True,True,True]

    def card_counter(self):

        #card indices indicate 2-A in ascending order
        card_count_array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        #suit indices indicate spades-hearts in ascending order
        #i.e. spades -> clubs -> diamonds -> hearts
        suit_count_array = [0, 0, 0, 0]
        for card in range(0, len(self.student_Hand)):
            #count card values
            if self.student_Hand[card][0] == '2':
                card_count_array[0] = card_count_array[0] + 1
            elif self.student_Hand[card][0] == '3':
                card_count_array[1] = card_count_array[1] + 1
            elif self.student_Hand[card][0] == '4':
                card_count_array[2] = card_count_array[2] + 1
            elif self.student_Hand[card][0] == '5':
                card_count_array[3] = card_count_array[3] + 1
            elif self.student_Hand[card][0] == '6':
                card_count_array[4] = card_count_array[4] + 1
            elif self.student_Hand[card][0] == '7':
                card_count_array[5] = card_count_array[5] + 1
            elif self.student_Hand[card][0] == '8':
                card_count_array[6] = card_count_array[6] + 1
            elif self.student_Hand[card][0] == '9':
                card_count_array[7] = card_count_array[7] + 1
            elif self.student_Hand[card][0] == 'T':
                card_count_array[8] = card_count_array[8] + 1
            elif self.student_Hand[card][0] == 'J':
                card_count_array[9] = card_count_array[9] + 1
            elif self.student_Hand[card][0] == 'Q':
                card_count_array[10] = card_count_array[10] + 1
            elif self.student_Hand[card][0] == 'K':
                card_count_array[11] = card_count_array[11] + 1
            elif self.student_Hand[card][0] == 'A':
                card_count_array[12] = card_count_array[12] + 1

            # count card suits
            if self.student_Hand[card][1] == 's':
                suit_count_array[0] = suit_count_array[0] + 1
            elif self.student_Hand[card][1] == 'c':
                suit_count_array[1] = suit_count_array[1] + 1
            elif self.student_Hand[card][1] == 'd':
                suit_count_array[2] = suit_count_array[2] + 1
            elif self.student_Hand[card][1] == 'h':
                suit_count_array[3] = suit_count_array[3] + 1
        return[card_count_array, suit_count_array]
