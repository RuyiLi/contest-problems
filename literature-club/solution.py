n, k = map(int, input().split())
input()
f = [0] * 4
names = ['Sayori', 'Natsuki', 'Yuri', 'Monika']
d = [input().split() for asdf in range(4)]
poem = ' '.join([input() for asdf in range(n)])
for x in range(4):
    f[x] = len(list(filter(lambda a: a in poem, d[x])))
    print(list(filter(lambda a: a in poem, d[x])))
m = max(f)
match = list(filter(lambda e: f[e] == m, range(4)))
print('\n'.join(list(map(lambda j: names[j], match))))