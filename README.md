# flip-a-coin-strategy
#
# Author: Philip Ruehl
# Date: 2022-01-06
#

Idea: play a simple game -- the player either wins or loses. If the player wins the game, he gets twice 
the stake money and continues playing with the same stake. If he looses, the player doubles the stake. 
The game ends if the player cannot afford another round.
The amount gain/loss may also be variabel.

Questions:

 * What is the expected number of rounds depending on the players seed capital? What does the 
   distribution look like?
 * Does the game always come to an end?
 * What is the expected maximum capital depending on the seed capital?
 * How many rounds have to be played (on average) until the maximum capital is reached?
 * How big is the confidence that the maximum can be reached before the game ends?
 * (redundant question) What seed capital is neccessary to reach the maximum (or any given threshold) 
   at 3/4/5 sigma confidence level before the game ends?
