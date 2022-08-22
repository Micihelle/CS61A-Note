#https://inst.eecs.berkeley.edu/~cs61a/su20/hw/hw01/
#Q2: A Plus Abs B
from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    >>> # a check that you didn't change the return statement!
    >>> import inspect, re
    >>> re.findall(r'^\s*(return .*)', inspect.getsource(a_plus_abs_b), re.M)
    ['return h(a, b)']
    """
    if b >= 0:
        h= add  #变量指向函数
    else:
        h = sub
    return h(a,b)

#print(a_plus_abs_b(2, 3))
#print(a_plus_abs_b(2, -3))

'''
注意return语句中的h(a,b)，对表达式求值并返回结果
'''


#Q3: Two of Three
def two_of_three(x, y, z):
    """Return a*a + b*b, where a and b are the two smallest members of the
    positive numbers x, y, and z.

    >>> two_of_three(1, 2, 3)
    5
    >>> two_of_three(5, 3, 1)
    10
    >>> two_of_three(10, 2, 8)
    68
    >>> two_of_three(5, 5, 5)
    50
    >>> # check that your code consists of nothing but an expression (this docstring)
    >>> # a return statement
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(two_of_three)).body[0].body]
    ['Expr', 'Return']
    """
    return pow(min(x,y,z),2)+pow(max(min(x,y),min(x,z),min(y,z)),2)

#print(two_of_three(1, 2, 3))
#print(two_of_three(5, 3, 1))
#print(two_of_three(10, 2, 8))
#print(two_of_three(5, 5, 5))

#Q4
def largest_factor(x):
    """Return the largest factor of x that is smaller than x.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    factor =[]
    for i in range(x-1,0,-1):
        if(x%i==0):
            factor.append(i)
    return max(factor)
    '''
    创建因数列表 （所有可以整除这个数的数,不包括这个数自身）
    除数的选取（从本身到1进行遍历）
    判断是否能够除尽 a%b==0,如果可以则添加到列表中
    挑选最大因数（除了本身）return
    '''

#print(largest_factor(15))
#print(largest_factor(80))
#print(largest_factor(13))

#Q5 构建实现if语句功能的function
def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.条件为真值 return true result，否则 return false_result

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result

#print(if_function(True, 2, 3))
#print(if_function(False, 2, 3))
#print(if_function(3==2, 3+2, 3-2))
#print(if_function(3>2, 3+2, 3-2))


'''
if 3>2:
    print(3+2)
else:
    print(3-2)
'''
#对上面代码证伪
def with_if_statement():
    """
    >>> result = with_if_statement()
    47
    >>> print(result) #print函数为Non-pure function（除了返回值以外还会对解释器或计算的状态进行更改,(display and return)
    对于没有返回值，没有输出代码块的函数 ,无法在全局框架下display

    None
    """
    if cond():
        return true_func()
    else:
        return false_func()

def with_if_function():
    """
    >>> result = with_if_function()
    42
    47
    >>> print(result)
    None
    """
    return if_function(cond(), true_func(), false_func())
"""
利用cond()代替condition判断 ； 如果为true value 返回true_func();如果为false value 返回false_func()

"""

def cond():
    return 1

def true_func():
    print(42)

def false_func():
    print(47)

'''
编译载入Module
'''

'''
def func1():
    print(42)
    return 42


def func2(a, b):
 res = a + b
'''

# Q6 Hailstone sequence
def hailstone(x):
    """Print the hailstone sequence starting at x and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """

def hailstone(x):
    i = 1
    while (x > 1):
        print(x)
        i +=1
        if (x%2==0):
            x=int(x/2)
        else:
            x=int(3*x+1)
    print(x)
    return i





