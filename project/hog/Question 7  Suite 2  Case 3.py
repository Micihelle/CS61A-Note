"Question 7 > Suite 2 > Case 3"

"""
from hog import play, always_roll, announce_lead_changes
from dice import make_test_dice
#
def echo(s0, s1, player=None):
    return player, f"{s0} {s1}" # message of the form: "s0 s1"
s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(3), goal=6, say=echo)# Remember pigs on prime!
"""


"""
(line 1)? 5 0
(line 2)? 5 5
(line 3)? 8 5
"""


"Question 7 > Suite 2 > Case 4"

"""
from hog import play, always_roll, announce_lead_changes
from dice import make_test_dice
def count(n):
    def say(s0, s1, curr_count=None):
            if curr_count is None:
                curr_count = n
            return curr_count + 1, str(curr_count) + " " + str(s0)
    return say

s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(5), goal=15, say=count(1))
print(s0)
print(s1)
"""

#curr_count 逐增的问题
"""
(line 1)? 1 7
(line 2)? 2 7
(line 3)? 3 12
(line 4)? 4 12
(line 5)? 5 19 
"""

"Question 7 > Suite 3 > Case 1"

"""
from hog import play, always_roll, both, announce_lead_changes, say_scores
from dice import make_test_dice
#
def echo(s0, s1, player=None):
    return player, str(s0) + " " + str(s1)
strat0 = lambda score, opponent: 1 - opponent // 10
strat1 = always_roll(3)
s0, s1 = play(strat0, strat1, dice=make_test_dice(4, 2, 6), goal=15, say=echo)
"""

"""
(line 1)? 4 0
(line 2)? 4 12
(line 3)? 7 12
(line 4)? 7 24
"""

"Question 7 > Suite 3 > Case 2"
"""
from hog import play, always_roll, both, announce_lead_changes, say_scores
from dice import make_test_dice
#
def total(s0, s1, player=None):
    return player, str(s0 + s1)
s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(2, 5), goal=10, say=total)
"""

"Question 7 > Suite 3 > Case 3"

"""
from hog import play, always_roll, both, announce_lead_changes, say_scores
from dice import make_test_dice
#
def echo_0(s0, s1, player=None):
    return player, f"* {s0}" # message of the form: "* s0"
def echo_1(s0, s1, player=None):
    return player, f"** {s1}" # message of the form: "** s1"
s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(2), goal=5, say=both(echo_0, echo_1))
"""


"""
(line 1)? * 3
(line 2)? ** 0
(line 3)? * 3
(line 4)? ** 3
(line 5)? * 7
(line 6)? ** 3

"""


