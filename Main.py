
# Ultimate Battleships

def print_ships_to_be_placed():
    print("Ships to be placed:", end=" ")

# elem expected to be a single list element of a primitive type.
def print_single_element(elem):
    print(str(elem), end=" ")


def print_empty_line():
    print()


# n expected to be str or int.
def print_player_turn_to_place(n):
    print("It is Player {}'s turn to place their ships.".format(n))


def print_to_place_ships():
    print("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) :", end=" ")


def print_incorrect_input_format():
    print("Input is in incorrect format, please try again.")


def print_incorrect_coordinates():
    print("Incorrect coordinates given, please try again.")


def print_incorrect_ship_name():
    print("Incorrect ship name given, please try again.")


def print_incorrect_orientation():
    print("Incorrect orientation given, please try again.")


# ship expected to be str.
def print_ship_is_already_placed(ship):
    print(ship, "is already placed, please try again.")


# ship expected to be str.
def print_ship_cannot_be_placed_outside(ship):
    print(ship, "cannot be placed outside the board, please try again.")


# ship expected to be str.
def print_ship_cannot_be_placed_occupied(ship):
    print(ship, "cannot be placed to an already occupied space, please try again.")


def print_confirm_placement():
    print("Confirm placement Y/N :", end=" ")


# n expected to be str or int.
def print_player_turn_to_strike(n):
    print("It is Player {}'s turn to strike.".format(n))


def print_choose_target_coordinates():
    print("Choose target coordinates :", end=" ")


def print_miss():
    print("Miss.")


# n expected to be str or int.
def print_type_done_to_yield(n):
    print("Type done to yield your turn to player {} :".format(n), end=" ")


def print_tile_already_struck():
    print("That tile has already been struck. Choose another target.")


def print_hit():
    print("Hit!")


# n expected to be str or int.
def print_player_won(n):
    print("Player {} has won!".format(n))


def print_thanks_for_playing():
    print("Thanks for playing.")

# my_list expected to be a 3-dimensional list, formed from two 2-dimensional lists containing the boards of each player.
def print_3d_list(my_list):
    first_d = len(my_list[0])
    for row_ind in range(first_d):
        second_d = len(my_list[0][row_ind])
        print("{:<2}".format(row_ind+1), end=' ')
        for col_ind in range(second_d):
            print(my_list[0][row_ind][col_ind], end=' ')
        print("\t\t\t", end='')
        print("{:<2}".format(row_ind+1), end=' ')
        for col_ind in range(second_d):
            print(my_list[1][row_ind][col_ind], end=' ')
        print()
    print("", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\t\t", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\nPlayer 1\t\t\t\t\t\tPlayer 2")
    print()


def print_rules():
    print("Welcome to Ultimate Battleships")
    print("This is a game for 2 people, to be played on two 10x10 boards.")
    print("There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).")
    print("First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.")
    print("Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.")
    print("If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.")
    print("If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.")
    print("Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.")
    print("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.")
    print("The last player to have an unsunk ship wins.")
    print("Have fun!")
    print()


# Create the game
board_size = 10
print_rules()


