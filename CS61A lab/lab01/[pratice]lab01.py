def how_big(x):
     if x > 10:
         print('huge')
     elif x > 5:
         return 'big'
     elif x > 0:
         print('small')
     else:
         print("nothin'")

"""
字符串字面量
python 中的字符串字面量由单引号或双引号括起
'hello 等同于 "hello"
"""
n=3
while n >= 0:  # If this loops forever, just type Infinite Loop
    n -= 1
    print(n)

positive=28
#positive=27
while positive: # If this loops forever, just type Infinite Loop
    print("positive?")
    positive -=3

# while <boolean value> 如果为真值则一直执行 如果为false value 如None False 0等则直接不执行


True and 1 / 0 and False

"""
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    True and 1 / 0 and False
ZeroDivisionError: division by zero
"""
#哪个能判定总的expression的结果 执行哪个小expression
#and逻辑运算符左侧为True 故直接执行右侧 expression:1/0

True or 1 / 0 or False
#or 逻辑运算符左侧为True 直接输出Boolean value为True ；右侧expression 直接short-circuiting






