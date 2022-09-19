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


Problem8 CS61A 文档说明 学习笔记：
关于多参数传入的代码实现：
EX:
``` python
def printed(f):
    def print_and_return(*args):
        result = f(*args)
        print('Result:', result)
        return result
    return print_and_return
```

具体实现情况：
``` python
"""
可以接受 需要传递任意数量的参数传递的 函数
EX1: 接受两个或者三个参数
printed_pow = printed(pow)
printed_pow(2, 8)

Result: 256
256
###
printed_pow = printed(pow)
printed_pow(2, 8,10)

Result: 6
6

EX2:接受一个参数
>>> printed_abs = printed(abs)
>>> printed_abs(-10)
Result: 10
10

"""
```

重新考虑Problem 8 先概括自己的实现思路 然后参考别人的代码
思路实现：由Case1可得
averaged_and_return 返回值为 function 此时的代码为
``` python
    def averaged_and_return(*args):
        sum = 0
        for i in range(total_samples):
            result = original_function(*args)
            sum = sum + result
        return sum/total_samples
    return averaged_and_return
```
通过 h(x)=f(g(x)) 的想法重新设计函数

``` python
def make_averaged(original_function, total_samples=1000):
    def averaged_and_return(*args):
        result = original_function(*args)
        def sum_average(result):
            sum = 0
            for i in range(total_samples):
                sum = sum + result()
            return sum/total_samples
        return sum_average(result)
    return averaged_and_return
```

但是在sum 求和行出错 不太清楚 调用 result的值该如何求和 即传入函数的返回值要怎么保证多次调用(idea 1)

参考别人代码发现自己的第一段代码和大佬比较相似  直接考虑第一段代码出错的地方
...发现没有错误 之前应该是 对 result 多运行了一次  result()

Problem 9 
关于每回合最大投掷次数：
problem 9 中的注释可得默认情况下每回合的最大游戏投掷次数
`Return the number of dice (1 to 10) that gives the highest average turn score `


**根据problem 9 对 max_scoring_num_rolls的要求 对于不同的投掷次数 计算对应的该回合得到的点数 然后在最大平均分的基础上 找到最小的投掷次数 （可能后续要计算获胜的概率）**
**如果在该回合内每次投掷得到的点数都相同 则必然返回投掷次数最多的可能（10）**
**如果在该回合内每次投掷得到的点数存在不同情况，则分别对不同投掷次数的情况进行计算，找到最高平均分对应的投掷次数，如果存在两个或两个以上相同的投掷次数，则让函数返回最少的投掷次数。**

**通过调用 roll_dice 直接考虑每回合任意次数 返回的点数**
**(roll_dice function 内部已经考虑了 游戏规则sow sad 对该回合任意投掷点数对最终得分的影响)**`roll_dice(num_rolls, dice=six_sided)`



不太清楚关于最大值搜寻的具体代码，此时代码为
``` python
def max_scoring_num_rolls(dice=six_sided, total_samples=1000):
    num = 0
    num_rolls=[]
    average = make_averaged(dice, total_samples)
    if average() == dice() :
        return 10
    #从 1 到 10
    while num<=10
    num+=1
    num_rolls =roll_doce(num,dice)
```

参考了北大学长
``` python
def max_scoring_num_rolls(dice=six_sided, trials_count=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE over TRIALS_COUNT times.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(1, 6)
    >>> max_scoring_num_rolls(dice)
    1
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    ma = make_averaged(roll_dice, trials_count)
    trials = [ma(i, dice) for i in range(1, 11)]
    return trials.index(max(trials)) + 1
```
从def 行开始逐行分析，对于def 的分析 结合验证情况会更好理解
``` python
#Question 9 > Suite 2 > Case 1

from hog import *
dice = make_test_dice(3)   # dice always returns 3
DEBUG = max_scoring_num_rolls(dice, total_samples=1000)

10
```
在全局frame下定义了 dice 然后将全局frame下定义的 dice传入 max_scoring_num_rolls 的formal parameter:`dice` 包括了函数体剩余部分`dice`的使用

相关教材内容于1.6.2，可参考 `gloden ratio.py` 中形参的指向

ma 行：`calling roll_dice with the provided DICE over TRIALS_COUNT times.`
- roll_dice 调用： `def roll_dice(num_rolls, dice=six_sided)`


