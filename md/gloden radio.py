def improve(update, close, guess=1):
    while not close(guess):  #此处在close即square_close_to_successor 中绑定了 guess=1 的default value
        guess = update(guess) 
    return guess

def golden_update(guess):
    return 1/guess + 1

def square_close_to_successor(guess):
    return approx_eq(guess * guess,guess + 1)
	
def approx_eq(x, y, tolerance=1e-3):
    return abs(x - y) < tolerance
	
phi = improve(golden_update,square_close_to_successor)

"""
计算思路：
if the ratio of the shorter lenth to the longer length is equal to the ratio of the longer length to the sum of both lengths.
Let S=shorter length and L=longer length. 
可得S/L = L/(S+L).
L=S*(1+5^.5)/2 or approximately L=1.6S. (即一般黄金比例定义式）
"""

from math import sqrt
phi = 1/2 + sqrt(5)/2
def improve_test():
    approx_phi = improve(golden_update, square_close_to_successor)
    assert approx_eq(phi, approx_phi), 'phi differs from its approximation'
improve_test()
