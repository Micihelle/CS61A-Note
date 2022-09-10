def curried_pow(x):
        def h(y):
            return pow(x, y)
        return h


#1.6.9   Function Decorators
def trace(fn):
        def wrapped(x):
            print('-> ', fn, '(', x, ')')
            return fn(x)
        return wrapped
@trace   #改变了 def 的 execution rule
def triple(x):
    return 3 * x
"""
the name `triple` is bound to the returned function value of calling `trace`
on the newly defined triple function
"""

"""
triple(12)

->  <function triple at 0x000002726A08F790> ( 12 )
36

"""
