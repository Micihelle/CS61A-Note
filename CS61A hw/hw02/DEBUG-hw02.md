> ## Content-Question  

**根据assignment 具体问题分类，每一问题具体实现过程(主要整理耗时较长、难度较大的)**

### Q2:

参考solution 之前 关于递归逻辑的实现代码:(参考对应教材内容后发现未明确规定base-case)

``` python
    while(n>0):
        print('DEBUG: 初始值 merger(start,term(n)) is ', merger(0,term(n)))
        sum = merger(merger(start,term(n)),term(n-1) #嵌套逻辑抽象Q1的连乘逻辑
        merger(sum,term(n-1))
    return sum
```

关于嵌套逻辑的完全调用实现？>参考solution, solution 实现思路为传统迭代逻辑

``` python
def accumulate(merger, start, n, term):
    total, k = start, 1
    while k <= n:
        total, k = merger(total, term(k)), k + 1
    return total
```


``` python
def accumulate(merger, start, n, term):
    sum=1
    if n==1:
        return sum
    else:
        return merger(merger(start,term(n)),term(n-1))
```

> ## Idea-Question

**根据assignment 具体问题分类，每一问题具体实现过程中的疑惑、对比分析(相当于对实现过程的初步概括)**

待进一步学习整理(未完成，且无相关反馈资源参考，但是有学习价值的事情):
Q2: 


> ## Summary-对应问题的技术内容总结  

**基于assignment 具体实现需求整理对应内容，包括Python 语言基本特性的技术内容、课程textbook对应概念内容的整理、其他拓展信息学习内容的整理**  
<!-- 对学习课程需求的反馈:程序构造解释(SICP)中对数据处理、操作组合等等过程的抽象、计算机程序的一些抽象概念的理解、面向对象等程序设计思想 -->

Q1 & Q2
抽象过程理解:Q1 基础上利用 arg(merger) 进行交互逻辑过程的抽象

关于 textbook 的 1.7 Recursive Function 内容的整理:
(直接根据EX 进行抽象技术概括)

1. base case的基本定义 
2. 对自身不断调用的结果返回(从最后一项开始构造问题)

(主要应用场景为Q2中 递归逻辑的实现思路，对比EX：`func sum_digits`):

此时的Q2 递归逻辑实现思路

``` python
def accumulate(merger, start, n, term):
    if n < 1:
        return sum
    else:
        sum = merger(start,term(n))
        n = n-1
        return accumulate(merger, sum,n, term(n))
```

(直接针对 assignment 应用场景进行 对应技术内容学习实践的整理 更便于实现"更好的调用归档"的初衷)

结合环境图理解 主要问题为 merger func 的计算值没有成功return 从而进行sum 进一步递归 由于merger func 的frame 为[global], 关于sum的值无法 传入？

改名成 start 确保值的传入(这里才真正符合textbook 的EX逻辑)

结果还是有 TypeError 的错误 检验发现为 term(n) 替代了 term 的传入
(1h -重点总结：通过对比EX案例的递归逻辑改进出了自己 的 关于Q2 的实现，真正实现了内容资源的调用)




**其他拓展信息学习内容的整理**(待完成)
- 递归逻辑实现的数据结构与算法学习


**该项assginment 完成的时间表及思路衔接**

2022/10/10思路衔接：
2h-关于HW02 Q1的DEBUG 基于Q1进行抽象逻辑的技术改进(Q2 accumulate function)

【衔接assignment】基于迭代逻辑的个人代码修改 (可参考1.7 关于recursion的md 或进一步整理后续内容)s

2022/10/12
(1h -重点总结：通过对比EX案例的递归逻辑改进出了自己 的 关于Q2 的实现，真正实现了内容资源的调用)
【衔接assignment】Q2后续部分的实现

数值计算正确 除了test func case不通过 可能跟测试评分系统代码有关 直接进行Extra pratcie

Extra pratice 都是一些exam 直接进入lab02