*"Challenge: I request participation in this game." - Unit Üc207Pr4f57t9*

Shuvi and Riku are playing a game called Double Half. In this game, Riku reads out ~N~ pairs of numbers representing the numerators and denominators of fractions and Shuvi is to determine if their product is equal to 1 and say "Double Half" if it is or "Not" if it is not. Shuvi, being an Ex-Machina, wishes to utilize a program to automatically determine the answer. However, there is a catch; her speech synthesis program interprets numbers as words rather than actual digits. Write a program to determine if the product of the rational expressions is equal to 1 and print the appropriate response.

## Input Specifications
The first line will contain a number, ~N (2<=N<=10^6)~.

The following ~N~ lines will each contain the verbal representations for the numerator and denominator, respectively, of the corresponding fraction. 

The numerator and denominator will consist solely of lowercase alphabetic characters (a-z).

## Output Specifications
A single line containing the words "Double Half" if the product is equal to 1, or "Not" if the product is not equal to 1.

## Sample Input 1
```
4
one three
seven onehundredthree
onehundredthree one
three seven
```

## Sample Output 1
```
Double Half
```

## Sample Input 2
```
3
seven nine
five seven
nine one
```

## Sample Output 2
```
Not
```
