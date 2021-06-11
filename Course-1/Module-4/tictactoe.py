from random import randrange

board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def display_board():
    global board

    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   " + board[0] + "   |   " + board[1] + "   |   " + board[2] + "   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   " + board[3] + "   |   " + board[4] + "   |   " + board[5] + "   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   " + board[6] + "   |   " + board[7] + "   |   " + board[8] + "   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")

def enter_move():
    global board

    while (True):
        num = int(input("Enter your move: "))
        if num <= 0 or num >= 10 or board[num - 1] == "X" or board[num - 1] == "O":
            print("Please enter a valid space!")
        else:
            break

    board[num - 1] = "O"

def draw_move():
    global board

    if board[4] != "X" and board[4] != "O":
        board[4] = "X"
    else:
        while (True):
            rand = randrange(8)
            if board[rand] != "X" and board[rand] != "O":
                break
        board[rand] = "X"

def victory():
    global board

    if ((board[0] == "X" and board[1] == "X" and board[2] == "X") or (board[3] == "X" and board[4] == "X" and board[5] == "X") or
    (board[6] == "X" and board[7] == "X" and board[8] == "X") or (board[0] == "X" and board[3] == "X" and board[6] == "X") or
    (board[1] == "X" and board[4] == "X" and board[7] == "X") or (board[2] == "X" and board[5] == "X" and board[8] == "X")):
        print("The Computer has Won!")
        return True
    elif ((board[0] == "O" and board[1] == "O" and board[2] == "O") or (board[3] == "O" and board[4] == "O" and board[5] == "O") or
    (board[6] == "O" and board[7] == "O" and board[8] == "O") or (board[0] == "O" and board[3] == "O" and board[6] == "O") or
    (board[1] == "O" and board[4] == "O" and board[7] == "O") or (board[2] == "O" and board[5] == "O" and board[8] == "O")):
        print("The Player has Won!")
        return True
    else:
        for item in board:
            if item != "O" and item != "X":
                return False
        print("The Game has Ended in a Tie!")
        return True

display_board()

while (True):
    enter_move()
    if victory(): break
    display_board()
    draw_move()
    if victory(): break
    display_board()
    
print("\nThe End")
