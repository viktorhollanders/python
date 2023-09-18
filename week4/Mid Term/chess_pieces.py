chess_piece_value = int(input())

if chess_piece_value == 1:
    print("Pawn")
elif chess_piece_value == 3:
    print("Bishop or Knight")
elif chess_piece_value == 5:
    print("Rook")
elif chess_piece_value == 9:
    print("Queen")
else:
    print("No piece")
