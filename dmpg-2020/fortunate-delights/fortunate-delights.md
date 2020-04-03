Hondomachi is playing the game on the back of her Fortunate Delights :tm: cereal box! On the box, a path made up of various cereal pieces is shown, and the objective is to get from the start to the finish. She can move by taking a random piece from the cereal and moving to the next place where that piece appears until the final piece is reached. There are a total of 10 different cereal pieces, all of which will appear on the path. Given the length of the path and the path itself, with the various pieces represented using the numbers from 0 to 9, what is the least amount of pieces Hondomachi needs to draw to reach the end point?

## Input Specification
The first line will consist of a single integer, N, representing the length of the path.
The second line will consist of N digits, numbers from 0-9 representing types of different cereal pieces.

## Output Specification
A single integer, representing the least amount of moves she needs to make to complete the path.

## Sample Input
```
31
0123456789012345678901234567890
```

## Sample Output
```
4
```

## Explanation for Sample
There are a variety of possible sequences of pieces that Hondomachi can draw in order to obtain a swift victory. Some examples include:
- 0 -> 0 -> 0 -> 0 (length 4)
- 9 -> 9 -> 9 -> 0 (length 4)
- 9 -> 0 -> 0 -> 0 (length 4)

Alternative but longer paths include:
- 0 -> 0 -> 1 -> 1 -> 0 (length 5)
- 9 -> 0 -> 9 -> 0 -> 9 -> 0 (length 6)
