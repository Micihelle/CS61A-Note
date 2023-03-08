(Q1-Q3前面整理的内容有点冗长而且没有按框架整理，Q4单独分页)


## Q4实现

最初实现思路：

接受一个判断条件condition, 从 condition 提取 two-argument


最终结果：
借鉴该题目的前置技术知识基础 进行抽象概括
Q4 侧重于对判断条件的逻辑封装 进行抽象技术的封装，从具体的前置函数定义 到后面函数逻辑的封装。



## **Environment Diagram Practice**
## Q5: HOF Diagram Practice

(独立完成，等后续一并参考SOLUTION)
## Q6: Composite Identity Function

(独立完成，等后续一并参考SOLUTION)

## Q7: I Heard You Liked Functions...

如何优化算法 使得每次循环不用每次都判断所有条件
Hint: 固定顺序的嵌套函数调用 如何和遍历联系起来?


具体如何实现 final_function 的嵌套调用 并且在最后user-defined function 内进行参数的传入


参考solution 的 Q7实现之前的具体代码:(应该是不太了解python的技术内容特性)
``` python
    def cycle_func(n):
        cycle_int = n
        count = 0
        final_func = lambda x: x
        while (n>1):
            if count == 0:
                if n% 3 == 1:
                    final_func = f1
                elif n% 3 == 2:
                    final_func = f2
                elif n% 3 == 0:
                    final_func = f3
            else:
                if n% 3 == 1:
                    final_func = f1(final_func)
                elif n% 3 == 2:
                    final_func = f2(final_func)
                elif n% 3 == 0:
                    final_func = f3(final_func)
            n -=1
            count+=1
        def cycle_int(x):
            return final_func(x)
    return cycle_func
```

参考solution, 可能没有简化判断条件的逻辑 但是简化了代码量(固定嵌套函数调用顺序)(这里应该用的是 多级参数的调用 可以联系lambda function 中进行直观理解，通过return 多级参数的传入来实现嵌套函数的调用)

``` python
def cycle(f1, f2, f3):
    def ret_fn(n):
        def ret(x):
            if n == 0:
                return x
            return cycle(f2, f3, f1)(n - 1)(f1(x))
        return ret
    return ret_fn

def cycle(f1, f2, f3):
    def ret_fn(n):
        def ret(x):
            i = 0
            while i < n:
                if i % 3 == 0:
                    x = f1(x)
                elif i % 3 == 1:
                    x = f2(x)
                else:
                    x = f3(x)
                i += 1
            return x
        return ret
    return ret_fn
    

def add1(x):
    return x + 1

def times2(x):
    return x * 2

def add3(x):
    return x + 3
    
```

然后参考 solution的具体实现过程思路:
对比自己的嵌套逻辑 和 solution的嵌套逻辑


关于自己代码的DEBUG: 
1.直接进行了 lambda x:x的嵌套调用 
solution 对应的逻辑: 直接进行 x的return(作为 final function) 然后进行参数的传递的时候可以直接调用 final function 
改进方式: return x 自身函数
``` python
    def cycle_func(n):
        cycle_int = n
        count = 0
        final_func = lambda x: x
        while (n>1):
            if count == 0:
                if n% 3 == 1:
                    final_func = f1
                elif n% 3 == 2:
                    final_func = f2
                elif n% 3 == 0:
                    final_func = f3
            else:
                if n% 3 == 1:
                    final_func = f1(final_func)
                elif n% 3 == 2:
                    final_func = f2(final_func)
                elif n% 3 == 0:
                    final_func = f3(final_func)
            n -=1
            count+=1
        def cycle_int(x):
            final_func

            return final_func
    return cycle_func
```


## [调用环境图理解]
具体case 分析:
对于n=0;
``` python
my_cycle = cycle(add1, times2, add3)
identity = my_cycle(0)
identity(5)

    5
```

对于n=2;
``` python
my_cycle = cycle(add1, times2, add3)
add_one_then_double = my_cycle(2)
add_one_then_double(1)

    4
```

对于n=3；
``` python
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
```

对应n=4;
``` python
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
```

对应n=6;
``` python
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
```




> ## Summary-对应问题的技术内容总结  

**基于assignment 具体实现需求整理对应内容，包括Python 语言基本特性的技术内容、课程textbook对应概念内容的整理、其他拓展信息学习内容的整理**  
<!-- 对学习课程需求的反馈:程序构造解释(SICP)中对数据处理、操作组合等等过程的抽象、计算机程序的一些抽象概念的理解、面向对象等程序设计思想 -->


**Python 语言基本特性的技术内容**


**课程textbook对应概念内容的整理**


**其他拓展信息学习内容的整理**(待进一步学习实践、反馈交流参考)


**该项assginment 完成的时间表及思路衔接**

2022/10/13: 2h30min+
关于hw02 lab02 的全部问题的自己思路实现，除了lab02 Q7其他全部实现通过

思路衔接： 从lab02 Q7问题开始 进行个人代码的DEBUG 和改进
分析思路: 
1. solution实现的代码逻辑
2. 个人在参考solution 之前的报错问题处理
3. 基于个人代码报错问题处理改正 参考solution代码逻辑进行进一步修正

