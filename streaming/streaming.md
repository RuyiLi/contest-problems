# Streaming

echofox is playing the popular rhythm game, osu! However, he is not very good at doing streams (explained below), and thus will give any map that consists of at least ~N~ streams a rating of 1 star. The being referring to himself in third person requests that you write a program to determine if a map has too many streams so that he knows what to rate it once he beats it with NF on.

A stream is defined as a sequence of **10 or more circles** that appear rapidly one after another in a line. Because they are so close to each other, osu! players must alternate between pressing their Z and X keys in rapid succession in order to not fail. **Essentially, if there are 5 or more ~XZ~s in a row, it counts as a stream.**

To help you with your task, echofox has voluntarily installed a keylogger onto his computer that keeps tracks of the keys he has pressed while playing osu. After a map is completed, it is saved into a text file consisting of only `Z`s and `X`s which he then sends to you to analyze. Each `Z` or `X` represents one circle. Each map will have exactly 140 circles.

Given ~K~ text files, each consisting of 2 lines: the name of the map and the corresponding keylog, write a program that prints the names of all of the maps that he should give a rating of 1 star to.

## Input Specification
The first line will contain two integers, ~N~ and ~K~ ~(1<=N, K<=100)~.

The following lines will contain two lines for each of the ~K~ maps:
1. The name of the map
2. The text file containing all of the keystrokes made while playing the map, containing a string made of ~Z~s or ~X~s   

## Output Specification
The names of the maps that echofox should rate a 1, seperated by line breaks, in alphebetical order.

## Sample Input
```
2 3
xi - Freedom Dive [FOUR DIMENSIONS]
XZXZXZXZXZXZXZXZXZXZXXXXXXXXXXXXXXXXXXZXZXXXXZXZXXXXXZXZXZXZXXXXXXXZXZXZXZXZXZXZXZZXZXZXZXZXZXZXZXXXXXXXZXZXZXZXZXXXXXXZXZXZXXXXXXXXXXXXXXXX
Icon For Hire - Make a Move (Speed Up Ver.) [Expert]
XXXXXXXXXXXXZXZXZXZXZXXXXXXXXXXXXXXXXXXXXXXXXZXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXZXZXXXXXXZXZXXXXXXXXXXXXXXXXXZXXXXXXXXXXXZXXZXXXXXXXXXXXX
ClariS - Hitorigoto [Kencho's Insane]
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXZXXXXXXXXXZXZXXXXXZXZXZXZXZXXXXXXXXXXXXXXXZXZXZXZXZXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

## Sample Output
```
ClariS - Hitorigoto [Kencho's Insane]
xi - Freedom Dive [FOUR DIMENSIONS]
```

## Explanation
Streams will be distinguished by bold text.

Since ~N = 2~ and ~K = 3~, there will be 3 songs which echofox will give a rating of 1 star if they have 2 or more streams. 

---
`xi - Freedom Dive [FOUR DIMENSIONS]`

**XZXZXZXZXZXZXZXZXZX**ZXXXXXXXXXXXXXXXXXXZXZXXXXZXZXXXXXZXZXZXZXXXXXX**XZXZXZXZXZXZXZ**XXZX**XZXZXZXZXZXZXZ**XXXXXX**XZXZXZXZXZ**XXXXXXZXZXZXXXXXXXXXXX

There are 4 streams, so by echofox's definition, this map has too many streams. Thus, he should rate it a 1.

---
`Icon For Hire - Make a Move (Speed Up Ver.) [Expert]`

XXXXXXXXXXX**XZXZXZXZXZ**XXXXXXXXXXXXXXXXXXXXXXXXZXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXZXZXXXXXXZXZXXXXXXXXXXXXXXXXXZXXXXXXXXXXXZXXZXXXXXXXXXXXX

This map only has one stream, so it will be spared from a rating of 1.

---
`ClariS - Hitorigoto [Kencho's Insane]`
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXZXXXXXXXXXZXZXXXX**XZXZXZXZXZ**XXXXXXXXXXXXXX**XZXZXZXZXZ**XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

This map has 2 streams, so it should be given a rating of 1.

## Disclaimer
(This doesn't affect the question, just a small afterword)

Maps in osu actually require much more keystrokes than in the sample input. They have been omitted for the sake of brevity (not really).