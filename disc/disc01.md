> ## Content
•A conditional expression is an expression that evaluates to either atruthy value (True, a non-zero integer, etc.) or a falsy value (False, 0, None, "", [], etc.).

`and` evaluates expressions in order and stops evaluating (short-circuits)once it reaches the first falsy value, and then returns it. If all valuesevaluate to a truthy value, the last value is returned.


### While loops
``` python
while <conditional clause>:
    <statements body>
```
As long as `<conditional clause>` evaluates to a true value, `<statements body>` will continue to be executed. The conditional clause gets evaluated each time the body finishes executing.

> ## Idea 
8.31思路衔接 关于disc方面的知识输入 可以后续归类到课程笔记的md中 或者归类到dis对应的py文件中
不然可能笔记比较零散不好后续调用 复习