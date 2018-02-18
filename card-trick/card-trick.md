# Card Trick
Victor Putin is performing a card trick ~~to impress girls~~ for educational reasons. To start the trick, he takes out a deck of cards with *N* card numbered 1 to *N*. He then gives the cards to a random audience member and tells them to place each card, face, up, in order on a table. 

After they are done, he tells them to flip every card over. Once they have done so, he instructs them to flip every card that is a multiple of 2 (if the card was face down, then it would now be face up, and vice versa). Then, he tells them to flip every card that is a multiple of 3. This continues for every number up to *N*. Once the audience has finished flipping all the cards, he announces that, without looking, he can calculate the sum of every number on every card that is still face down. You, being the master coder that you are, decide to one-up Victor so you can ~~impress girls~~ improve your coding skills. Write a program that, when given *N*, determines the sum of every number on every card that is still face down.

## Input Specification
The first line of input will contain one integer, *N* (*1<=N<=10^8*).

## Output Specification
Print the sum of every number on every card that is still face down after undergoing the process described in the problem.

## Sample Input 1
```
4
```

## Sample Output 1
```
5
```

## Sample Input 2
```
37
```

## Sample Output 2
```
91
```