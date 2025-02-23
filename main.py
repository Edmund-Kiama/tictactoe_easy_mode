import random

board = [
    "-","-","-",
    "-","-","-",
    "-","-","-"
]
free_slots = []
current_player = "X"
winner = None

def print_board (board):
    print("")
    print(f"| {board[0]} | {board[1]} | {board[2]} |                 | 1 | 2 | 3 |")
    print("-------------                 -------------")
    print(f"| {board[3]} | {board[4]} | {board[5]} |                 | 4 | 5 | 6 |")
    print("-------------                 -------------")
    print(f"| {board[6]} | {board[7]} | {board[8]} |                 | 7 | 8 | 9 |")
    print("")

def slot_remaining():
    global free_slots
    free_slots = [index + 1 for index, slot in enumerate(board) if slot == "-"]

def player_turn():
    global board
    
    slot_remaining()
    print(f"Current player is {current_player}")

    while True:
        player = int(input(f"{current_player} player turn. Choose board position {free_slots}: "))

        if str(player) in free_slots:
            break
        else:
            print("Invalid input!! Try again!")
            print(f"Valid input: {free_slots}")


    board[player - 1] = current_player

def switch_player ():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

def comp_turn ():
    if current_player == "X":
        return None
    
    global board
    
    slot_remaining()
    comp_choice = int(random.choice(free_slots)) 
    board[comp_choice - 1] = current_player


def win_row():
    global winner

    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
    else:
        pass

def win_column():
    global winner
    
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
    else:
        pass

def win_diagonal():
    global winner
    
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
    else:
        pass

def check_win():

    win_row()
    win_column()
    win_diagonal()

    if winner != None:
        print_board(board)
        print("")
        print("###########")
        print("")
        print("Game Over!")
        print("")
        print("###########")
        print("")
        print(f"Player {winner} wins !")
        print("")

        return True
    
    return False

def choose_mode():
    print("Modes available")
    print("A. Multiplayer")
    print("B. Vs Computer")
    print("")

    while True:
        mode = input("choose your mode: ").upper().strip()

        if mode == "A" or "B":
            break
        else:
            print("Invalid input!! Try again!")
            print(f"You can only choose 'A' or 'B'")

    print(f"Mode '{mode}' chosen.")
    print("")

    return mode


def main():
    game_running = True

    mode = choose_mode()        

    while game_running and mode == "B":
        print_board(board)

        if current_player == "X":
            player_turn()
        else:
            comp_turn()

        if check_win():
            game_running = False
        else:    
            switch_player()
    
    while game_running and mode == "A":
        print_board(board)
        player_turn()

        if check_win():
            game_running = False
        else:
            switch_player()

        

if __name__ == "__main__":
    main()


