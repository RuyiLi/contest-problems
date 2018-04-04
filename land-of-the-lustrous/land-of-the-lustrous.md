# Land of the Lustrous
Phosphophyllite (Phos-chan for short) has shattered yet again! Rutile, frustrated with Phos' tendency to shatter, asks you for a certain amount of gold and platinum alloy in order to strengthen Phos' body. Since you, the amazing Graphite (Graph-chan for short) are a coder and not a fighter, you decide to pass on the task to another, more able Gem; namely, Bort. As you make your way to Bort's living space, you are stopped by Alexandrite, who provides you with a square map of size S flled with information about possible Lunarian locations as well as possible alloy locations. As she can hardly contain her excitement at the very thought of Lunarians, the two of you engage in a match of tug-of-war for a couple of seconds, after which you successfully manage to pry the information from her hands. The map consists of certain symbols: empty spaces are represented by `.`, possible Lunarian locations by `L`, and possible alloy locations by `A`. You thank Alexandrite (who is still in a state of ecstasy due to hearing the word "Lunarian") and locomote to Bort's location. 

After explaining everything to Bort, they examine the graph for a while. After they are finished doing so, Bort asks you Q questions; however, your inability to do anything social renders you unable to answer their questions, so you just give Bort a piece of paper. On the paper are Q lines, with the ith line containing one integer, d_i. Bort explains that they want to be as efficient as possible, so they would like to know the maximum amount of alloy they can obtain by travelling d_i units (the way back does not count as part of the trip), **starting from the top-left corner while avoiding all Lunarians**. Since you, the amazing Graph-chan, are the best and only coder in and amongst the Gems, you figure that it is a trivial task to just write a program to answer Bort's queries.

# Input Specification
The first line will consist of one integer, S (1<=S<=100), representing the size of the map.

The following S lines will consist of S characters, representing the map with the aforementioned symbols.

The `S+2`th line will consist of one integer, Q (2<=Q<=10^6), representing the amount of Bort's queries.

The following Q lines will each consist of one integer, d_i (1<=d_i<=S), the maximum distance that Bort would like to travel.

# Output Specification
For each query (the ith), print a single integer on a new line, representing the maximum amount of alloy that Bort can obtain by travelling by travelling d_i units.

# Sample Input
```
5
..ALL
.L.LA
AA.L.
LL..A
AALL.
5
4
2
1
9
8
```

# Sample Output
```
2
1
0
4
3
```
