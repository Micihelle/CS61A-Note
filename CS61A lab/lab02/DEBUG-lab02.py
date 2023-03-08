#Q3
from operator import add, mul, mod
from lab02 import *

curried_add = lambda_curry2(add)
add_three = curried_add(3)
add_three(5)
print('DEBUG: result is ' ,add_three(5))

curried_mul = lambda_curry2(mul)
mul_5 = curried_mul(5)
mul_5(42)

lambda_curry2(mod)(123)(10)


"""
return 一个 柯里化的二元函数
"""

#Q4: Count van Count
def count_factors(n):
    """Return the number of positive factors that n has.
    >>> count_factors(6)
    4   # 1, 2, 3, 6
    >>> count_factors(4)
    3   # 1, 2, 4
    """
    i = 1
    count = 0
    while i <= n:
        if n % i == 0:
            count += 1
        i += 1
    return count

print('DEBUG: count_factors(6) is ',count_factors(6))
print('DEBUG: count_factors(4) is ',count_factors(4))


def is_prime(n):
    return count_factors(n) == 2 # only factors are 1 and n

"判断是否为质数的标准：根据质数的定义，只要因数总和为2（即只能被1和n(自己)整除）则可判断其为质数"

def count_primes(n):
    """Return the number of prime numbers up to and including n.
    >>> count_primes(6)
    3   # 2, 3, 5
    >>> count_primes(13)
    6   # 2, 3, 5, 7, 11, 13
    """
    i = 1
    count = 0
    while i <= n:
        if is_prime(i):
            count += 1
        i += 1
    return count

print('DEBUG: count_primes(6) is ',count_primes(6))
print('DEBUG: count_primes(13) is ',count_primes(13))