# PLACEMENT PHASE
# Initiating boards and ships for both players.
# boards is a 4d list. 4th dimension exist because p1 can't see p2's board and vice versa. This means:
# boards[0] ===> boards visible to P1                  # boards[1] ===> boards visible to P2
# boards[0][0] ===> P1's board that is visible to P1   # boards[0][1] ===> P2's board that is visible to P1
# boards[1][0] ===> P1's board that is visible to P2   # boards[1][1] ===> P2's board that is visible to P2
boards = [[[["-" for x in range(10)]for y in range(10)] for z in range(2)] for t in range(2)]
# remaining_ships is list of dictionaries. Keys are ship names and values are ship lengths.
# There are 2 dictionaries in this list because there are 2 players
remaining_ships = [{"Carrier": 5, "Battleship": 4, "Cruiser": 3, "Submarine": 3, "Destroyer": 2} for i in range(2)]
# This list is created to ensure placed ship cannot be placed again. This is a 2d list because there are 2 players
placed_ships = [[] for i in range(2)]
# This for loop switches to P2 when P1 done placing. a=0 means P1. a=1 means P2.
for a in range(2):
    # If player says 'n' to confirm placement then sequence under this loop will be executed again without changing player
    while True:
        # When there is no ship left to place for player it will exit this loop and ask for confirmation
        while remaining_ships[a] != {}:
            # Printing boards that is visible to that player
            print_3d_list(boards[a])
            # Prints available ships and necessary print statements to player
            print_ships_to_be_placed()
            for i in remaining_ships[a]:
                print_single_element(i)
            print_empty_line()
            print_player_turn_to_place(a + 1)
            print_to_place_ships()
            # Takes ship, coordinates and orientation input as a list
            ship_input = input().split()
            # Ship input case insensitivity
            ship_input[0] = ship_input[0].capitalize()

            # ERROR CHECKS
            # If an error occurs during any of these error checks program will continue the loop and ask for input again
            # Checks if there are enough inputs.
            if len(ship_input) < 4:
                print_incorrect_input_format()
                continue
            # Checks if ship name format is correct
            try:
                # If ship name input can't be converted into float this means it is a string
                # Code will go to exception part and will pass that part because it is an exception that we want
                checker = float(ship_input[0])
                if type(checker) == float:
                    print_incorrect_input_format()
                    continue
            except:
                pass
            # Checks if coordinate format is correct then checks if coordinates are within the board
            try:
                # If it can't be converted to integer it means format is wrong. It will give an ValueError
                x = int(ship_input[1]) - 1
                y = int(ship_input[2]) - 1
                # If coordinates are integers this if block checks if they are within the board
                if x < 0 or y < 0:
                    print_incorrect_coordinates()
                    continue
                if x > 9 or y > 9:
                    print_incorrect_coordinates()
                    continue
            except ValueError:
                print_incorrect_input_format()
                continue
            # Checks if ship name is correct. If not it will give an KeyError for the remaining_ships dictionary
            if ship_input[0] not in placed_ships[a]:
                try:
                    checker = remaining_ships[a][ship_input[0]]
                except KeyError:
                    print_incorrect_ship_name()
                    continue
            # Checks if orientation is valid
            if ship_input[3].lower() != "h" and ship_input[3].lower() != "v":
                print_incorrect_orientation()
                continue
            # Checks if ship is already placed
            if ship_input[0] in placed_ships[a]:
                print_ship_is_already_placed(ship_input[0])
                continue
            # Checks if ship goes out of bounds during placement
            try:
                # This is the same code for the This is the same code for the placement of ships except for one thing. except for one thing.
                # It will iterate through tiles that ship will be placed.
                # But it will not change that tile to '#' because it could be invalid input
                # If it goes out of bounds at some point in iteration it will give and IndexError
                if ship_input[3].lower() == "h":
                    for i in range(remaining_ships[a][ship_input[0]]):
                        checker = boards[a][a][y][x + i]
                if ship_input[3].lower() == "v":
                    for i in range(remaining_ships[a][ship_input[0]]):
                        checker = boards[a][a][y + i][x]
            except IndexError:
                print_ship_cannot_be_placed_outside(ship_input[0])
                continue
            # Checks if given coordinates overlap with another ship. A flag is set to False at the beginning
            # It will iterate through tiles that ship will be placed. If any of the tile is '#' it will set the flag to True
            # If flag is True it prints tile already occupied and ask for input again
            check_overlap = False
            if ship_input[3].lower() == "h":
                for i in range(remaining_ships[a][ship_input[0]]):
                    if boards[a][a][y][x + i] == "#":
                        check_overlap = True
                        break
            if ship_input[3].lower() == "v":
                for i in range(remaining_ships[a][ship_input[0]]):
                    if boards[a][a][y + i][x] == "#":
                        check_overlap = True
                        break
            if check_overlap:
                print_ship_cannot_be_placed_occupied(ship_input[0])
                continue

            # PLACING THE SHIP
            # If the while loop came to this point it means input is valid so we can place the ship
            # Places the ship if the orientation is horizontal
            if ship_input[3].lower() == "h":
                # Range is the length of the ship
                # It will start iterating with given coordinate and will increase x coordinate with each iteration
                # During each iteration the tile will be changed to '#'
                for i in range(remaining_ships[a][ship_input[0]]):
                    boards[a][a][y][x + i] = "#"
            # Places the ship if the orientation is vertical
            if ship_input[3].lower() == "v":
                # Range is the length of the ship
                # It will start iterating with given coordinate and will increase y coordinate with each iteration
                # During each iteration the tile will be changed to '#'
                for i in range(remaining_ships[a][ship_input[0]]):
                    boards[a][a][y + i][x] = "#"
            # Remove placed ship from remaining ships and append it to placed ships for upcoming loops
            placed_ships[a].append(ship_input[0])
            remaining_ships[a].pop(ship_input[0])

        # When code comes to this point it means there is no ship left to place for that player and will ask for confirmation
        # Printing last state of the board before asking for confirmation
        print_3d_list(boards[a])
        # Asks confirmation. If input is invalid it will repeatedly ask
        while True:
            print_confirm_placement()
            confirmation = input().strip().lower()
            if confirmation == "n" or confirmation == "y":
                break
        # If placement is not confirmed then player's board and ships will be reset.
        # And will not break outermost while loop so it is still same player's turn
        if confirmation == "n":
            boards[a] = [[["-" for i in range(10)] for j in range(10)] for k in range(2)]
            remaining_ships[a] = {"Carrier": 5, "Battleship": 4, "Cruiser": 3, "Submarine": 3, "Destroyer": 2}
            placed_ships[a] = []
        # If placement is confirmed program will break while loop and go to next iteration of for loop (next player)
        # If there is no iteration left in the for loop then program will move on to action phase
        elif confirmation == "y":
            break

