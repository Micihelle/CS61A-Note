## Summary:
study python program:
- Q7: Coordinates (Python 函数计算>查找限定值域内的自变量离散点)
- Q8：关于list 的错位操作 (List comprehensions中的逻辑判断挑选结构)

## Blog
Lists(data struture)

search as a element:
[1,2] in [3, [1,2], 4]
### Q1：Squared Virahanka Fibonacci
tree resursion 分支更改
(偶数号序列有0的输出)(branch 遍历)
``` Python
>>> r4 = virfib_sq(4)
(line 1)? 4
(line 2)? 3
(line 3)? 2
(line 4)? 1
(line 5)? 0
(line 6)? 1
(line 7)? 2
(line 8)? 1
(line 9)? 0
-- OK! --

>>> r4
? 25
```

(2023/3/2):summation environment diagram analysis(lab04)
- [x] 出现了AssertionError的问题 （assert return)
``` Python
def summation(n, term):
    """Return the sum of numbers 1 through n (including n) wíth term applied to each number.
    Implement using recursion!

    >>> summation(5, lambda x: x * x * x) # 1^3 + 2^3 + 3^3 + 4^3 + 5^3
    225
    >>> summation(9, lambda x: x + 1) # 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    54
    >>> summation(5, lambda x: 2**x) # 2^1 + 2^2 + 2^3 + 2^4 + 2^5
    62
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'summation',
    ...       ['While', 'For'])
    True
    """
    assert n >= 1
    "*** YOUR CODE HERE ***"
    return (term(n)+summation(n-1,term))
```


### Q5:

相关内容 List Comprehensions
EX: Sequence Iteration
```Python 
for <name> in <expression>
	<suite>
```

``` Python
pairs =[[1,2],[3,4],[1,1],[5,5]]
same_count = 0

for x,y in pairs:
	if x==y:
		same_count=same_count + 1

same_count 
```

EX： Range（finite length):including this starting value but excluding the ending value

Length: ending value - starting value
Element selection: starting value + index

the element never use
``` Python
def cheer():
	for _ in range(3):
		print("GO BEARS!")
```

EX: List comprehensions（对列表个元素进行逻辑判断)
- 逻辑判断环节
- 分支返回值的处理
``` Python
odds = [1,3,5,7,9]

[x + 1 for ]
```


### Q7: Coordinates (Python 函数计算>查找限定值域内的自变量离散点)


Reflect: in terms of using computer resources?: the govern of resources and code


### Q8：
关于list 的错位操作