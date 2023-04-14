


主要需求：
整理 cats 的学习材料，如果有比较疑惑的知识点 直接进行相关lab hw的编程训练，并整理对应的系统学习材料
(比较面向实际需求的学习材料的学习方法)






## 材料整理

### Requirement
- measures typing speed
- typing autocorrect

可参考项目：
[typeracer](https://play.typeracer.com/)

文件管理参考：

## Logistics
### Problem 2

``` Python
>>> 'dogs' in 'A paragraph about dogs.'
True
```
`# -u case analysis: logic comparasion (read .md)`

``` Python
>>> from cats import about
>>> from cats import pick
>>> dogs = about(['dogs', 'hounds'])
>>> dogs('A paragraph about cats.')
False

>>> dogs('A paragraph about dogs.')
? True
-- OK! --

>>> dogs('Release the Hounds!')
? True
-- OK! --

>>> dogs('"DOGS" stands for Department Of Geophysical Science.')
? True
-- OK! --

>>> dogs('Do gs and ho unds don\'t count')
? False
-- OK! --

>>> dogs("AdogsParagraph")
False

# return statement: a function that 
# selete logic:

1. whether in topic
2. string operation?(iterable value) string[x:] >>  full sequence abstraction? 字符空格划分？ >> str.split(' ',len(topic))
EX1："dogs" is not a match for the word "dog".
EX2：lowercase problem
4. 
```

- [x] `AttributeError: 'list' object has no attribute 'split's`
(2023/4/1: 字符串划分处理)[AttributeError: ‘list‘ object has no attribute ‘split‘ 报错_no attribute split_MaoNanBei2233的博客-CSDN博客](https://blog.csdn.net/MaoNanBei2233/article/details/110046587)
 


[Project 2: CS 61A Autocorrected Typing Software | CS 61A Fall 2022 (berkeley.edu)](https://inst.eecs.berkeley.edu/~cs61a/fa22/proj/cats/#phase-1-typing) 
#d 关于 topic word 的存在独立性
> Additionally, only check for exact matches of the words in topic in the paragraph, not substrings. For example, "dogs" is not a match for the word "dog".


- DEBUG-CASE `([lower(whether)] != lower(whether).split(x))]` 判定逻辑更改
- DEBUG-CASE 
- [ ] **关于两层遍历逻辑的架构(2023/4/8)** 重点关注这几行
``` Python
    for y in range(len(topic)):
        whether[y] = [x for x in whether if (topic[y] in x)]   # influence of punctuation
```

 
 ~~单 topcic word 成段情况修正
 
 ``` PYTHON
         if split(whether) == [whether]:  # 针对单字符成行情况修正 当且仅当 topic word 恰好单独成行情况 return True
            whether = [x for x in topic if (x==whether)]  # 非空列表 返回 True
        else:
            whether = split(lower(whether))
```

说明: 
- **若判定逻辑设置为对 topic word 进行遍历 `x in topic ` 需要修正puntuation problem 的影响**
	- ~~利用 String 数据结构的可Slicing 特性： `x[0:m] == topic word[0:(topic)] ` ，则无需专门修正单 topcic word 成段情况
	- ~~针对 list topic word 的遍历结构搭建
``` Python
p = [x for x in pword if ((x[0:len(y)] == y) | (x[1:len(y)+1] == y))]
```
- 若判定逻辑设置为对 list(paragraph) 进行遍历   需要搭建多序列遍历逻辑架构

puntuation march problem:
- `'#crystallogenIcalW'` 和 `'crystallogenical'` 不匹配
	- `| (x[1:(len(y)+1)] == y))`
- DEBUG-case: topic word 的独立性 只能和 punctuation 拼接 不能与其他字母拼接
	- **导入 utils 中的 remove_punctuation**
``` Python
>>> dogs = about(['dogs', 'hounds'])
>>> dogs('"DOGS" stands for Department Of Geophysical Science.')
DEBUG: current topic word is  dogs
DEBUG: current topic word is  hounds
True

>>> ab = about(['unsimilar', 'conditioning', 'crystallogenical', 'mennom', 'foreannouncement', 'neomorph'])
>>> ab('#crystallogenIcalW podded reorganizationist neomorPhf hneomorphj')
DEBUG: current topic word is  unsimilar
DEBUG: current topic word is  conditioning
DEBUG: current topic word is  crystallogenical
False

```

在发现 外部库可调用函数之前的逻辑架构
``` Python
    def select(paragraph):
        pword = split(lower(paragraph))   # influence of lowercase
        for y in topic:       # 对 topic word 进行遍历
            if [paragraph] == split(paragraph):  # 针对单字符成行情况修正 当且仅当 topic word 恰好单独成行情况 return True
                p = [x for x in pword if (lower(remove_punctuation(x)) == y)]    # 单字符成行情况 字符拼接的判定逻辑修正 >> 比如 paragraph = '#dogs'?     
            else:        
                print('DEBUG: current topic word is ',y)
                p = [x for x in pword if (lower(remove_punctuation(x)) == y)]   # influence of punctuation  空字符
            if p != []:
                return True
        return False                        # 对 topic word 及 paragraph 搜寻完毕后 
    return select
```

problem2 ss: 调用外部库内的函数辅助操作


problem3-u:

``` Python
>>> accuracy("a b \tc" , "a b c") # Tabs don't count as words
? 100.0
-- OK! --

>>> accuracy("abc", "")
? 0.0
-- OK! --

>>> accuracy("", "abc")
? 0.0
-- OK! --

>>> accuracy("a b c d", "b c d")
? 0.0
-- OK! --

>>> accuracy("cats.", "cats") # punctuation counts
? 0.0
-- OK! --

>>> accuracy("", "") # Returns 100.0
? 100.0
-- OK! --
```

`typed` 长度大于 `source` 情况修正

problem 4:
typing speed 定义：
> instead the number of groups of 5 characters, so that a typing test is not biased by the length of words.


- [x] (2023/3/28: Problem2 
- [x]  子函数调用父函数变量问题: 
	- `global external_variable`
- [ ] return 一元子函数情况下如何存储父函数变量 >> 对helper进行柯里化？>>Blog: lambda expression-Currying相关内容整理
	- [ ] global external_variable environment diagram analysis


### Phase 2 :Autocorrect

problem5 -u
``` PowerShell
>>> from cats import autocorrect, lines_from_file
>>> abs_diff = lambda w1, w2, limit: abs(len(w2) - len(w1))
>>> autocorrect("cul", ["culture", "cult", "cultivate"], abs_diff, 10)
"cult"

>>> autocorrect("cul", ["culture", "cult", "cultivate"], abs_diff, 0)
"cul"

>>> autocorrect("wor", ["worry", "car", "part"], abs_diff, 10)
"car"

>>> first_diff = lambda w1, w2, limit: 1 if w1[0] != w2[0] else 0
>>> autocorrect("wrod", ["word", "rod"], first_diff, 1)
"word"

>>> autocorrect("inside", ["idea", "insider"], first_diff, 0.5)
? "idea"  #取最近 return the string that appears first in `word_list`.
```

~~diff_return 判定 >> 
``` Python
if len([x for x in diff_return if (x == min(diff_return))]) == 1:
	return 
else:
    for j in range(len(diff_return)):
        if diff_return[j] == min(diff_return):
	        return word_list[j]     # min index 提取
```

调用 str.index 进行判定

Q6
[【Python基础】字符串逆序（反转）输出的几种方式实例_字符串逆序输出python_Du(o_o)的博客-CSDN博客](https://blog.csdn.net/dyfDewey/article/details/107000800?ydreferer=aHR0cHM6Ly9jbi5iaW5nLmNvbS8%3D) 


list_recursion 相关materials
- lab05: flatten function
	- base case: []

利用Python 实现一个递归算法要求如下：如果递归次数超出某一个值及时退出并返回目前总共递归次数
- ~~每次递归 前 limit 个字符？
- 递归过程中所传递参数的变化 >> limit 

考虑分支转向结构为 常数时间复杂度：
``` Python
if ((len(typed) > limit) & (limit > 0)):   
    return feline_fixes(typed[:limit],source[:limit],limit) + feline_fixes(typed[limit:len(typed)],source[limit:len(source)],limit) 
```

`# Check that the recursion stops when the limit is reached`

(2023/4/11)
目前问题: 不同递归分支导向判断设计 >> 目前无论在相同位置上是否存在不同字符 都会导向相同的递归情况。。
``` Python
return feline_fixes(source[1:],typed[1:],limit)
return 1 + feline_fixes(source[1:],typed[1:],limit)
```
参考 CSDIY的实现 注意递归过程中 limit 参数的变化 从而实现及时退出递归过程
此时已经通过了 所有test
``` Python
    if (limit < 0):    #  超出 limit 时候 及时退出 recursion
        return 0
    elif ((source == '') | (typed == '')):
        return abs(len(source)-len(typed))
    else:
        if source[0] == typed[0]:     
            print("DEBUG: current character is ",source[0])
            return feline_fixes(source[1:],typed[1:],limit)
        else:
            print("DEBUG: current character is ",source[0])
            return 1 + feline_fixes(source[1:],typed[1:],limit-1)
```

对比csdiy 的参考方案，可优化点？：具体实现目标不同不好做比较 

Optional problem: (优化 autocorrect 模块)
测试 autocorrect 模块
```
python3 score.py
```
直接利用 `minimum_mewtations` 的 测试情况
```
Correction Speed: 269.02211527916074 wpm
Correctly Corrected: 142 words
Incorrectly Corrected: 38 words
Uncorrected: 22 words
```

problem9:
match function 中对 dictionary containing 的处理
在此基础上实现 `time_per_word`
[Project 2: CS 61A Autocorrected Typing Software | CS 61A Fall 2022 (berkeley.edu)](https://inst.eecs.berkeley.edu/~cs61a/fa22/proj/cats/#problem-9-2-pts)


DEBUG-CASE:
未考虑对多玩家打字速度计算功能的实现(只考虑到两人情况)
``` Python
player0_t = [times_per_player[0][x+1] - times_per_player[0][x] for x in range(len(times_per_player[0])) if (x+1 < len(times_per_player[0]))]
player1_t = [times_per_player[1][x+1] - times_per_player[1][x] for x in range(len(times_per_player[1])) if (x+1 < len(times_per_player[1]))]
times = [player0_t,player1_t]
return match(words,times)
```
根据 multiplayer 数 进行遍历（支持两个以上的玩家)
- list of lists 实现



problem10:
DEBUG-CASE: 同个单词相同速度只进行一次的添加操作
修改前
``` Python
    min_words = [min([get_all_times(match)[y][x] for y in player_indices]) for x in word_indices]
    return [[get_all_words(match)[x] for x in word_indices if (get_all_times(match)[y][x] == min_words[x])] for y in player_indices]

```
修改后()


> ## Idea

> ## Summary

具体实现过程中的各种运用
- 各种遍历搜寻与字符串操作
- 递归过程中对字符的添加、删除、更改 以及通过传入参数的操作来限制递归次数 (problem 7 & problem 8 )
- list of lists 多级遍历结构搭建 (problem9 & problem10)
- 利用穷举法来搜寻最小值 (problem10)
	- Python min函数的key 用法：[python min函数的key用法_python中key的用法_运维饺子的博客-CSDN博客](https://blog.csdn.net/qq_37369726/article/details/122324645) 
``` Python 
min(list,key=func) #第一个参数是需要比较的数据，key后面传入函数名

#func 内容补充
def func(x): # x 为min传入的参数list
	return x[1] # 返回给min结果，让min 以这些数值排序


# 若用 lambda 表达式简写
list = [('lg',24),('wx',23),('aa',34)]
result = min(list,key=lambda x : x[1])
print(result)
>>> ('wx', 23)
```
- min函数 key 用法 在 Problem 10 中的运用 (传入一个 list 返回的是最小值对应的索引)
``` Python
word_times = [times[player][i] for player in player_indices]  # 对 各个玩家的当前 word 的 typing speed 进行遍历
idx = min(player_indices, key=lambda x: word_times[x]) 
#1.the fastest (against all the other players 
#2. lambda 表达式返回值为 玩家x 在当前 word 的 typing time 
#3.最终返回值为对应的 list值(此处为索引)
```
- min 函数本身特性运用
	- min函数本身特性 With two or more arguments, return the smallest argument.
	- 使得每个 word 只会被进行一次添加操作

参考:  [Getting the index of the returned max or min item using max()/min() on a list](https://stackoverflow.com/questions/2474015/getting-the-index-of-the-returned-max-or-min-item-using-max-min-on-a-list)


相关笔记补充
#### Python String
1. Membership: does not conform to the full sequence abstraction
2. Slicing operation:
	- Slicing operation: `.split()`
	- 利用 topic word 作为划分工具
3. 单引号' 和双引号“ 使用区别：利用单引号表示一串字符时，里面出现的双引号表示空字符