## 课堂讲义
### Order of Recursion Calls

EX:Cascade

``` Python
def cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n//10)
        print(n)

cascade(123)

```

``` output
123
12
1
12
123
```

how to back up?
None return statement

首先递归溯源到最基本情况，然后又逐层返回到 未完成的`func cascade`初始调用


Cascade 另一种 demo：
``` Python
def cascade(n):
    print(n)
    if n >= 10:
        cascade(n//10)
        print(n)
```


EX:Inverse Cascade

```
1
12
123
1234
123
12
1
```

代码思路参考
``` python
def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f,g,n):

grow = lambda n: f_then_g(grow,print,n//10)

```



``` python
def num_eights(pos):
    c = 0
    if pos%10 == 8:
        c = c + 1
    elif pos > 10 :
        num_eights(pos//10)
    return c
```

### Tree Recursion

函数多次调用 
比如 Fibonacci sequence: `return fib(n-2)+fib(n-1)`
比如 partitions相关的算法


从 environment diagram 的角度  有树形结构的计算过程
(基本情况的还原，为了计算fib(3)要先计算fib(1)、fib(2) )



EX: Counting Partitions  
count_ partitions(6,4) 
最大子数为 m，返回可组成母数的序列总数
基本情况还原(possibilities):  ~  `古典概率论模型主题联系`
- 使用子数最大为4
- 子数不使用4



```python

def count_partitions(n,m):
# 基本情况设计
	if n == 0:
		return 1
	elif n < 0:
		return 0
	elif m == 0:
		return 0	
# 树干部分迭代设计
	else:
		with_m = count_partitions(n-m,m)    
		without_m = count_partitions(n,m-1)
		return with_m + without_m
result = count_partitions(5,3)

// m==0 即无法再进一步细分
// n==0 可被当前子数 m partition
```

**迭代层级 `return` 中长度标志问题 ：还原到最基本情况以后根据  `return` statement 逐层累加**


## hw03 实现

### 关于q1
个人实现
```python
def num_eights(pos):
    if pos == 8:
        print("DEBUG: pos_1 is",pos)
        return 1
    elif (pos%10 ==8) & (pos > 10):
        print("DEBUG: pos_2 is",pos)
        return 1 + num_eights(pos//10)
    elif pos > 10:
        return num_eights(pos//10)
    else:
        return 0
```

思路
```
#迭代算法中的长度标志
#对于尾数为0的情况处理——迭代持续进行到最基本情况
#对于迭代算法可还原至基本情况以外的情形处理
#注意operator coding对原有逻辑架构的影响

#对照答案以后更优化地方
#将不累加情况和不可还原成基本情况这两类情况都进行统一处理
#由此可得基本迭代模型: 
else:
	return func(func(n))
```



### q2

func `num_eights` 运用


- 转向数列描述？> 转向判断
- 转向间隔长度处理

参考答案前的思路
- 方向标志位如同开关电源一样迅速转换，在迭代或递归过程中该如何记录
- 转向间隔长度(step)计算，从而确定return stament

参考答案后的思路整理
- solution1：构造helper函数：突破global 函数框架、设定更多的参数来利用程序推演出预定的数理逻辑（太牛逼了 大道至简 solution2 和1结构类似)
- solotion3：？`ping_pong.py` DEBUG

## idea & blog
2023/2/6 数据结构学习情况

CS61A page[page](https://inst.eecs.berkeley.edu/~cs61a/fa22/)
CS61A lecture:[1](https://www.youtube.com/watch?v=ls0GsJyLVLw&list=PL6BsET-8jgYWFbuoglCtjq_8Awe96k1u7&index=4) 关于Tree recursion 
CS61A coding:[hw03-q1](https://inst.eecs.berkeley.edu/~cs61a/fa22/hw/hw03/)

数据结构算法 RAM实例处理

书籍拓展：
The DESIGN AND ANALYSIS OF COMPUTER ALGORITHMS P15：关于RAM模型的详细解释
Introduction_to_algorithm: 
	1.前面看书习题 
	2.第二章末尾后学习

论坛联系：
[王道](http://www.cskaoyan.com/member.php?mod=logging&action=login)

2023/2/8:
(1h40min+)完成了
- CS61A 的hw03-q1
- CS61A Recursion lecture 的学习

2023/2/9:
数据结构课程-级数
[算法，第一部分 | Coursera](https://www.coursera.org/learn/algorithms-part1)