"""Typing test implementation"""

from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def pick(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns True. If there are fewer than K such paragraphs, return
    the empty string.

    Arguments:
        paragraphs: a list of strings
        select: a function that returns True for paragraphs that can be selected
        k: an integer

    >>> ps = ['hi', 'how are you', 'fine']
    >>> s = lambda p: len(p) <= 4
    >>> pick(ps, s, 0)
    'hi'
    >>> pick(ps, s, 1)
    'fine'
    >>> pick(ps, s, 2)
    ''
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    ps_selected = [x for x in paragraphs if select(x)==True]    # K such paragraphs which SELECT called returns True.
    if len(ps_selected)>k:
        return ps_selected[k]
    else:
        return ""
    
    # mapping expression: ps = [x for x in selecct if select(paragraphs)==True]
    # conditional:define outrage output?
    # requirement: index range(len(paragraphs))& string range 
    # return statement: return ps[k]
    # selete logic: arguments selete
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether
    a paragraph contains one of the words in TOPIC.

    Arguments:
        topic: a list of words related to a subject

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> pick(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> pick(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # import function lower from utilis which return a lowercased version of x
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    def select(paragraph):
        pword = split(lower(paragraph))   # influence of lowercase
        for y in topic:       # 对 topic word 进行遍历
            print('DEBUG: current topic word is ',y)
            p = [x for x in pword if (lower(remove_punctuation(x)) == y)]   # influence of punctuation  空字符
            if p != []:
                return True
        return False                        # 对 topic word 及 paragraph 搜寻完毕后 
    return select

    # 2023/4/9: 利用string 特性重新搭建了判定逻辑架构
    # DEBUG-case: 关于topic word 的遍历搜寻问题


    # 2023/4/8: AttributeError: 'str' object has no attribute 'splic' > str.split()
    # DEBUG-CASE 针对 input paragraph 的修正
    # DEBUG-CASE: 确保对所有 topic word 进行遍历 
    # DEBUG-CASE: 针对单字符成行情况 >> 确保 topic word 存在独立性 >> 能否对划分工具上进行前后字符的限制?
        # split( stradd    'dogs/' and '/dogs')
        # topic word 的一些规定: dogs 和 dog 出现在 paragraph 中是否等同
            # 1.topic word 为 dogs >>  paragraph中出现 dog
            # 2. topic word 为 dog >> paragraph 中出现 dogs
                # 回归到关于 topic word 存在独立性说明
        # & codition statement ： lower(whether) == topic
    # DEBUG-CASE: 替换字符划分工具 否则无法处理'#crystallogenIcalW 情况  >> topic word 独立匹配关系
    # DEBUG-CASE: 多层遍历结构搭建 对topic word 的遍历 + 对 paragraph 的遍历(匹配判定)  (2023/4/8-last)
        
    
    

    # 2023/4/2
    # other influence: such as the tail of the string '.'
    # case analysis: 'dogs' in 'A paragraph about cats.'
    # False
    # 'dogs' in 'A paragraph about dogs.'
    # True
    # implement: 遍历select list 的 字符串
    # DEBUG-TypeError: 'list' object is not callable >> list() is not euqal to list[]  (call and index)
    # DEBUG-last case: the operation of paragraphs ?
        # topic 内的单词作为一个单独个体 不允许与其他字符产生依赖>>单个单词成行情况修补
        # 字符串"''"的实际含义：((sss))

    # ago
    # case analysis: arguments 'select' of the pick -> about function ->
    # -u case analysis: logic comparasion (read .md)
    # return statement: a function that returns whether a paragraph contains ...(TOPIC)
    # selete logic: 1.sequence partition by space
    #                     2.outrage define(the match between 'dogs' and 'dog'
    # END PROBLEM 2


def accuracy(typed, source):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of SOURCE that was typed.

    Arguments:
        typed: a string that may contain typos
        source: a string without errors

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    >>> accuracy('', '')
    100.0
    """
    typed_words = split(typed)
    source_words = split(source)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    if ((typed_words == []) & (source_words == [])):
        return 100.0
    elif ((typed_words == []) & (source_words != [])):
        return 0.0
    elif (len(typed_words) > len(source_words)):   # debug the IndexError
        percentage = [x for x in range(len(source_words)) if (typed_words[x] == source_words[x])]
    else:
        percentage = [x for x in range(len(typed_words)) if (typed_words[x] == source_words[x])]
    percentage = (len(percentage))/(len(typed_words))*100
    return percentage                  # compute the percentage of words typed correctly
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string.

    Arguments:
        typed: an entered string
        elapsed: an amount of time in seconds

    >>> wpm('hello friend hello buddy hello', 15)
    24.0
    >>> wpm('0123456789',60)
    2.0
    """
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    # END PROBLEM 4
    
    return (60*len(typed))/(elapsed*5)


###########
# Phase 2 #
###########

def autocorrect(typed_word, word_list, diff_function, limit):
    """Returns the element of WORD_LIST that has the smallest difference
    from TYPED_WORD. Instead returns TYPED_WORD if that difference is greater
    than LIMIT.

    Arguments:
        typed_word: a string representing a word that may contain typos
        word_list: a list of strings representing source words
        diff_function: a function quantifying the difference between two words
        limit: a number

    >>> ten_diff = lambda w1, w2, limit: 10 # Always returns 10
    >>> autocorrect("hwllo", ["butter", "hello", "potato"], ten_diff, 20)
    'butter'
    >>> first_diff = lambda w1, w2, limit: (1 if w1[0] != w2[0] else 0) # Checks for matching first char
    >>> autocorrect("tosting", ["testing", "asking", "fasting"], first_diff, 10)
    'testing'
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    if typed_word in word_list:
        return typed_word
    else:
        diff_return = [diff_function(typed_word,x,limit) for x in word_list]
        if min(diff_return) > limit:
            return  typed_word
        else:# 去掉最小值后仍然存在一个跟之前相同的最小值
            return word_list[diff_return.index(min(diff_return))]

            
    # diff_function return statement : the difference in length between the two input strings:
    # limit 意义 >> return the lowest difference
        #  if the lowest difference between typed_word and any of the words in word_list is
        #  greater than limit, then typed_word is returned instead.
    # END PROBLEM 5


def feline_fixes(typed, source, limit):
    """A diff function for autocorrect that determines how many letters
    in TYPED need to be substituted to create SOURCE, then adds the difference in
    their lengths and returns the result.

    Arguments:
        typed: a starting word
        source: a string representing a desired goal word
        limit: a number representing an upper bound on the number of chars that must change

    >>> big_limit = 10
    >>> feline_fixes("nice", "rice", big_limit)    # Substitute: n -> r
    1
    >>> feline_fixes("range", "rungs", big_limit)  # Substitute: a -> u, e -> s
    2
    >>> feline_fixes("pill", "pillage", big_limit) # Don't substitute anything, length difference of 3.
    3
    >>> feline_fixes("roses", "arose", big_limit)  # Substitute: r -> a, o -> r, s -> o, e -> s, s -> e
    5
    >>> feline_fixes("rose", "hello", big_limit)   # Substitute: r->h, o->e, s->l, e->l, length difference of 1.
    5
    """
    # BEGIN PROBLEM 6
    """
    if len(source) == len(typed):
        return sum(x)
    else:
        return sum(x) + abs(len(source)-len(typed))
    """
    if (limit < 0):    #  超出 limit 时候 及时退出 recursion
        return 0
    elif ((source == '') | (typed == '')):
        return abs(len(source)-len(typed))
    else:
        if source[0] == typed[0]:     
            print("DEBUG: current character is ",source[0])
            return feline_fixes(source[1:],typed[1:],limit)
        else:
            print("DEBUG: current character is ",source[0])
            return 1 + feline_fixes(source[1:],typed[1:],limit-1)

        # 逐字符递归判断, >> 不同情况对应不同的分支树
        # 无论在相同位置上是否存在不同字符 导向相同的递归情况。。
        # 只要超出 limit 值 及时退出

    
    # 递归 累加相同的字符数(2023/4/10)
    
    
    
    # END PROBLEM 6


def minimum_mewtations(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL.
    This function takes in a string START, a string GOAL, and a number LIMIT.
    Arguments:
        start: a starting word
        goal: a goal word
        limit: a number representing an upper bound on the number of edits
    >>> big_limit = 10
    >>> minimum_mewtations("cats", "scat", big_limit)       # cats -> scats -> scat
    2
    >>> minimum_mewtations("purng", "purring", big_limit)   # purng -> purrng -> purring
    2
    >>> minimum_mewtations("ckiteus", "kittens", big_limit) # ckiteus -> kiteus -> kitteus -> kittens
    3
    """
    if limit < 0:  # Fill in the condition
        # BEGIN
        "*** YOUR CODE HERE ***"
        return 0
        # END
    elif ((len(start) == 0) | (len(goal)==0)):
        return len(start)+len(goal)
    else:
        if start[0] == goal[0]:  # Feel free to remove or add additional cases
        # BEGIN
            return minimum_mewtations(start[1:],goal[1:],limit)
        # END
        else:   #(start[0] != goal[0])
            add = minimum_mewtations(start,goal[1:],limit-1) # Fill in these lines (后面字符相等)
            remove = minimum_mewtations(start[1:],goal,limit-1)  #(goal 不动)
            substitute = minimum_mewtations(start[1:],goal[1:],limit-1) # start 和 goal 都动
        # BEGIN
            return 1+ min(min(add,remove),substitute)  # minimum the number of edit operations
        # END


def final_diff(typed, source, limit):
    """A diff function that takes in a string TYPED, a string SOURCE, and a number LIMIT.
    If you implement this function, it will be used."""
    if limit < 0:  # Fill in the condition
        # BEGIN
        "*** YOUR CODE HERE ***"
        return 0
        # END
    elif ((len(typed) == 0) | (len(source)==0)):
        return len(typed)+len(source)
    else:
        if typed[0] == source[0]:  # Feel free to remove or add additional cases
        # BEGIN
            return final_diff(typed[1:],source[1:],limit)
        # END
        else:   #(start[0] != goal[0])
            add = final_diff(typed,source[1:],limit-1) # Fill in these lines (后面字符相等)
            remove = final_diff(typed[1:],source,limit-1)  #(goal 不动)
            substitute = final_diff(typed[1:],source[1:],limit-1) # start 和 goal 都动
        # BEGIN
            return 1+ min(min(add,remove),substitute)  # minimum the number of edit operations
        # END


FINAL_DIFF_LIMIT = 6  # REPLACE THIS WITH YOUR LIMIT


###########
# Phase 3 #
###########


def report_progress(typed, prompt, user_id, upload):
    """Upload a report of your id and progress so far to the multiplayer server.
    Returns the progress so far.

    Arguments:
        typed: a list of the words typed so far
        prompt: a list of the words in the typing prompt
        user_id: a number representing the id of the current user
        upload: a function used to upload progress to the multiplayer server

    >>> print_progress = lambda d: print('ID:', d['id'], 'Progress:', d['progress'])
    >>> # The above function displays progress in the format ID: __, Progress: __
    >>> print_progress({'id': 1, 'progress': 0.6})
    ID: 1 Progress: 0.6
    >>> typed = ['how', 'are', 'you']
    >>> prompt = ['how', 'are', 'you', 'doing', 'today']
    >>> report_progress(typed, prompt, 2, print_progress)
    ID: 2 Progress: 0.6
    0.6
    >>> report_progress(['how', 'aree'], prompt, 3, print_progress)
    ID: 3 Progress: 0.2
    0.2
    """
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    if len(typed) == 0:  #长度为0 无法进行迭代
        progress = 0.0
    else:   
        for x in range(min(len(typed),len(prompt))):      
            if typed[x] != prompt[x]:           #只要出现错误就没有 progress
                progress = (x)/(len(prompt))
                break
            else:# 遍历完以后发现 输入结果都正确
                progress = (x+1)/len(prompt)
    upload({'id': user_id, 'progress': progress})
    print(progress)
    
    # END PROBLEM 8


def time_per_word(words, times_per_player):
    """Given timing data, return a match dictionary, which contains a
    list of words and the amount of time each player took to type each word.

    Arguments:
        words: a list of words, in the order they are typed.
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.

    >>> p = [[75, 81, 84, 90, 92], [19, 29, 35, 36, 38]]
    >>> match = time_per_word(['collar', 'plush', 'blush', 'repute'], p)
    >>> match["words"]
    ['collar', 'plush', 'blush', 'repute']
    >>> match["times"]
    [[6, 3, 6, 2], [10, 6, 1, 2]]
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    t = times_per_player
    times = [[t[y][x+1]-t[y][x] for x in range(len(t[y])) if (x+1 < len(t[y]))] for y in range(len(times_per_player))]
         
   # player0_t = [times_per_player[0][x+1] - times_per_player[0][x] for x in range(len(times_per_player[0])) if (x+1 < len(times_per_player[0]))]
    #player1_t = [times_per_player[1][x+1] - times_per_player[1][x] for x in range(len(times_per_player[1])) if (x+1 < len(times_per_player[1]))]
    return match(words,times)
    # END PROBLEM 9


def fastest_words(match):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        match: a match dictionary as returned by time_per_word.

    >>> p0 = [5, 1, 3]
    >>> p1 = [4, 1, 6]
    >>> fastest_words(match(['Just', 'have', 'fun'], [p0, p1]))
    [['have', 'fun'], ['Just']]
    >>> p0  # input lists should not be mutated
    [5, 1, 3]
    >>> p1
    [4, 1, 6]
    """
    player_indices = range(len(get_all_times(match)))  # contains an *index* for each player   0 .. 1 .. player_tol-1
    word_indices = range(len(get_all_words(match)))    # contains an *index* for each word
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"
    words = get_all_words(match)    #get_all_times(match) euqal match["words"]
    times = get_all_times(match)#get_all_words(match)  equal match["times"]
    fastest =[[] for i in player_indices]
    for i, word in enumerate(words):  # 0 'What' 1 'great' 2 'luck'
        word_times = [times[player][i] for player in player_indices]  # 对 各个玩家的当前 word 的 typing time 进行遍历
        idx = min(player_indices, key=lambda x: word_times[x])       #1.the fastest (against all the other players 2. lambda 表达式返回值为 玩家x 在当前 word 的 typing time 3.最终返回值为对应的 list值(此处为索引)
        fastest[idx].append(word)
    return fastest
    

    # DEBUG-CASE:  在某一单词速度相同只进行一次的添加操作
    # 利用 enumerate 实现逐添加操作 >> 同个单词只允许被操作一次  
   
    # 提取在相同位置上的最小值，返回
    # 根据玩家ID顺序返回一个 list of lists 结构 包含各自在与他人对比下的输入最快的单词

    
    # END PROBLEM 10


def match(words, times):
    """A dictionary containing all words typed and their times.

    Arguments:
        words: A list of strings, each string representing a word typed.
        times: A list of lists for how long it took for each player to type
            each word.
            times[i][j] = time it took for player i to type words[j].

    Example input:
        words: ['Hello', 'world']
        times: [[5, 1], [4, 2]]
    """
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return {"words": words, "times": times}


def get_word(match, word_index):
    """A utility function that gets the word with index word_index"""
    assert 0 <= word_index < len(match["words"]), "word_index out of range of words"
    return match["words"][word_index]


def time(match, player_num, word_index):
    """A utility function for the time it took player_num to type the word at word_index"""
    assert word_index < len(match["words"]), "word_index out of range of words"
    assert player_num < len(match["times"]), "player_num out of range of players"
    return match["times"][player_num][word_index]


def get_all_words(match):
    """A selector function for all the words in the match"""
    return match["words"]


def get_all_times(match):
    """A selector function for all typing times for all players"""
    return match["times"]


def match_string(match):
    """A helper function that takes in a match dictionary and returns a string representation of it"""
    return f"match({match['words']}, {match['times']})"


enable_multiplayer = False  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        source = pick(paragraphs, select, i)
        if not source:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(source)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, source))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)
