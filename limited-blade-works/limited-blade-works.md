# Limited Blade Works
Archer, the servant of Rin Tohsaka in the Fuyuki Holy Grail War, is activating his Noble Phantasm, Limited Blade Works! Limited Blade Works is a reality marble which affects anyone within a sphere, originating from the caster, within a certain radius. However, Tohsaka only has ~M~ mana, which is enough to allow Archer to cast his Noble Phantasm in a sphere of radius ~M~. Tohsaka, being the strategist that she is, wants to know if she has enough mana to use Archer's Noble Phantasm on all ~N~ enemies with the ~i~th enemy positioned at ~P_i~, assuming she only has ~M~ mana. Write a program that prints "LIMITED BLADE WORKS" if she has enough mana to use Limited Blade Works on all of the enemies, or "RETREAT" if she does not have enough mana and should retreat.

## Input Specification
The first line of input will contain two integers, ~N~ and ~M (1 \le N \le 1000, 1 \le M \le 100)~, that represent the amount of enemies and the amount of mana Tohsaka has, respectively.

The second line of input will contain three integers, representing the x, y, and z coordinates of Archer.

The following ~N~ lines of input represent the x, y, and z coordinates of the ~P_i~th enemy.

## Output Specification
Print "LIMITED BLADE WORKS" if she has enough mana or "RETREAT" if she does not have enough mana.

## Sample Input 1
```
3 5
0 0 0
1 1 1
1 1 0
2 2 0
```

## Sample Output 1
```
LIMITED BLADE WORKS
```

## Sample Input 2
```
4 5
0 0 0
1 1 1
1 1 0
2 2 0
3 3 5
```

## Sample Output 2
```
RETREAT
```