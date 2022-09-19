Problem7处理前 Problem5 结果
problem5 只实现了一个回合的情况
Problem7 要求当回合内 player0 的点数情况一次 和player1 的点数情况一次
``` python
def play(strategy0, strategy1, score0=0, score1=0, dice=six_sided,goal=GOAL_SCORE, say=silence):
    """

    strategy function(Phase 3 ):
        given a player's score and their opponent's score,
        returns the number of dice that the current player will roll in the turn.

    EX:strategy1(score1, score0)  strategyX(current_score,opponent_score)
    1. num_dice \\ order
    2. strategy: determine how many dice are rolled each turn
    3. additional points: pigs_on_prime

    A turn is defined as one roll of the dice.
    对单个回合的处理
    """
    who = 0  # Who is about to take a turn, 0 (first) or 1 (second)
    leader = None  # To be used in problem 7
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    print("DEBUG:before while score0 is ", score0)
    while not who:
        who=next_player(who)
        print("DEBUG:before take_turn score0 is ", score0)
        score0 = score0 + take_turn(strategy0(score0,score1), score0, score1, dice, goal)#此处再用=设置defalut value会影响play() argumens的传递
        print("DEBUG:after take_turn score0 is ", score0)
        score0 = score0 + pigs_on_prime(score0, score1)
        print("DEBUG:after pigs_on_prime score0 is ", score0)
        if score0>=goal:
            return score0,score1
        else:
            score1 = score1 + take_turn(strategy1(score1,score0), score1, score0, dice, goal)
            score1 = score1 + pigs_on_prime(score1, score0)
            return score0,score1
```

Problem7：Question 7 > Suite 2 > Case 4

#关于curr_count 逐增的问题

参考别人代码和 ` leader = None  # To be used in problem 7` 这一行代码后的思路
利用player 接受 return 的curr_count 

function play 中的leader初始值为None 在第一次调用 function say的时候 
curr_count + 1 =2

case4 编译结果通过 考虑其他case（区别在于初始值是否为None 所以其他case编译结果不受影响）

Probelm8:Question 8 > Suite 2 > Case 2
在上一个case中实现了original_function的多次调用 但是没有实现传递多个args的功能
``` python
def make_averaged(original_function, total_samples=1000):
    def averaged_and_return(function=original_function, total=total_samples):
        sum = 0
        for i in range(0,total):
            sum = sum + function()
            #print("DEBUG: sum is ",sum)
        return sum/total
    return averaged_and_return
```

考虑传递args的初步实现
``` python
def make_averaged(original_function, total_samples=1000):
    def averaged_and_return(*args, total=total_samples):
        sum = 0
        for i in range(total):
            result = make_averaged(*args)
            sum = sum + result()
            #print("DEBUG: sum is ",sum)
        return sum/total
    return averaged_and_return
```

参考大佬的代码：
``` python
def make_averaged(original_function, total_samples=1000):
    def averaged_dice(*args):
        sum = 0
        for i in range(total_samples):
            sum += original_function(*args)
        return sum / total_samples
    return averaged_dice
```

想到两个问题:
- 1. function body 内定义函数 是怎么传递参数的？(function averaged_dice 里面的total_samples 和 original_function 是怎么传递进去的)
- 2. *args 的使用问题 能否在使用 *args 后 在设置其他参数的传入 