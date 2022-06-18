"Requirments for TIC-TAC-TOE"
# - 2 players should be able to play the game (both sitting at the same 
#   computer)

# - The board should be printed out every time a player makes a move

# - You should be able to accpet input of the player position and then 
#   place a symbol on the board

row1 = ["1", " ", " ", " ", " ", "", " ", " ", "|", "2", " ", "", " ", " ", " ", "", " ", "|", "3"]
row2 = [" ", " ", " ", " ", " ", "", " ", " ", "|", " ", " ", "", " ", " ", " ", "", " ", "|", " ", " ", " "]
row3 = [" ", " ", " ", " ", " ", "", " ", " ", "|", " ", " ", "", " ", " ", " ", "", " ", "|"]
spaces = ["---------------------"]
row4 = ["4", " ", " ", " ", " ", "", " ", " ", "|", "5", " ", "", " ", " ", " ", "", " ", "|", "6"]
row5 = [" ", " ", " ", " ", " ", "", " ", " ", "|", " ", " ", "", " ", " ", " ", "", " ", "|", " ", " ", " "]
row6 = [" ", " ", " ", " ", " ", "", " ", " ", "|", " ", " ", "", " ", " ", " ", "", " ", "|"]
row7 = ["7", " ", " ", " ", " ", "", " ", " ", "|", "8", " ", "", " ", " ", " ", "", " ", "|", "9"]
row8 = [" ", " ", " ", " ", " ", "", " ", " ", "|", " ", " ", "", " ", " ", " ", "", " ", "|", " ", " ", " "]
row9 = [" ", " ", " ", " ", " ", "", " ", " ", "|", " ", " ", "", " ", " ", " ", "", " ", "|"]


def ask_user():

    choice = "wrong"

    global player1
    player1 = ""

    global player2 
    player2 = ""

    while choice.upper() not in ["X", "O"]:
        choice = input("Player 1: Do you want to be X or O? ").upper()
        
        if choice.upper() not in ["X", "O"]:
            print("Please either choose X or O")
        
    if choice == "X":
        print("\nPlayer 1, 'X' will go first.")
        player1 += "X"
        player2 += "O"
    elif choice == "O":
        print("Player 1, 'O' will go first.")
        player1 += "O"
        player2 += "X"

def ready():
    global readier
    readier = ""

    while readier.upper() not in ["YES"]:
        readier = input("Are you ready? Yes?: ")

        if readier.upper() not in ["YES"]:
            print("Please either say yes or otherwise exit the game.")

def board():
    print(f" {''.join(row1)} \n {''.join(row2)} \n {''.join(row3)} \n {''.join(spaces)} \n {''.join(row4)} \n {''.join(row5)} \n {''.join(row6)} \n {''.join(spaces)} \n {''.join(row7)} \n {''.join(row8)} \n {''.join(row9)}")

def player_one():
    placement = "WRONG"

    while placement not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "quit"]:
        placement = input(("Choose your next box: "))

        if placement not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "quit"]:
            print('Please enter only (number) of the box - like 1')

        if placement == "quit":
            break

    if placement == "1":
        row2[4] = player1
    if placement == "2":
        row2[13] = player1
    if placement == "3":
        row2[20] = player1
    if placement == "4":
        row5[4] = player1
    if placement == "5":
        row5[13] = player1
    if placement == "6":
        row5[20] = player1
    if placement == "7":
        row8[4] = player1
    if placement == "8":
        row8[13] = player1
    if placement == "9":
        row8[20] = player1

def player_two():
    global placement
    placement = "WRONG"

    while placement not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "quit"]:
        placement = input("Choose your next box number: ")

        if placement not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "quit"]:
            print('Please enter only enter the number of box where you want to place your X or O')

    if placement == "1":
        row2[4] = player2
    if placement == "2":
        row2[13] = player2
    if placement == "3":
        row2[20] = player2
    if placement == "4":
        row5[4] = player2
    if placement == "5":
        row5[13] = player2
    if placement == "6":
        row5[20] = player2
    if placement == "7":
        row8[4] = player2
    if placement == "8":
        row8[13] = player2
    if placement == "9":
        row8[20] = player2

win_check = False
def checker():
    return((row2[4] == row2[13] == row2[20]) or (row5[4] == row5[13] == row5[20]) or (row5[4] == row5[13] == row5[20]) or (row8[4] == row8[13] == row8[20]) or (row2[4] == row5[4] == row8[4]) or (row2[13] == row5[13] == row8[13]) or (row2[20] == row5[20] == row8[20]) or (row2[4] == row5[13] == row8[20]) or (row2[20] == row5[13] == row8[4]))



#GAME FUNCTIONS
print("Welcome to The Modified Tic - Tac - Toe game")
print("\nBackground:\nTic-Tac-Toe always had only one winner. But why not have two?\nDue to this reason, a game has been made in which there could be more than one winner.\nAs long as there are spots left on the board, you can still win.\nI hope you enjoy playing the game")
print("\nInstructions: \n1. Please play the entire game")
print('\n2. Choose your box - make sure to say the number of the box \n   For example, it can be something like "1"\n\n3. Most of all, have fun\n\nMore updates to come soon\n\n')
ask_user()
print("\n")
ready()
print("\n")
board()
x = 0
while x != 9: 
    player_one()
    print("\n" * 100)
    board()
    x += 1

    player_two()
    print("\n" * 100)
    board()
    x += 1

    if x == 8:
        player_one()
        print("\n" * 100)
        board()
        x += 1
    checker()
    if checker() == True:
        break