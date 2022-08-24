# Q4 Falling Factorial
def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    sum=1
    if k==0:
        sum=1
    else:
        for i in range (0,k): #不包括k
            sum=sum*(n-i)
            print('DEBUG: sum is', sum)
    return sum

#Q5: Sum Digits

def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    """
    利用% 得到每一位数
    对每一位数求和
        """
    sum=0
    if y==10:
        sum = 1
    else:
        while y>10:
            z=y%10
            y=y//10
            sum=sum+z
            print('DEBUG: y is', y)
            print('DEBUG: z is', z)
            print('DEBUG: sum is', sum)
        sum=sum+y
    return sum

#python ok -q sum_digits

def bake(cake, make):
    if cake == 0:
        cake = cake + 1
        print(cake)
    if cake == 1:
        print(make)
    else:
        return cake
    return make
#bake(1, "mashed potatoes") return 字符串

#python ok -q if-statements -u

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"""

#位数 连续出现两个8
    if n<=10:
        return False
    while n>10:
        x=n%10
        n=n//10
        if(x==8 & n==8):
            print('DEBUG: x is', x)
            print('DEBUG: n is', n)
            return True
        else:
            continue
    return False

"""
 之前的思路:
 遍历 n 的所有位数中有8的位数
 判断是否存在有相邻的 index 序号
"""

"""
def double_eights(n):
    list=[]
    while n>10:
        x=n%10
        n=n//10
        list.append(x)
        print('DEBUG: list is', list)
        if n<10:
            list.append(n)
            print('DEBUG: list is', list)
        print('DEBUG: list.index(8) is ', list.index(8)) #搜寻第一个为8的元素的位置
"""


#python ok -q double_eights
