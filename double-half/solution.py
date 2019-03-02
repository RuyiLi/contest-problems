num = dict()
for _ in range(int(input())):
    n, d = input().split()
    num[n] = num.get(n, 0) + 1
    num[d] = num.get(d, 0) - 1
print('Not' if len(set(num.values())) - 1 else 'Double Half')