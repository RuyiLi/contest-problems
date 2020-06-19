got a new problem
so basically you have N clues numbered from [1, N], and you need a certain set of clues to obtain another clue
you're given a set of clues which you start with, as well as your target clue
the goal is to find out whether or not you can get your target clue from your given clues
oh btw 0 means that you can't get that clue from any other clues, you have to be given those from the start
otherwise they're just unobtainable

example:
```
(N) 5
(clues you have to begin with) 2 3
(clue you're trying to get) 5
(clue 1) 2 4
(clue 2) 0 
(clue 3) 0
(clue 4) 3
(clue 5) 1 2 3 4
```

output is "yes" because you can get clue 4 from clue 3, and since you already have clue 2, and you just got clue 4, you can get clue 1
since you now have clues 1 (from 2 and 4), 2 (given at start), 3 (given at start), and 4 (from 3), you can get clue 5, which is the target


# freeman's solution
1. represent clue dependency via directed graph. if 2 require 3, then 3 has edge pointing to 2. HOWEVER, do not include starting clues in the graph, just throw them away.
2. keep array of pairs, one pair for each node in format (ingoing edges, node #). let cnt = 0
3. sort deg array.
4. look at deg[cnt].first. if it is 0, then "remove" this node from graph because the dependancy conditions are met. to remove just loop thorugh all outgoing edges of node deg[cnt].second and subtract 1 from the destination degree then cnt++
5. keep doing until cannot find 0
if ur destination is in removed pile then u can reach it
not nlogn oof more like Elogn
oof that is quite bad if very dense graph
