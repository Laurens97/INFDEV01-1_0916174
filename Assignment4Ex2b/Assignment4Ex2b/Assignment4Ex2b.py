"""
to-do:
1.      Implement explanation as to why player 1/2 or cpu won.
2. //   Clear screen when player has chosen character, and tell what player x has chosen after match, before result.
3. //   Maybe random player 2
4.      Replaying feature. (play = True, while play: ... again=str(input("Play again? ", if again == "no":, play = False)
"""
    #importing os function for clearing screen
import os
    #importing randint fuction from random library
from random import randint

    #no error when wrong input
move = raw_input("Player 1: Choose rock, paper, scissors, lizard or spock: ")
while not (move == "scissors" or move == "rock" or  move == "paper" or  move == "lizard" or  move == "spock"):
    move = raw_input("Wrong input. Choose rock, paper, scissors, lizard or spock: ")

    #clear screen
os.system('cls')

    #cpu human input
randyn = raw_input("Will player 2 be a CPU or a human?\n(Please don't answer with yes or no, Maggiore.): ")

    #cpu human yes no input check
while (randyn == "yes" or randyn == "Yes" or randyn == "YES"  or randyn == "no" or randyn == "No" or randyn == "NO"):
    randyn = raw_input("Are you kidding me? Just please tell me; CPU or human?: ")

    #cpu human input check
while not (randyn == "CPU" or randyn == "cpu" or randyn == "human"  or randyn == "HUMAN" or randyn == "a CPU" or randyn == "a cpu" or randyn == "a human"):
    randyn = raw_input("Wrong input. Will player 2 be a CPU or a human?: ")

    #clear screen
os.system('cls')

    #if cpu = yes, random cpu
if (randyn == "CPU" or randyn == "cpu" or randyn == "a CPU" or randyn == "a cpu"):
    cpu=randint(1,5)
    if cpu==1:
        move2="scissors"
    elif cpu==2:
        move2="paper"
    elif cpu==3:
        move2="rock"
    elif cpu==4:
        move2="lizard"
    elif cpu==5:
        move2="spock"
else:
    #player2 human input check
    move2 = raw_input("Player 2: Choose rock, paper, scissors, lizard or spock: ")
    while not (move2 == "scissors" or move2 == "rock" or  move2 == "paper" or  move2 == "lizard" or  move2 == "spock"):
        move2 = raw_input("Wrong input. Choose rock, paper, scissors, lizard or spock: ")

    #clear screen
os.system('cls')

sc = "scissors"
pa = "paper"
ro = "rock"
li = "lizard"
sp = "spock"

scc = "Scissors"
pac = "Paper"
roc = "Rock"
lic = "Lizard"
spc = "Spock"

bt = " beats "
dw = " draws with "
scb = "A cutting edge "
pab = "A flat "
rob = "A soul crushing "
lib = "A nasty bite of a "
spb = "A beaming "

win = "victory for player 1! :D\n"
los = "loss for player 1! :(\n"
draw = "draw! :/\n"

err = "\nOops. The programmer screwed up :/"

    #import function where a beats b
print "Player 1 chose " + move + "!"
print "Player 2 chose " + move2 + "!"
if move == sc:
    if move2 == sc:
        print scb + draw + scc + dw + sc + "."
    elif move2 == pa:
        print scb + win + scc + bt + pa + "."
    elif move2 == ro:
        print scb + los + roc + bt + sc + "."
    elif move2 == li:
        print scb + win + scc + bt + li + "."
    elif move2 == sp:
        print scb + los + spc + bt + sc + "."
    else:
        print err

if move == pa:
    if move2 == pa:
        print pab + draw + pac + dw + pa + "."
    elif move2 == ro:
        print pab + win + pac + bt + ro + "."
    elif move2 == sc:
        print pab + los + scc + bt + pa + "."
    elif move2 == li:
        print pab + los + lic + bt + pa + "."
    elif move2 == sp:
        print pab + win + pac + bt + sp + "."
    else:
        print err
        
if move == ro:
    if move2 == ro:
        print rob + draw + roc + dw + ro + "."
    elif move2 == sc:
        print rob + win + roc + bt + sc + "."
    elif move2 == pa:
        print rob + los + pac + bt + ro + "."
    elif move2 == li:
        print rob + win + roc + bt + li + "."
    elif move2 == sp:
        print rob + los + spc + bt + ro + "."
    else:
        print err
        
if move == li:
    if move2 == ro:
        print lib + los + roc + bt + li + "."
    elif move2 == sc:
        print lib + los + scc + bt + li + "."
    elif move2 == pa:
        print lib + win + lic + bt + pa + "."
    elif move2 == li:
        print lib + draw + lic + dw + li + "."
    elif move2 == sp:
        print lib + win + lic + bt + sp + "."
    else:
        print err
        
if move == sp:
    if move2 == ro:
        print spb + win + spc + bt + ro + "."
    elif move2 == sc:
        print spb + win + spc + bt + pa + "."
    elif move2 == pa:
        print spb + los + pac + bt + sp + "."
    elif move2 == li:
        print spb + los + lic + bt + sp + "."
    elif move2 == sp:
        print spb + draw + spc + dw + sp + "."
    else:
        print err

raw_input('\nPress Enter to exit.')