#Q1
"""
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

"""

#Q2
"""
d = lambda f: f(4)  # They can have functions as arguments as well
def square(x):
    return x * x
d(square)
"""

#Q3: WWPD: Higher Order Functions
def cake():
    print('beets')
    def pie():
        print('sweets')
        return 'cake'
    return pie





chocolate = cake() # return 和 print func  display 的不同
"""
>>> chocolate

Function
(<function cake.<locals>.pie at 0x0000013294300790>) 多级调用

>>> chocolate()

sweets
'cake'  #对func pie 直接调用
"""
more_chocolate, more_cake = chocolate(), cake

"""
>>> more_chocolate

'cake'
"""
## cake  more_cake 的 对比(一个函数一个 字符 没啥好对比的 可能在教室太紧张了

def snake(x, y):
    if cake == more_cake:
        return chocolate
    else:
        return x + y

    """
>>> snake(10, 20)

Function
（<function cake.<locals>.pie at 0x0000020C9D060790>）

>>> snake(10, 20)()  相当于对func cake 的调用等价于 chocolate()

sweets
'cake'
    """

    """
cake = 'cake'
snake(10, 20)
    """
