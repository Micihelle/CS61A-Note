
关于Q4之前的具体代码可见同根文件夹下 `test.py`
Q4之后的代码见 `lab02.py`

## Q1: HOF Diagram Practice

DEBUG: 设置不同数量的形参传递入口 得到的函数不一样？即使是同名函数
关于环境图：从最基本的形参结构入手进行传递参数之间的环境状态分析

对比分析：
``` python
a = lambda x: x * 2 + 1
def b(b, x):
    return b(x + a(x)) #此处为 formal parameter b
x = 3
x = b(a, x)
g = (lambda y: y())(f)
```


``` python
n = 7

def f(x):
    n = 8
    return x + 1

def g(x):
    n = 9
    def h():
        return x + 1
    return h

def f(f, x):
    return f(x + n)

f = f(g, n)
g = (lambda y: y())(f)
```


## Q2: WWPD: Lambda the Free
> A lambda expression does not automatically bind the function object that it returns to an intrinsic name.

``` python
>>> (lambda: 3)()  # Using a lambda expression as an operator in a call exp.(operator 调用)
```

``` python
b = lambda x: lambda: x  # Lambdas can return other lambdas!
c = b(88)
c
```

EX:将函数作为参数传递
``` python
d = lambda f: f(4)  # They can have functions as arguments as well
def square(x):
    return x * x
d(square)
```

EX: None 在 python interpreter 的 display
``` python
x = None # remember to review the rules of WWPD given above!
x
lambda x: x # lambda function display
```

EX:变量传递范围 对应的frame
``` python
>>> #
>>> # Pay attention to the scope of variables
>>> z = 3
>>> e = lambda x: lambda y: lambda: x + y + z  #第三级函数不接受参数的传递 直接返回表达式 x+y+z
>>> e(0)(1)()

>>> e(0)(1)(3)
TypeError: <lambda>() takes 0 positional arguments but 1 was given
```

EX: lambda 多层函数调用 及对应参数传入
``` python
# Try drawing an environment diagram if you get stuck!
higher_order_lambda = lambda f: lambda x: f(x)
g = lambda x: x * x
higher_order_lambda(g)(2) # Which argument belongs to which function call?
```

``` Python
>>> call_thrice = lambda f: lambda x: f(f(f(x)))
>>> call_thrice(lambda y: y + 1)(0)
```


EX:  display function
``` python
print_lambda = lambda z: print(z)
print_lambda
```


## Q3: WWPD: Higher Order Functions
EX: 基于Higher Order Functions的 绝对值函数
``` python
>>> def even(f):
...     def odd(x):
...         if x < 0:
...             return f(-x)
...         return f(x)
...     return odd

#DEBUG
>>> steven = lambda x: x
>>> stewart = even(steven)
>>> stewart
>>> stewart(61)
>>> stewart(-4)
```


## Q4: Lambdas and Currying (2022summer lab02 的q4对应2022 fall lab02 q3)


