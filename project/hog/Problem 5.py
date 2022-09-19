"""
import hog
always_three = hog.make_test_dice(3)
always = hog.always_roll
#
# Play function stops at goal
s0, s1 = hog.play(always(5), always(3), score0=91, score1=10, dice=always_three)
s0
"""


"""
import hog
always_three = hog.make_test_dice(3)
always = hog.always_roll
#
# Goal score is not hardwired
s0, s1 = hog.play(always(5), always(5), goal=10, dice=always_three)
s0
"""

import hog
always_three = hog.make_test_dice(3)
always_seven = hog.make_test_dice(7)
#
# Use strategies
# We recommend working this out turn-by-turn on a piece of paper (use Python for difficult calculations).
strat0 = lambda score, opponent: opponent % 10
strat1 = lambda score, opponent: max((score // 10) - 4, 0)
s0, s1 = hog.play(strat0, strat1, score0=71, score1=80, dice=always_seven)
s0
