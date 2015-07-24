#! /usr/bin/python
# A Python script that simulates rolling two dice a few times.
#Now add your own code.

# Module for dealing with random numbers.
import random


# How many times to roll the dice.
# NUM_DICE_ROLLS = 5
#
#
# print 'Rolling the dice ' + str(NUM_DICE_ROLLS) + ' times'
# for dice_rolls in range(NUM_DICE_ROLLS):
#   roll1 = random.randint(1, 6)
#   roll2 = random.randint(1, 6)
#   print 'Rolled', roll1, roll2
#

def until_double_sixes():
    double_sixes = False
    count = 0
    while double_sixes is False:
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        count += 1
        print roll1, roll2
        if roll1 is 1 and roll2 is 1:
            print "Snake Eyes!"
        if roll1 is 6 and roll2 is 6:
            double_sixes = True
            print "Got double sixes! You rolled " + str(count) + " times."
until_double_sixes()
