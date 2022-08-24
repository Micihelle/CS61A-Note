# Lab 1: Variables & Functions, Control

## Debugging
[教材链接](https://inst.eecs.berkeley.edu/~cs61a/su20/articles/debugging.html)
### Introduction
``` python
Traceback (most recent call last):
  File "<pyshell#29>", line 3 in <module>
    result = buggy(5)
  File <pyshell#29>", line 5 in buggy
    return f + x
TypeError: unsupported operand type(s) for +: 'function' and 'int'
```

### Traceback message：

``` python
File "<file name>", line <number>, in <function>
```

### Error Messages：


``` python
<error type>: <error message>
```
- #### Error type:
  e.g.`SyntaxError`(语法错误）、`TyeError`(类型错误)
- #### Error message 

## Debugging Techniques

### Running doctests

### Writing your own tests
(1) write additional doctests
- `take_turn_test` function from Project 1
(2) write testing functions.

### Using `print` statements
``` python
def foo(x):
    result = some_function(x)
    print('DEBUG: result is', result)
    return other_function(result)
```

#### Long-term debugging (代码的长期调试)

``` python
debug = True

def foo(n):
i = 0
while i < n:
    i += func(i)
    if debug:
        print('DEBUG: i is', i)
```

#### Interactive Debugging
#### PythonTutor Debugging

```
python ok -q <question name> --trace

```

#### Using `assert` statements

``` python 
def double(x):
    assert isinstance(x, int), "The input to double(x) must be an integer"
    return 2 * x
```

``` python
def g(x, y):
    return double(x) + y # should be double(y) + len(x)
```

``` python
>>> double (2)
4
>>> double(3.2)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    double(3.2)
  File "<pyshell#7>", line 2, in double
    assert isinstance(x, int), "The input to double(x) must be an integer"
AssertionError: The input to double(x) must be an integer
```


``` python
def double2(x):
    return 2 * x
    
double2(2)
4
double2(3.2)
6.4
```

### Error Types

#### SyntaxError(语法问题)

Notes: Python will check for SyntaxErrors before executing any code. This is different from other errors, which are only raised during runtime
(python会先检查Syntaxerros)

#### IndentationError(缩进问题)
EX:
``` python
  File "file name", line number
    print('improper indentation')
IndentationError: unindent does not match any outer indentation level

```

#### TypeError(类型问题)


>## Idea

``` python
>>> 1 and 3 and 6 and 10 and 15

>>> 15
```