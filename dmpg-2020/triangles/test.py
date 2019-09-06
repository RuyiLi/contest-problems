from random import randint

n = [3, 4, 4, 4, 5]

length = len(n)


def area(a, b, c):
    s = (a + b + c) / 2
    return (s ** 2) * ((s - a) ** 2) * ((s - b) ** 2) * ((s - c) ** 2)


def is_valid(a, b, c):
    return a + b > c and b + c > a and a + c > b


areas = []

# naive solution
for i in range(length):
    for j in range(i + 1, length):
        for k in range(j + 1, length):
            q, w, e = n[i], n[j], n[k]
            if not is_valid(q, w, e):
                continue
            areas.append(area(q, w, e))

print(sorted(areas, reverse=True))
print()
# gets 3 largest sides, yes i know i didnt check if they were valid
print(area(*sorted(n, reverse=True)[: 3]))
