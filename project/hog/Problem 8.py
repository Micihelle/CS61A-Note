#doctest
"""
from doctest import run_docstring_examples
run_docstring_examples(make_averaged, globals(), True)
"""

#Question 8 > Suite 2 > Case 1

"""
from hog import *
dice = make_test_dice(3, 1, 5, 6)  #函数传递
averaged_dice = make_averaged(dice, 1000)
# Average of calling dice 1000 times
averaged_dice()
"""

"""
3.750
"""


#Question 8 > Suite 2 > Case 2
"""
from hog import *
dice = make_test_dice(3, 1, 5, 6)
averaged_roll_dice = make_averaged(roll_dice, 1000)
# Average of calling roll_dice 1000 times
# Enter a float (e.g. 1.0) instead of an integer
averaged_roll_dice(2, dice)

6.0
"""

