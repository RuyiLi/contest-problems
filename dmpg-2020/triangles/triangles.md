Flandre really loves triangles! She loves them so much, in fact, that she wants to create the biggest triangle possible using her collection of $N$ crystals. Each crystal has a length $S_i$ and a color $C_i$, and she will use these crystals to create her triangle. Since she also likes nice patterns of colors, she will only accept triangles that are formed from 3 unique colors. Please help her by creating a program that will print the **square of the area** of the largest triangle that can be created, following these constraints!

It is guaranteed that there will be at least 3 different colors.

## Input Specification
The first line will contain a single integer, $N (3 < N <= 5 * 10^3)$.

The second line will consist N integers, representing the length each crystal, with the ith crystal having a length of $S_i (todo constraints)$.

The third and final line of input will contain N strings, representing the color of each crystal, with the ith crystal having a color $C_i (1 <= |C_i| <= 10)$.

## Output Specifications
A single integer, representing the area of the largest triangle formed using all different colors, squared. If no such triangle can be formed, print `-1`.

## Sample Input
```
5
4 3 4 2 5
green blue red blue red
```

## Sample Output
```
36
``` 