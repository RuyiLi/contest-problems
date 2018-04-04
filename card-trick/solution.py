n = int(input())
s = 0
for i in range(1, int(n**.5) + 1):
    s += i**2
print(s)