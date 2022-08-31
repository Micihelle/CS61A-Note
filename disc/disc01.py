# Q1:if statement 和 elif statement的区别
def special_case():
    x = 10
    if x > 0:
        x += 2
    elif x < 13:
        x += 3
    elif x % 2 == 1:
        x += 4
    return x

#special_case()

def just_in_case():
    x = 10
    if x > 0:
        x += 2
    if x < 13:
        x += 3
    if x % 2 == 1:
        x += 4
    return x

#just_in_case()

"""
Summary:
if elif else 结合的condition statement 是直接对 function header 进行判断
如果满足其中的一个条件 则执行对应的 子语句
（即只有if elif expression计算为false value的时候 else的子语句才会被执行）

if if if 结合的condition statement 是依次对If 的条件进行判断
只要满足条件 就会执行里面的子语句

"""
def case_in_point():
    x = 10
    if x > 0:
        x = 12
    if x < 13:
        return x + 3
    if x % 2 == 1:
        return x + 4
    return x

#case_in_point()
"""
初始设想结果
12
15
19

实际输出结果为 12
函数中可以同时包含多个 return 语句，
一旦执行 一个return statement ,funcion就会结束
"""

"""
Q : when do you think using a series of if statements
has the same effect as using both if and elif cases?
"""
"""
故而可以通过 在连续if statament使用中 直接用return 来结束当前函数
来等效替代 if 和 elif statement同时使用的效果
"""


# Q2: Jacket Weather?
def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    "*** YOUR CODE HERE ***"
    """
    Alfonso will only wear a jacket outside if it is below 60 degrees or it is raining.
    满足其中一个条件就 返回True
    """
    
    return (temp<60 or raining==True)

# Q3: Square So Slow
def square(x):
    print("here!")
    return x * x

def so_slow(num):
    x = num
    while x > 0:
        x = x + 1
    return x / 0
"""
能否退出循环？
"""

#  Q4: Is Prime?

# Q5
def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> result is None  # No return value
    True
    """
    "*** YOUR CODE HERE ***"

    """
    Implement the fizzbuzz sequence, 
    which prints out a single statement for each number from 1 to n. For a number i,
    
    If i is divisible by 3 only, then we print "fizz".
    If i is divisible by 5 only, then we print "buzz".
    If i is divisible by both 3 and 5, then we print "fizzbuzz".
    Otherwise, we print the number i by itself.
    """
    
    """
    从1到n遍历
    条件判断输出
    """
    
    for i in range(1,n+1):
        if (i%3==0) and (i%5==0):
            print("fizzbuzz")
        elif i%5==0:
            print("buzz")
        elif i%3==0:
            print("fizz")
        else:
            print(i)
            


# Idea: & 和 and的区别
"""
首先 & 是位运算符，and 是逻辑运算符

a,b分别是整数1和2，以二进制表示分别为：01，10。
&运算结果的二进制为：00，即十进制的 0（按位逻辑运算）。
再如 ：2&3，二进制表示为 10&11，所以结果是 10，即十进制的 2。1 是真，2是真（整数0是否），所以 1 and 2 是真， 0 and 2 是否。
"""
# Q6: Unique Digits


# Python 中关于continue语句的技巧
"""
continue 语句是一个删除的效果，他的存在是为了删除满足循环条件下的某些不需要的成分:
"""

#Description of question:
"""
returns the number of unique digits in a positive integer.

Hints: You can use // and % to separate a positive integer into its one's digit and the rest of its digits.

You may find it helpful to first define a function has_digit(n, k), which determines whether a number n has digit k.

"""


"""
出现了多少种不同的数字
"""
def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(1313131) # 1 and 3
    2
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(10000) # 0 and 1
    2
    >>> unique_digits(101) # 0 and 1
    2
    >>> unique_digits(10) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    list=[]
    while n>=10:
        x = n%10
        n = n//10
        if x not in list:
            list.append(x)
            print('DEBUG: x is', x)
        if n<10 and (n not in list):  #必须和前面缩进一致 否则因为if header 判断为false直接跳过
            list.append(n)  #覆盖最高位数的处理
            print( 'DEBUG: n is', n )
        else:
            continue
    return len(list)

def has_digit(n, k):
    """Returns whether K is a digit in N.
    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    "*** YOUR CODE HERE ***"
    while n>=10:
        if n%10==k:
            return True
        else:
            n=n//10
            if n%10==k:
                return True
    return False
        
    "*** YOUR CODE HERE ***"
