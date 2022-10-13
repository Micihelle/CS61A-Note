from operator import add, mul

square = lambda x: x * x

identity = lambda x: x

triple = lambda x: 3 * x

increment = lambda x: x + 1


HW_SOURCE_FILE = __file__


def product(n, term):
    """Return the product of the first n terms in a sequence.

    n: a positive integer
    term:  a function that takes one argument to produce the term

    >>> product(3, identity)  # 1 * 2 * 3
    6
    >>> product(5, identity)  # 1 * 2 * 3 * 4 * 5
    120
    >>> product(3, square)    # 1^2 * 2^2 * 3^2
    36
    >>> product(5, square)    # 1^2 * 2^2 * 3^2 * 4^2 * 5^2
    14400
    >>> product(3, increment) # (1+1) * (2+1) * (3+1)
    24
    >>> product(3, triple)    # 1*3 * 2*3 * 3*3
    162
    """
    """
    1. term = identity 阶乘
    2. term = square   阶乘每一元素的平方连乘
    3. term = increment 阶乘每一元素 各+1 再连乘
    4. term = triple 阶乘每一元素乘以3 再连乘

    阶乘基本元素
        """
    "*** YOUR CODE HERE ***"
    sum = 1
    while(n>0):
        sum*=term(n)
        n=n-1
    return sum


def accumulate(merger, start, n, term):
    """Return the result of merging the first n terms in a sequence and start.
    The terms to be merged are term(1), term(2), ..., term(n). merger is a
    two-argument commutative function.

    在Q1 product 的基础上进一步抽象,Q1基础 merge逻辑为阶乘元素的连乘
    1.term = identity  初始值start merge 阶乘元素相加 term(n)=n
    2.term = square    初始值stat merge 阶乘元素平方和 term(n)=n*n

    初始值start 为 merge function 的第一参数 随后用嵌套逻辑进行调用(连加 或 连乘)
    merge 传递函数代表 start 和 term(1), term(2), ..., term(n) 之间的关系


    >>> accumulate(add, 0, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> accumulate(add, 11, 5, identity) # 11 + 1 + 2 + 3 + 4 + 5
    26
    >>> accumulate(add, 11, 0, identity) # 11
    11
    >>> accumulate(add, 11, 3, square)   # 11 + 1^2 + 2^2 + 3^2
    25
    >>> accumulate(mul, 2, 3, square)    # 2 * 1^2 * 2^2 * 3^2
    72
    >>> # 2 + (1^2 + 1) + (2^2 + 1) + (3^2 + 1)  2 2 5 10
    >>> accumulate(lambda x, y: x + y + 1, 2, 3, square)
    19
    >>> # ((2 * 1^2 * 2) * 2^2 * 2) * 3^2 * 2    嵌套逻辑调用
    >>> accumulate(lambda x, y: 2 * x * y, 2, 3, square)
    576
    >>> accumulate(lambda x, y: (x + y) % 17, 19, 20, square)
    16
    """
    "*** YOUR CODE HERE ***"
    if n < 1:
        return start
    else:
        print('DEBUG: n, is ',n)
        print('DEBUG: merger(start, term(n)) is ',merger(start, term(n)))
        start = merger(start, term(n))

        print('DEBUG: start, is ',start)
        print('DEBUG: term(n), is ',term(n))
        print('DEBUG: merger, is ',merger)
        print('DEBUG: sum is ',start)
        n = n - 1
        return accumulate(merger, start,n, term)

print('DEBUG: product(5, identity) is ',product(5, identity))
print('DEBUG: accumulate(add, 0, 5, identity) is ',accumulate(add, 0, 5, identity))

def summation_using_accumulate(n, term):
    """Returns the sum: term(0) + ... + term(n), using accumulate.

    >>> summation_using_accumulate(5, square)
    55
    >>> summation_using_accumulate(5, triple)
    45
    >>> # You aren't expected to understand the code of this test.
    >>> # Check that the bodies of the functions are just return statements.
    >>> # If this errors, make sure you have removed the "***YOUR CODE HERE***".
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(summation_using_accumulate)).body[0].body]
    ['Expr', 'Return']
    """
    "*** YOUR CODE HERE ***"

    return accumulate


def product_using_accumulate(n, term):
    """Returns the product: term(1) * ... * term(n), using accumulate.

    >>> product_using_accumulate(4, square)
    576
    >>> product_using_accumulate(6, triple)
    524880
    >>> # You aren't expected to understand the code of this test.
    >>> # Check that the bodies of the functions are just return statements.
    >>> # If this errors, make sure you have removed the "***YOUR CODE HERE***".
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(product_using_accumulate)).body[0].body]
    ['Expr', 'Return']
    """
    "*** YOUR CODE HERE ***"
