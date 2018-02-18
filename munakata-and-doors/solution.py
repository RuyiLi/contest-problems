def f(s):
    if s <= 1:
        return 1
    return s * f(s-1)

m, n = map(int, input().split())
a, b, c, d = map(int, input().split())

t = f(m+n)/(f(m)*f(n))
x = f(a+b)/(f(a)*f(b))
y = f(m-c+n-d)/(f(m-c)*f(n-d))

print(int(t-x*y))