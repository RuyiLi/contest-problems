n = int(input())
#True = face up, False = face down
a = [False] * n
for x in range(2,n+1):
    for i in range(x, n+1, x):
        a[i-1] = not a[i-1]
s = 0
for idx, _ in enumerate(a):
    if not _: s += idx + 1

print(s % (10e9+7))