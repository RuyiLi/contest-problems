n by m grid, top left is (0, 0) and bottom right is (n-1, m-1)
S black holes placed at various positions (x_i, y_i)
water falls down from the top but will stop upon encountering a black hole
print the resultant stream: water is `X`, empty is a space, black hole is `.`

e.g.
```
5 5  // width, height
3    // number of stones
0 1  // positions of stones
2 1
3 3
```

output:
```
XXXXX
.X.XX
 X XX
 X .X
 X  X
```