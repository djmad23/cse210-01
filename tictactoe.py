"""
TIC TAC TOE GAME
"""

def main():
    print()
    print("Tic Tac Toe")    
    exit_game = -1
    while exit_game !=0:
        number_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]       

        change_game = -1
        print("Player 1 = X")
        print("Player 2 = O")
        turn = 0
        player = ""
        while change_game != 0:
            print()
            print(f"{number_list[0]} | {number_list[1]} | {number_list[2]}")
            print(f"{number_list[3]} | {number_list[4]} | {number_list[5]}")
            print(f"{number_list[6]} | {number_list[7]} | {number_list[8]}")
            
            turn = turn + 1
            if turn == 1 or turn == 3 or turn == 5 or turn == 7 or turn == 9:
                choice = int(input("Player 1, select an available number from the table: "))
                choice = choice - 1
                number_list[choice] = "X"
                player = "PLAYER 1"
            elif turn == 2 or turn == 4 or turn == 6 or turn == 8:
                choice = int(input("Player 2, select an available number from the table: "))
                choice = choice - 1
                number_list[choice] = "O"
                player = "PLAYER 2"
            else:
                change_game == 0
                print("Tied game, no winners!")
                print()

            if get_validation(number_list) == True:
                print(f"And the winner is: {player}!")
                print()
                change_game = 0
            else:
                None

        reset_game(number_list)
        exit_game = int(input('Type "0" to exit or any number to continue!: '))
        print()
        print("Thanks for playing, see you soon!")
        print()

def get_validation(validation_list):
    result = False
    if validation_list[0] == validation_list[1] and validation_list[1] == validation_list[2]:
        result = True
    elif validation_list[3] == validation_list[4] and validation_list[4] == validation_list[5]:
        result = True
    elif validation_list[6] == validation_list[7] and validation_list[7] == validation_list[8]:
        result = True
    elif validation_list[0] == validation_list[3] and validation_list[3] == validation_list[6]:
        result = True
    elif validation_list[1] == validation_list[4] and validation_list[4] == validation_list[7]:
        result = True
    elif validation_list[2] == validation_list[5] and validation_list[5] == validation_list[8]:
        result = True
    elif validation_list[0] == validation_list[4] and validation_list[4] == validation_list[8]:
        result = True
    elif validation_list[2] == validation_list[4] and validation_list[4] == validation_list[6]:
        result = True
    return result

def reset_game(reset_list):
    reset_list[0] = "1"
    reset_list[1] = "2"
    reset_list[2] = "3"
    reset_list[3] = "4"
    reset_list[4] = "5"
    reset_list[5] = "6"
    reset_list[6] = "7"
    reset_list[7] = "8"
    reset_list[8] = "9"
    return reset_list


if __name__ == "__main__":
    main()