#Q1
def multiply(m, n):
    """ Takes two positive integers and returns their product using recursion.
    >>> multiply(5, 3)
    15
    """
    "*** YOUR CODE HERE ***"
    if n==1:
        return m
    else:
        return m+multiply(n-1)



#Q3
def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 2:
        return 2
    elif n==1:
        return 1
    else:
        return n * skip_mul(n - 2)




#Q4
def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    def helper(i):
        if i > (n ** 0.5): 
            return True
        elif n % i == 0:
            return False
        return helper(i + 1)
    return helper(2)

#Q5
def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the number of elements in the sequence.
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
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    "*** YOUR CODE HERE ***"
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + hailstone(n // 2)
    else:
        return 1 + hailstone(3 * n + 1)

## 利用迭代算法 return 简化多余的print, 以及简化关于长度的计算,; 而且可以少写一个循环 不然会直接计算到最终结果

#Q6: Merge Numbers(solution太6了)
def merge(n1, n2):
    """ Merges two numbers by digit in decreasing order
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31) 
    3211
    """
    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1
    elif n1 % 10 < n2 % 10:   #从序列末端位数开始对比
        return merge(n1 // 10, n2) * 10 + n1 % 10  #排列最小位数 记录
    else:
        return merge(n1, n2 // 10) * 10 + n2 % 10
    
## 只针对一组十位数的排列组合，三位数即三位数以上需要优化判断语句或者编写数据结构(数组)
    






    