思路：
【利用lambda 多级参数传入的特性实现二元函数的柯里化】
最初实现 [ED](https://pythontutor.com/cp/composingprograms.html#mode=edit)
``` python
from operator import add, mul, mod

def lambda_curry2(func):

    return lambda x: lambda y: lambda: func(x)(y)
    

curried_add = lambda_curry2(add)
add_three = curried_add(3)
add_three(5)
print('DEBUG: result is ' ,add_three(5))
```
得到输出结果为function ，

参考标准答案直接在lambda function 第二级进行多元函数的处理func(x,y)
标准答案形式  
``` python
def lambda_curry2(func):
    return lambda arg1: lambda arg2: func(arg1, arg2)
```

2022/10/3思路衔接:关于两种处理的不同 以及两级和三级处理的不同

关于最终返回函数的柯里化处理问题：(对比下面两行代码)
``` python
return lambda arg1: lambda arg2: func(arg1, arg2)
return lambda x: lambda y: lambda: func(x)(y)
```

根据[环境图]()理解， 联系关于lambda function 的相关expression
在同级调用中 lambda y:func(x,y) 相当于定义一个以y作为formal parameter,return func f(x,y)的函数，关于f(x,y)函数的定义及其相关调用可见 
`1.6.6 Currying def curry2(f)`,由于Python 语言本身特性而实现函数的柯里化


关于二级调用和三级调用的问题：(对比下面两行代码)
``` python
return lambda x: lambda y: func(x)(y)
return lambda x: lambda y: lambda :func(x,y)
```
根据[环境图]()理解， 联系关于lambda function 的相关expression
第三级内没有formal parameter 的传入接口 return func f() 没有传出

关于lamdbda func 对应expression 的同级参数传入及return 对比分析:
``` python
>>> add_three(5)
<function lambda_curry2.<locals>.<lambda>.<locals>.<lambda>.<locals>.<lambda> at 0x000002C1DB052670>
>>> add_three
<function lambda_curry2.<locals>.<lambda>.<locals>.<lambda> at 0x000002C1DB0E0B80>
>>> add_three(5)()
8
>>> add_three(3)()
6

>>> z = 3
>>> e = lambda x: lambda y: lambda: x + y + z
>>> e(0)(1)()
4
```
通过设置第三级lambda func 的调用`()` 得到了原先二级调用的结果

Summary:关于lambda function 及其expression 的调用，对于多级而言有递进式的调用，对于同级调用直接的严格一一对应关系


## Q4: Count van Count

[2022-fall-CS61A-homepage](https://cs61a.org/)
[textbook](http://composingprograms.com/pages/16-higher-order-functions.html)
[pyhtontutor](https://pythontutor.com/cp/composingprograms.html#mode=edit)
[2022-fall-CS61A-lab02-solution](https://cs61a.org/lab/sol-lab02/#q3-lambdas-and-currying)
[2022-fall-CS61A-lab02](https://cs61a.org/lab/lab02/#q4-count-van-count)


## Q6: Composite Identity Function

- 利用lambda 表达式返回一个需要接受参数x的组合函数f(g(x))

## 习题 case 对应的environment diagrams:
[平台](https://pythontutor.com/composingprograms.html#mode=display)
EX: Q1  2n+1输出 
``` python
#Q1
n = 7

def f(x):
    n = 8
    return x + 1

def g(x):
    print('DEBUG:x is ',x)
    n = 9
    def h():
        print('DEBUG:x is ',x)
        return x + 1
    return h

def f(f, x):
    print('DEBUG:x is ',x)
    return f(x + n)

f = f(g, n)

g = (lambda y: y())(f) #f 指向  func h() [parent = f2]  调用返回 return x+1

# 2n+1  >>  return f(x+n)  f 指向 func g(x) [parent=Global]
```

EX: Lambda return other lambdas
``` python
b = lambda x: lambda: x  # Lambdas can return other lambdas!
c = b(88)
c()
```

EX: None 在 python interpreter 的 display
``` python
x = None # remember to review the rules of WWPD given above!
x
lambda x: x # lambda function display
```

EX:变量传递范围 对应的frame （
``` python
#
# Pay attention to the scope of variables
z = 3
e = lambda x: lambda y: lambda: x + y + z
e(0)(1)()
```

对比分析：
EX: Lambda return other lambdas ，Lambda function 的多级调用
EX: lambda 多层函数调用 及对应参数传入

S:
关于lambda 多级函数及对应参数的传入 及函数的return 
关于lambda 调用 对None Error 在display 方面的先验性错误


EX: 函数内定义子函数情况下的直接多级调用  
[环境图理解](https://pythontutor.com/composingprograms.html#mode=display)

``` python
def cake():
    print('beets')
    def pie():
        print('sweets')
        return 'cake'
    return pie

cake()() 
```
注：对pie的调用对应的 parent frame = f1

## Summery

2022.9.27
- 1h30min 关于lab02 q1 q2的学习:有关lambda函数的多级调用(结合environment diagram 纠正了之前在同级frame下定义的误解) 有关lambda函数 调用时的 在python中的display(function nothing etc……)

2022.9.29
- 50min+ 关于lab02 q3的debug 正在准备关于q4的一些代码的调用(currying 和 lambda function 的结合调用学习)  
关于电子学习笔记的优势:对以往学习笔记归档的快速调用与对比学习


2022/10/3
- 30min+ 关于课程档案的选择:2022 fall 的跟进
