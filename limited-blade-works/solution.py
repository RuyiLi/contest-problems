n, mr = map(int, input().split())
x, y, z = map(int, input().split())
pos = [list(map(int, input().split())) for asdf in range(n)]
r = -1
for ax, ay, az in pos:
    d = ((x-ax)**2 + (y-ay)**2 + (z-az)**2)**.5
    r = max(d, r)

print('LIMITED BLADE WORKS' if r > mr else 'RETREAT')