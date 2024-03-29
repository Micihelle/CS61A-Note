"""CS 61A Presents The Game of Hog."""

from dice import six_sided, four_sided, make_test_dice
from ucb import main, trace, interact
from math import sqrt

GOAL_SCORE = 100  # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################


def roll_dice(num_rolls, dice=six_sided): #(optional):默认值为six_sided
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.

    num_rolls:  The number of dice rolls that will be made.
    dice:       A function that simulates a single dice roll outcome.
    """

    """
#游戏规则实现阶段：
Sow Sad 规则具体代码实现

根据 num_rolls( 投骰子的次数） dice( 随机点数或者人为设定的测试点数） 返回这一回合的点数总和
"""
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    sum = 0
    while num_rolls :
        x= dice()
        if x==1:
            return 1
        else:
            num_rolls=num_rolls-1
            sum = sum + x
            continue
    return sum
    # END PROBLEM 1


def oink_points(player_score, opponent_score):
    """Return the points scored by player due to Oink Points.

    player_score:   The total score of the current player.
    opponent_score: The total score of the other player.
    """
    # BEGIN PROBLEM 2
    tens = (opponent_score//10) % 10
    ones = opponent_score % 10
    x = 2*tens - ones
    if x>1:
        return x
    else:
        return 1
    # END PROBLEM 2


def take_turn(num_rolls, player_score, opponent_score, dice=six_sided, goal=GOAL_SCORE): #不同于设置function为 defalut value
    """Simulate a turn rolling NUM_ROLLS dice,
    which may be 0 in the case of a player using Oink Points.
    Return the points scored for the turn by the current player.

    num_rolls:       The number of dice rolls that will be made.
    player_score:    The total score of the current player.
    opponent_score:  The total score of the opponent.
    dice:            A function that simulates a single dice roll outcome.
    goal:            The goal score of the game.
    """
    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert max(player_score, opponent_score) < goal, 'The game should be over.'
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    """
    num_rolls 接受是否using Olink Points or the number of rolls
    使用using Olink Points: returns the number of points scored by Oink Points

    （如果规则为 使用这些num_rolls 来增加点数)直接return 增加的点数 方便后续函数的封装调用？ 直接返回最终得分可能不太好调用
    """
    if num_rolls >0 :
        return roll_dice(num_rolls, dice)  #注意dice 的传递
    else:
        return oink_points(player_score, opponent_score)
    # END PROBLEM 3


def is_prime(n):
    if n == 2:
        return True
    else:
        i = 2
        while i <= sqrt(n): #square root
            if n % i == 0:
                return False
            i += 1
        return True


def pigs_on_prime(player_score, opponent_score):
    """Return the points scored by the current player due to Pigs on Prime.

    player_score:   The total score of the current player.
    opponent_score: The total score of the other player.
    """
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    """
increases to the next prime number
player 0:
    is_prime()
    next prime
    return the addtional points that between itself and the next prime
player 1 then takes their turn

#prime: 一个大于1的自然数，除了1 和它自身外，不能整除其他自然数的数叫做质数
"""
    if is_prime(player_score):
        x=player_score
        while x:
            x=x+1
            if is_prime(x):
                return (x - player_score)
    return 0
    # END PROBLEM 4


def next_player(who):
    """Return the other player, for a player WHO numbered 0 or 1.

    >>> next_player(0)
    1
    >>> next_player(1)
    0
    """
    return 1 - who


def silence(score0, score1, leader=None):
    """Announce nothing (see Phase 2)."""
    return leader, None


def play(strategy0, strategy1, score0=0, score1=0, dice=six_sided,goal=GOAL_SCORE, say=silence):
    """Simulate a game and return the final scores of both players, with Player
    0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments (the
    current player's score, and the opponent's score), and returns a number of
    dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first.
    strategy1:  The strategy function for Player 1, who plays second.
    score0:     Starting score for Player 0
    score1:     Starting score for Player 1
    dice:       A function of zero arguments that simulates a dice roll.
    goal:       The game ends and someone wins when this score is reached.
    say:        The commentary function to call every turn.

    strategy function(Phase 3 ):
        given a player's score and their opponent's score,
        returns the number of dice that the current player will roll in the turn.

    EX:strategy1(score1, score0)  strategyX(current_score,opponent_score)
    1. num_dice \\ order
    2. strategy: determine how many dice are rolled each turn
    3. additional points: pigs_on_prime

    stragey 函数决定了投掷的次数 如果选择0 则进行 Oink Points ，并且有可能触发Pigs on Prime
    A turn is defined as one roll of the dice.
    对单个回合的处理
    """
    who = 0  # Who is about to take a turn, 0 (first) or 1 (second)
    leader = None  # To be used in problem 7
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    #print("DEBUG:before while score0 is ", score0)
    while max(score0, score1) < goal:
        if who==0:
            score0 = score0 + take_turn(strategy0(score0,score1), score0, score1, dice, goal)
            score0 = score0 + pigs_on_prime(score0, score1)
            #print("DEBUG:before player0 turn  leader is ", leader)
            leader,message = say(score0, score1,leader)
            #print("DEBUG:after while score0 is ", score0)
            #print("DEBUG:before turn to player1 score1 is ", score1)
            if message:
                print (message)
        else:
            score1 = score1 + take_turn(strategy1(score1,score0), score1, score0, dice, goal)
            score1 = score1 + pigs_on_prime(score1, score0)
            leader,message = say(score0, score1,leader)
            #print("DEBUG:after player1 turn  leader is ", leader)
            #print("DEBUG:after while score1 is ", score1)
            if message:
                print (message)
        who = next_player(who)
    return score0,score1


    # END PROBLEM 5
    # (note that the indentation for the problem 7 prompt (***YOUR CODE HERE***) might be misleading)
    # BEGIN PROBLEM 7
    "*** YOUR CODE HERE ***"

    # END PROBLEM 7

#######################
# Phase 2: Commentary #
#######################


def say_scores(score0, score1, player=None):
    """A commentary function that announces the score for each player."""
    message = f"Player 0 now has {score0} and now Player 1 has {score1}"
    return player, message


def announce_lead_changes(score0, score1, last_leader=None):
    """A commentary function that announces when the leader has changed.

    >>> leader, message = announce_lead_changes(5, 0)
    >>> print(message)
    Player 0 takes the lead by 5
    >>> leader, message = announce_lead_changes(5, 12, leader)
    >>> print(message)
    Player 1 takes the lead by 7
    >>> leader, message = announce_lead_changes(8, 12, leader)
    >>> print(leader, message)
    1 None
    >>> leader, message = announce_lead_changes(8, 13, leader)
    >>> leader, message = announce_lead_changes(15, 13, leader)
    >>> print(message)
    Player 0 takes the lead by 2
    """

    """
目前分数领先的玩家 比对方高多少分
领先玩家发生变换的时候 需要提供更加具体的 message
last_leader的assignment
先对score判断得到last_leader last_leader return 给leader
"""
    # BEGIN PROBLEM 6
    "*** YOUR CODE HERE ***"

    if score0>score1:              #判断这一轮的leader
        leader = 0
    elif score1>score0:
        leader = 1
    else:
        leader = last_leader          #分数相同情况

    if last_leader == None:        #是否记录了上一轮的leader 可简化成last_leader == None or last_leader != leader
        last_leader = leader
        message = f"Player {last_leader} takes the lead by {abs(score0-score1)}"
        return last_leader,message
    elif last_leader != leader:      #leader是否发生变更
        last_leader = leader
        message = f"Player {last_leader} takes the lead by {abs(score0-score1)}"
        return last_leader,message
    else:                                       #leader未发生变更
        return leader,None

    # END PROBLEM 6


def both(f, g):
    """A commentary function that says what f says, then what g says.

    >>> say_both = both(say_scores, announce_lead_changes)
    >>> player, message = say_both(10, 0)
    >>> print(message)
    Player 0 now has 10 and now Player 1 has 0
    Player 0 takes the lead by 10
    >>> player, message = say_both(10, 8, player)
    >>> print(message)
    Player 0 now has 10 and now Player 1 has 8
    >>> player, message = say_both(10, 17, player)
    >>> print(message)
    Player 0 now has 10 and now Player 1 has 17
    Player 1 takes the lead by 7
    """
    def say(score0, score1, player=None):
        f_player, f_message = f(score0, score1, player)
        g_player, g_message = g(score0, score1, player)
        if f_message and g_message:
            return g_player, f_message + "\n" + g_message
        else:
            return g_player, f_message or g_message
    return say


#######################
# Phase 3: Strategies #
#######################

### Return a XXX that always rolls N dice.
def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments (the
    current player's score, and the opponent's score), and returns a number of
    dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n
    return strategy


def make_averaged(original_function, total_samples=1000):
    """Return a function that returns the average value of ORIGINAL_FUNCTION
    called TOTAL_SAMPLES times.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(4, 2, 5, 1)
    >>> averaged_dice = make_averaged(roll_dice, 1000)
    >>> averaged_dice(1, dice)
    3.0
    """

    """
    call original_function a total of total_samples times and
    return the average of the results of these calls.

    accepts an arbitrary number of arguments>> formal parameter original_function
    and then calls another function using exactly those arguments.
    一部分负责 任意数量的参数传递 另一部分负责函数的多次调用

    游戏策略实现阶段：
    接受 original_function  total_sample (样本总和） 返回一个函数
    """
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    "current  = total_samples"   #在print_and_return function外部使用了同名变量会引起歧义 需要声明
    def averaged_and_return(*args):
        sum = 0
        for i in range(total_samples):
            result = original_function(*args)
            sum = sum + result
        return sum/total_samples
    return averaged_and_return


    # END PROBLEM 8


def max_scoring_num_rolls(dice=six_sided, total_samples=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn score
    by calling roll_dice with the provided DICE a total of TOTAL_SAMPLES times.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(1, 6)
    >>> max_scoring_num_rolls(dice)
    1
    """

    """
    maximum average score
    If two numbers of rolls are tied for the maximum average score, return the lower number
    (最高 make_average 的 最低  num_rolls 
    对 make_average 和 roll_dice 评估

    """

    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    ma = make_averaged(roll_dice, total_samples)
    trials = [ma(i, dice) for i in range(1, 11)]
    return trials.index(max(trials)) + 1


    # END PROBLEM 9


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(6)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    six_sided_max = max_scoring_num_rolls(six_sided)
    print('Max scoring num rolls for six-sided dice:', six_sided_max)
    print('always_roll(6) win rate:', average_win_rate(always_roll(6)))

    print('always_roll(8) win rate:', average_win_rate(always_roll(8)))
    print('oink_points_strategy win rate:', average_win_rate(oink_points_strategy))
    print('pigs_on_prime_strategy win rate:', average_win_rate(pigs_on_prime_strategy))
    #print('final_strategy win rate:', average_win_rate(final_strategy))
    "*** You may add additional experiments as you wish ***"


def oink_points_strategy(score, opponent_score, threshold=8, num_rolls=6):
    """This strategy returns 0 dice if that gives at least THRESHOLD points, and
    returns NUM_ROLLS otherwise.
    判断有利于实现oink_Points 策略的情况
    """
    # BEGIN PROBLEM 10
    """
解释了为什么problem2 不直接返回加上点数后的最终值
"""
    if oink_points(score, opponent_score)>=threshold:
        return 0
    else:
        return num_rolls
    # END PROBLEM 10


def pigs_on_prime_strategy(score, opponent_score, threshold=8, num_rolls=6):
    """This strategy returns 0 dice when this would result in Pigs on Prime taking
    effect. It also returns 0 dice if it gives at least THRESHOLD points.
    Otherwise, it returns NUM_ROLLS.

    pigs_on_prime()
    oink_points()
    """
    # BEGIN PROBLEM 11
    oink_score = score + oink_points(score, opponent_score)
    
    if oink_points(score, opponent_score)+pigs_on_prime(oink_score, opponent_score)>=threshold:
        return 0
    else:
        return num_rolls
    # END PROBLEM 11


def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.
    得到目标分数才能得到胜利 而不是超过目标分数
    Choose the num_rolls and threshold arguments carefully.
    
    *** YOUR DESCRIPTION HERE ***
    """
    # BEGIN PROBLEM 12


    # END PROBLEM 12

##########################
# Command Line Interface #
##########################

# NOTE: Functions in this section do not need to be changed. They use features
# of Python not yet covered in the course.


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()