# ACTION PHASE
# If continue_game==False then game is over
continue_game = True
# a variable switches between players. 0 is P1, 1 is P2. It starts with P1
a = 0
# Loop for the action phase
while continue_game:
    # GAME OVER CHECK
    # Before the for loop flag is set to false so if there isn't '#' left in the P1's board, game is over and loop breaks.
    continue_game = False
    for i in boards[0][0]:
        # If there is '#' in P1'board this means P1 has not lost. But we must still check P2's board
        if "#" in i:
            continue_game = True
    # If continue_game is false at this point it means P2 has won and loop will break. p1_won=False means P1 lost
    if not continue_game:
        p1_won = False
        break
    # Before the for loop flag has to be set to false again. If there isn't '#' left in the P2's board, game is over and loop breaks.
    continue_game = False
    for i in boards[1][1]:
        # If there is '#' in P2'board this means P2 has not lost. Since P1 has not lost either game will continue
        if "#" in i:
            continue_game = True
    # If continue_game is false at this point it means P1 has won.
    if not continue_game:
        p1_won = True
        break

    # Program checked if the game is over above. When code comes to this point then game is not over yet
    # Prints board visible to player and necessary texts
    print_3d_list(boards[a])
    print_player_turn_to_strike(a + 1)
    print_choose_target_coordinates()
    # Takes coordinates as input
    coordinates = input().split()

    # ERROR CHECKS
    # Checks if there are enough inputs
    if len(coordinates) < 2:
        print_incorrect_input_format()
        continue
    # Checks if coordinate format is correct then checks if coordinates are within the board
    try:
        # If it can't be converted to integer it means format is wrong. It will give an ValueError
        x = int(coordinates[0]) - 1
        y = int(coordinates[1]) - 1
        # If coordinates are integers this if block checks if they are within the board
        if x < 0 or y < 0:
            print_incorrect_coordinates()
            continue
        if x > 9 or y > 9:
            print_incorrect_coordinates()
            continue
    except ValueError:
        print_incorrect_input_format()
        continue

    # HIT PHASE
    # P1's turn and successful hit
    if a == 0 and boards[1][1][y][x] == "#":
        # If P1 does a successful hit then:
        # P2's board visible to P1 changes
        boards[0][1][y][x] = "!"
        # P2's board visible to P2 changes
        boards[1][1][y][x] = "!"
        print_hit()
        # It's still P1's turn so while loop continues
        continue
    # P1's turn and miss
    if a == 0 and boards[1][1][y][x] == "-":
        # If P1 misses then:
        # P2's board visible to P1 changes
        boards[0][1][y][x] = "O"
        # P2's board visible to P2 changes
        boards[1][1][y][x] = "O"
        print_miss()
        # This loop asks to yield until valid input
        while True:
            print_type_done_to_yield(2)
            yielding = input().strip().lower()
            if yielding == "done":
                break
        # Switches to P2 and continues next loop
        a = 1
        continue
    # P1's turn and tile already struck
    if (a == 0 and boards[1][1][y][x] == "O") or (a == 0 and boards[1][1][y][x] == "!"):
        print_tile_already_struck()
        # It's still P1's turn and no changes made to boards
        continue
    # P2's turn and successful hit
    if a == 1 and boards[0][0][y][x] == "#":
        # If P2 does a successful hit then:
        # P1's board visible to P2 changes
        boards[1][0][y][x] = "!"
        # P1's board visible to P1 changes
        boards[0][0][y][x] = "!"
        print_hit()
        # It's still P2's turn so while loop continues
        continue
    # P2's turn and miss
    if a == 1 and boards[0][0][y][x] == "-":
        # If P2 misses then:
        # P1's board visible to P2 changes
        boards[1][0][y][x] = "O"
        # P1's board visible to P1 changes
        boards[0][0][y][x] = "O"
        print_miss()
        # This loop asks to yield until valid input
        while True:
            print_type_done_to_yield(1)
            yielding = input().strip().lower()
            if yielding == "done":
                break
        # Switches to P1 and continues next loop
        a = 0
        continue
    # P2's turn and tile already struck
    if (a == 1 and boards[0][0][y][x] == "O") or (a == 1 and boards[0][0][y][x] == "!"):
        print_tile_already_struck()
        # It's still P2's turn and no changes made to boards
        continue
# When program got out of while loop that means game is over
# If p1_won == True that means P1 has won. If it is false then P2 has won.
if p1_won:
    # Printing boards visible to P1
    print_3d_list(boards[0])
    print_player_won(1)
    print_thanks_for_playing()
else:
    # Printing boards visible to P2
    print_3d_list(boards[1])
    print_player_won(2)
    print_thanks_for_playing()

