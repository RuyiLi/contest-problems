# Literature Club
Sayori, your childhood friend, has invited you to hang out with her in the Literature Club! Since you were looking for a club to join, you decide to accompany her. As luck has it, the club's members are all cute girls! In order to win their hearts, you must write poems suited to each girls' taste. Each member of the Literature Club has a set of W "trigger words" that, when used in a poem, increases your closeness points with them; duplicates will only be counted **once**. Your poem will consist of N sentences and K words in each sentence, and you want to know how your poem will affect your closeness with each member. Write a program that outputs the name of the girl with the highest number of closeness points. If your poem contains a word that is in none of the sets, you can ignore the word.

## Input Specification
You can assume that all input will be lowercase.

The first line of input contains two integers N and K, (1 <= N <= 10, 1 <= K <= 10) representing the number of sentences and the number of words in each sentence, respectively.

The second line of input contains an integer W (1 <= W <= 25) representing the size of the set of "trigger words" for each club member.

The next four lines contain the sets of "trigger words" for the four club members - Sayori, Natsuki, Yuri, and Monika - respectively.
Your poem will be made up of the next N lines, each containing K words.

> **Note:** The third to sixth lines of input will always contain trigger words in the exact order of Sayori, Natsuki, Yuri, and Monika. This is important for determining the output.

## Output Specification
The output should consist of one line containing the name(s) of the girls with the highest closeness points. The order in which you print their names do not matter. If two or more girls have the same number of closeness points, print all of their names, separated by a newline. If the **total** number of closeness points is equal to 0, the output will be empty.

## Sample Input
```
5 4
4
depression friend annoying weeb
cupcake happiness rainbow sky
knife storm massacre apocalypse
literature write pen protagonist
help friend sky factory
massacre storm trapped pen
write knife heart arm
window mouse depression club
literature depression massacre rainbow
```

## Sample Output
```
Yuri
Monika
```

## Explanation of Output for Sample Input
Below is a list of trigger words for each club member found in the sample poem:
```
Sayori: ['depression', 'friend']
Natsuki: ['rainbow', 'sky']
Yuri: ['knife', 'storm', 'massacre']
Monika: ['literature', 'write', 'pen']
```
Two trigger words can be found for both Sayori and Natsuki, and three trigger words for both Yuri and Monika. Since 3 > 2, the output will be Yuri and Monika, since they both have the highest closeness points.
