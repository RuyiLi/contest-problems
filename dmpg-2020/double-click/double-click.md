We're given a string S containing alphanumeric characters and punctuation
We "double-click" a character at index N
Double-clicking highlights all characters around the character that are of the same type (i.e. all alphanumeric or all punctuation excepting spaces)
If the punctuation character is only one character long, highlight the alphanumeric section to the left instead (even if it is also only one character long)


Sample 1
_In this research, we present two comparative studies; the first one is between two methods_
- double click at anywhere before the semicolon highlights "In this research, we present two comparative studies"
- after gives "the first one is between two methods"
- doubleclicking the semicolon highlights "In this research, we present two comparative studies"


Sample 2
_a;bc;;;;_
- double clicking "a" highlights "a"
- dcing the first semi highlights "a"
- dcing "b" or "c" highlights "bc"
- dcing any of the semis after "bc" highlights them all