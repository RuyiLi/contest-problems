Haruna just got a new Googol Home and wants to use it to play her favorite songs! She will ask the device to play a multitude of songs from her playlist.
However, since Haruna is not subscribed to YooToob Music Premium, the Home will play the song with the name that is the least similar to the one requested.

The similarity between two songs, A and B, is calculated as following:
- For each letter in A that is in B and in the correct place, subtract 1 from the "difference score".
- For each letter in A that is in B but in the incorrect place, subtract 0.5 from the score.
- For each letter in A that is not in B, add 1 to the score.
- Finally, add the absolute differences in the lengths of A and B to the score.

She has a playlist of P songs, and will ask the Home to play Q songs. For each query, print the corresponding least similar song. If there exists a tie between two songs, print the lexicographically least song.