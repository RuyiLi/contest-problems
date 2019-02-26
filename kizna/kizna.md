Through the use of the revolutionary Kizna system, scientists have found a way to distribute pain evenly amongst a network of ~N~ people in Sugomori City. This feat is accomplished by dividing the entire city into a square grid, and determining a path for the pain from the first person to the second, from the second person to the third, and so on. The ~i~th person will be standing at position ~(x_i, y_i)~; the ~-i+1~th person is guaranteed to be at least 2 units apart, horizontally and vertically.

The pain starts at the position of the first person, and can only traverse the square grid one unit north or one unit east. It cannot move diagonally. It will not attempt to find anyone else before it has found the next person, starting fron the first person. 

The scientists have asked you to write a program to find the total number of ways to distribute the pain, so that they can do their science stuff in order to make the system more efficient.


## Input Specifications
The first line will contain the number ~N (2<=N<=TODO constraints)~, the number of people connected to the Kizna network.
The following ~N~ lines will consist of two integers, ~x_i ~ and ~y_i (TODO constraints)~. These coordinates are guaranteed to be in order

## O