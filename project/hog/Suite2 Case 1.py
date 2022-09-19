"Suite2> Case 1:"
import hog
always_three = hog.make_test_dice(3)
always = hog.always_roll
#
# Play function stops at goal
s0, s1 = hog.play(always(5), always(3), score0=91, score1=10, dice=always_three)
print(s0)
print(s1)

"""
>>> s0
106
>>> s1
10  ## player0 在第一回合(投5次 每次点数为3)就达到了goal
"""
