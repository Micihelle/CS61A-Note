## problem 1
from cats import * 
ps = ['hi', 'how are you', 'fine']
s = lambda p: len(p) <= 4
pick(ps, s, 0)
pick(ps, s, 1)
pick(ps, s, 2)

## problem 2
from cats import * 
dogs = about(['dogs', 'hounds'])
dogs('A paragraph about cats.')
print(dogs('A paragraph about cats.'))
print(dogs('A paragraph about dogs.'))
print(dogs('Release the Hounds!'))
print(dogs("AdogsParagraph"))


## problem 6-test
from cats import minimum_mewtations, autocorrect
import tests.construct_check as test
big_limit = 10
minimum_mewtations("wind", "wind", big_limit)



## problem 8
from cats import report_progress
print_progress = lambda d: print('ID:', d['id'], 'Progress:', d['progress'])
typed = ['I', 'have', 'begun']
prompt = ['I', 'have', 'begun', 'to', 'type']
print_progress({'id': 1, 'progress': 0.6})

report_progress(typed, prompt, 1, print_progress) # print_progress is called on the report
report_progress(['I', 'begun'], prompt, 2, print_progress)
report_progress(['I', 'hve', 'begun', 'to', 'type'], prompt, 3, print_progress)


## problem 9
from cats import *
p = [[1, 4, 6, 7], [0, 4, 6, 9]]
words = ['This', 'is', 'fun']
match = time_per_word(words, p)
match["words"]

p = [[0, 2, 3], [2, 4, 7]]
match = time_per_word(['hello', 'world'], p)
get_word(match, word_index=1)
match["times"]
time(match, player_num=0, word_index=1)

from cats import match, fastest_words
p0 = [2, 2, 3]
p1 = [6, 1, 2]
fastest_words(match(['What', 'great', 'luck'], [p0, p1]))



## problem 10
from cats import match, fastest_words
p0 = [2, 2, 3]
p1 = [6, 1, 2]
fastest_words(match(['What', 'great', 'luck'], [p0, p1]))

p0 = [2, 2, 3]
p1 = [6, 1, 3]
fastest_words(match(['What', 'great', 'luck'], [p0, p1]))  # with a tie, choose the first player















