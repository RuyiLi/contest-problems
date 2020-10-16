To celebrate Halloween, many companies are mass purchasing chocolate. You are the CTO of Harshay's Chocolate, the most popular distributor of chocolates in the entire country of Vatican City, and have received $N$ orders requesting exactly $n_i$ chocolates. The problem is, you only sell chocolate in packs of certain sizes, and thus may not be able to sell an exact amount of chocolates to a customer. Harshay's offers $A$ types of packs, with the $i$th pack containing $a_i$ chocolates. Due to the large amount of orders, you decide to create a program to determine which orders are unfulfillable.

# Input Specification
The first line of input contains a number $A$.

The second line of input contains $A$ numbers, representing the sizes of the packs offered.

The third line of input contains a number $N$ representing the number of orders.

The following $N$ lines each contain a number, representing the amount of chocolates that a company has ordered.

# Output Specification
$N$ lines containing either the string `YES` or `NO`, depending on if the respective order can be fulfilled.

# Sample Input
```
2
4 5
7
3
4
5
6
9
11
13
```

# Sample Output
```
NO
YES
YES
NO
YES
NO
YES
```