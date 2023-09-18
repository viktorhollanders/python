p1_move = input()
p2_move = input()
# ...now fill in the rest

p1 = p1_move.lower()
p2 = p2_move.lower()

if p1 == p2:
    print("Draw")
elif p1 == "scissors" and p2 == "paper":
    print("player 1")
elif p1 == "paper"  and p2 == "rock":
    print("player 1")
elif p1 == "rock" and p2 == "scissors":
    print("player 1")
else:
    print("player 2")



