move = raw_input("Player 1: Choose rock, paper or scissors: ")
while not (move == "scissors" or move == "rock" or  move == "paper"):
    move = raw_input("Wrong input. Choose rock, paper or scissors: ")

move2 = raw_input("Player 2: Choose rock, paper or scissors: ")
while not (move2 == "scissors" or move2 == "rock" or  move2 == "paper"):
    move2 = raw_input("Wrong input. Choose rock, paper or scissors: ")

sc = "scissors"
pa = "paper"
ro = "rock"

scb = "A cutting edge "
pab = "A flat "
rob = "A soulcrushing "

win = "victory! :D"
los = "loss! :("
draw = "draw! :/"

err = "The programmer screwed up :/"

if move == sc:
    if move2 == sc:
        print scb + draw
    elif move2 == pa:
        print scb + win
    elif move2 == ro:
        print scb + los
    else:
        print err

if move == pa:
    if move2 == pa:
        print pab + draw
    elif move2 == ro:
        print pab + win
    elif move2 == sc:
        print pab + los
    else:
        print err
        
if move == ro:
    if move2 == ro:
        print rob + draw
    elif move2 == sc:
        print rob + win
    elif move2 == pa:
        print rob + los
    else:
        print err