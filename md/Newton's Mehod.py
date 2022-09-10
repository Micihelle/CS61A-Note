#逼近收敛
def improve(update, close, guess=1):
    while not close(guess):  
        guess = update(guess) 
    return guess

def approx_eq(x, y, tolerance=1e-3):
    return abs(x - y) < tolerance

#沿着 tangent 计算
def newton_update(f, df):
        def update(x):
            return x - f(x) / df(x)
        return update

#查找零点近似值
def find_zero(f, df):
        def near_zero(x):
            return approx_eq(f(x), 0)
        return improve(newton_update(f, df), near_zero)

#利用Newton's Method 计算平方根
def square_root_newton(a):
        def f(x):
            return x * x - a
        def df(x):
            return 2 * x
        return find_zero(f, df)

#推广到任意 degree 的平方根
def power(x, n):
        """Return x * x * x * ... * x for x repeated n times."""
        product, k = 1, 0
        while k < n:
            product, k = product * x, k + 1
        return product

def nth_root_of_a(n, a):
        def f(x):
            return power(x, n) - a  #f(x)=x^n-a
        def df(x):
            return n * power(x, n-1) # df(x)=n*x^(n-1)
        return find_zero(f, df)