trials行： 
- 1.包括了列表的创建于对各种投掷情况的记录。ma(i,dice)传入 投掷次数 i 和 每次投掷对应点数情况 dice 计算对应的点数情况
利用前面def 的 func  make_averaged 在 `original_function`处可接收具有任意形式参数的函数，然后返回一个可调用的能接受对应数量参数的函数。
如problem 8中的验证情况  

``` python
    >>> dice = make_test_dice(4, 2, 5, 1)
    >>> averaged_dice = make_averaged(roll_dice, 1000)
    >>> averaged_dice(1, dice)
    3.0
```   
- 2.利用了python 搜寻本身的特性 直接返回最高平均分对应的最小投掷次数情况

return行: 同样考虑了python 序号的特性 在index的基础上加 1

后续可调用的地方：一处对Python特性的利用及注意事项
- 利用了python index 搜寻本身的特性 直接返回最高平均分（函数最大值）对应的最小投掷次数情况（变量最小值）
- 考虑 python 序号的特性 在index 得到的返回值的基础上加 1

对应环境图：
- [Python Tutor](https://pythontutor.com/composingprograms.html#code=from%20random%20import%20randint%0A%0A%23%20A%20fair%20dice%20produces%20each%20possible%20outcome%20with%20equal%20probability.%0Adef%20make_fair_dice%28sides%29%3A%0A%20%20%20%20%22%22%22Return%20a%20die%20that%20returns%201%20to%20SIDES%20with%20equal%20chance.%22%22%22%0A%20%20%20%20assert%20type%28sides%29%20%3D%3D%20int%20and%20sides%20%3E%3D%201,%20'Illegal%20value%20for%20sides'%0A%0A%20%20%20%20def%20dice%28%29%3A%0A%20%20%20%20%20%20%20%20return%20randint%281,%20sides%29%20%23randrange%28start,%20stop%2B1%29%20%E5%AF%B9%20formal%20parameter%0A%20%20%20%20return%20dice%0A%0A%0Afour_sided%20%3D%20make_fair_dice%284%29%0Asix_sided%20%3D%20make_fair_dice%286%29%0A%0Adef%20make_test_dice%28*outcomes%29%3A%0A%20%20%20%20index%20%3D%20len%28outcomes%29%20-%201%20%20%0A%0A%20%20%20%20def%20dice%28%29%3A%0A%20%20%20%20%20%20%20%20nonlocal%20index%20%20%20%23nonlocal%E5%8F%AA%E8%83%BD%E5%9C%A8%E5%B0%81%E8%A3%85%E5%87%BD%E6%95%B0%E4%B8%AD%E4%BD%BF%E7%94%A8%EF%BC%8C%E5%9C%A8%E5%A4%96%E9%83%A8%E5%87%BD%E6%95%B0%E5%85%88%E8%BF%9B%E8%A1%8C%E5%A3%B0%E6%98%8E%EF%BC%8C%E5%9C%A8%E5%86%85%E9%83%A8%E5%87%BD%E6%95%B0%E8%BF%9B%E8%A1%8Cnonlocal%E5%A3%B0%E6%98%8E%EF%BC%8C%E8%BF%99%E6%A0%B7make_test_dice%28%29%E5%92%8Cdice%28%29%E5%86%85%E7%9A%84index%E6%98%AF%E5%90%8C%E4%B8%80%E4%B8%AA%E5%8F%98%E9%87%8F%0A%20%20%20%20%20%20%20%20index%20%3D%20%28index%20%2B%201%29%20%25%20len%28outcomes%29%20%20%20%23%20%E5%B0%86index%20%E9%99%90%E5%AE%9A%E5%9C%A8%5B0,len%28outcomes%29-1%5D%E7%9A%84%E5%8C%BA%E9%97%B4%20%20%20%20%20%E4%BB%8E%E6%9C%80%E9%AB%98%E4%BD%8D%E5%BC%80%E5%A7%8B%E5%81%9A%20%25%20%E8%BF%90%E7%AE%97%20%E8%B7%9F%E8%BE%93%E5%85%A5%E7%9A%84%E9%A1%BA%E5%BA%8F%E4%B8%80%E8%87%B4EX%3A2%253%3E%3E%202/3%3D0......2%20%E5%8F%AF%E7%BF%BB%E9%98%85Discrete%20%E4%B8%AD%E5%85%B3%E4%BA%8E%E5%90%8C%E4%BD%99%E7%9A%84%E8%A7%A3%E9%87%8A%0A%20%20%20%20%20%20%20%20return%20outcomes%5Bindex%5D%0A%20%20%20%20return%20dice%20%20%20%23%E8%BF%94%E5%9B%9Efunction%20dice%28%29%20%20%E5%8F%98%E9%87%8F%E6%8C%87%E5%90%91dice%28%29%0A%0Adef%20roll_dice%28num_rolls,%20dice%3Dsix_sided%29%3A%20%0A%20%20%20%20%22***%20YOUR%20CODE%20HERE%20***%22%0A%20%20%20%20sum%20%3D%200%0A%20%20%20%20while%20num_rolls%20%3A%0A%20%20%20%20%20%20%20%20x%3D%20dice%28%29%0A%20%20%20%20%20%20%20%20if%20x%3D%3D1%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%201%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20num_rolls%3Dnum_rolls-1%0A%20%20%20%20%20%20%20%20%20%20%20%20sum%20%3D%20sum%20%2B%20x%0A%20%20%20%20%20%20%20%20%20%20%20%20continue%0A%20%20%20%20return%20sum%0A%20%20%20%20%23%20END%20PROBLEM%201%0A%0Adef%20make_averaged%28original_function,%20total_samples%3D1000%29%3A%0A%20%20%20%20%23%20BEGIN%20PROBLEM%208%0A%20%20%20%20%22***%20YOUR%20CODE%20HERE%20***%22%0A%20%20%20%20%22current%20%20%3D%20total_samples%22%20%20%20%0A%20%20%20%20def%20averaged_and_return%28*args%29%3A%0A%20%20%20%20%20%20%20%20sum%20%3D%200%0A%20%20%20%20%20%20%20%20for%20i%20in%20range%28total_samples%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20result%20%3D%20original_function%28*args%29%0A%20%20%20%20%20%20%20%20%20%20%20%20sum%20%3D%20sum%20%2B%20result%0A%20%20%20%20%20%20%20%20return%20sum/total_samples%0A%20%20%20%20return%20averaged_and_return%0A%20%20%20%20%0Adef%20max_scoring_num_rolls%28dice%3Dsix_sided,%20total_samples%3D1000%29%3A%0A%20%20%20%20%23%20BEGIN%20PROBLEM%209%0A%20%20%20%20%22***%20YOUR%20CODE%20HERE%20***%22%0A%20%20%20%20ma%20%3D%20make_averaged%28roll_dice,%20total_samples%29%0A%20%20%20%20trials%20%3D%20%5Bma%28i,%20dice%29%20for%20i%20in%20range%281,%2011%29%5D%0A%20%20%20%20return%20trials.index%28max%28trials%29%29%20%2B%201%0A%20%20%20%20%0A%20%20%20%20%0Afrom%20hog%20import%20*%0Adice%20%3D%20make_test_dice%283%29%20%20%20%23%20dice%20always%20returns%203%0ADEBUG%20%3D%20max_scoring_num_rolls%28dice,%20total_samples%3D1000%29%0A%20%20%20%20%0A%20%20%20%20&cumulative=true&curInstr=13&mode=display&origin=composingprograms.js&py=3&rawInputLstJSON=%5B%5D)


关于最终策略环境计算和 胜率计算
发现run_experiments 并没有得到计算结果，message也没有怎么输出
此时 func play 代码为：
``` python
def play(strategy0, strategy1, score0=0, score1=0, dice=six_sided,goal=GOAL_SCORE, say=silence):
    who = 0  # Who is about to take a turn, 0 (first) or 1 (second)
    leader = None  # To be used in problem 7
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    print("DEBUG:before while score0 is ", score0)
    player = 0
    while not who:
        score0 = score0 + take_turn(strategy0(score0,score1), score0, score1, dice, goal)
        score0 = score0 + pigs_on_prime(score0, score1)
        #print("DEBUG:before player0 turn  leader is ", leader)
        leader,message = say(score0, score1,leader)
        #print("DEBUG:after player0 turn  leader is ", leader)
        print("DEBUG:after while score0 is ", score0)
        print (message)

        score1 = score1 + take_turn(strategy1(score1,score0), score1, score0, dice, goal)
        score1 = score1 + pigs_on_prime(score1, score0)
        leader,message = say(score0, score1,leader)
        #print("DEBUG:after player1 turn  leader is ", leader)
        print("DEBUG:after while score1 is ", score1)
        print (message)

    return score0,score1
```
对比其他代码发现没有将who的循环调用起来
此时代码逻辑
在player 0 player 1 各自确定strategy后还有对pigs_on_prime的策略的应用？() 

改进前结构：
``` python
    while max(score0, score1) < goal:
        
        score0 = score0 + take_turn(strategy0(score0,score1), score0, score1, dice, goal)
        score0 = score0 + pigs_on_prime(score0, score1)
        score1 = score1 + take_turn(strategy1(score1,score0), score1, score0, dice, goal)
        score1 = score1 + pigs_on_prime(score1, score0)
```
改进 who:
```python
    while max(score0, score1) < goal:
        if who==0:
            score0 = score0 + take_turn(strategy0(score0,score1), score0, score1, dice, goal)
            score0 = score0 + pigs_on_prime(score0, score1)
        else:
            score1 = score1 + take_turn(strategy1(score1,score0), score1, score0, dice, goal)
            score1 = score1 + pigs_on_prime(score1, score0)
        who = next_player(who)
```
确保可以在达到goal 之前将score0 score1 的值传递出去，避免直接被assume 截止

> ## idea  
idea1 
`*args` 使用的时候 如果不传入参数 会得到函数的 return value 吗

电脑如何画environment diagrams：
[Python tutor](https://pythontutor.com/composingprograms.html#mode=edit): 学会把代码框架简化 否则具体运行起来得到的环境图 反而不太容易理解参数之间的传递

> ## Summary  
对游戏规则的整理：
关于 dice.py:
A dice function takes no arguments and returns a number from 1 to n
(inclusive), where n is the number of sides on the dice.

两名玩家轮流投骰子，决定当前的投掷次数。
两种游戏策略
- 1.Oink Points
- 2.Pigs on Prime

当前回合的游戏情况：在Problem 5 中func play(strategy0, strategy1, score0=0, score1=0, dice=six_sided,goal=GOAL_SCORE, say=silence)
其中 stragey 函数决定了投掷的次数 如果选择0 则进行 Oink Points ，并且有可能触发Pigs on Prime


关于每回合最大投掷次数：
problem 9 中的注释可得默认情况下每回合的最大游戏投掷次数

`Return the number of dice (1 to 10) that gives the highest average turn score `


### 根据每个problem 的可调用代码整理

Problem 5:注意调用其他fun中包含的assert语句对循环结果的截止及返回值传递的影响

用一些具体函数代替逻辑运算
`max(score0, score1) < goal`


Problem 8: 任意数量的参数传递和随机函数结果的多次调用：(original_function 可为需要接受任意数量参数的函数 total_samples为调用次数 最终随机函数多次调用结果的平均值)
``` python
def make_averaged(original_function, total_samples=1000):
    def averaged_and_return(*args):
        sum = 0
        for i in range(total_samples):
            result = original_function(*args)
            sum = sum + result
        return sum/total_samples
    return averaged_and_return
```


2020.9.10
30min problem 8 debug

2022.9.11:
- 1h 20min: 对problem 9 具体需求的理解 准备参考优秀代码改进自己的

2022.9.12:
- 1h 完成了对Problem 9参考的学习：原先设想的两部分内容都有被优秀代码很好的实现 补充列表元素的创建反而体现了对python特性的不了解(大佬666)
- 1h 完成了所有Problem 的主要需求:
- 1h +  整理 实验和胜率评估代码   及可调用代码：
目前进度：
重新理解Problem5的 代码框架，
配合ok 实验要求 进行关于Problem5的修正 DEBUG
Problem12可实现性 胜率评估代码 
进行project总结 根据每个problem 整理对应的后续可多次调用的代码

2022.9.13:
- 1h 完成了关于Problem 5 的调整

后续安排：关于problem 7 的调整

- summary:在一开始做的时候就找到可以参考的资源


2022.9.14
30min
防止 None 的输出 来计算各个策略的胜率
后续安排： 
- 输出None 对计算胜率的影响
[python print打印时出现None](https://blog.csdn.net/weixin_42212753/article/details/111147961)
- 关于 run_experiments()函数 的调用

2022.9.19思路衔接：对可调用代码的初步整理，在Project2中进行进一步归纳整理(应用为导向,知识存档)