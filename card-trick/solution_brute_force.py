n = int(input())
#True = face up, False = face down
a = [False] * n
for x in range(2,n+1):
    for i in range(x, n+1, x):
        a[i-1] = not a[i-1]
s = 0
for i, b in enumerate(a):
    if not b: s += i + 1

print(s)