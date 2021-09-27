# Author:       Tyler Wennstrom
# Date:         May 31, 2021
# Description:  This file contains the source code for three classes that represent the objects needed
#               for a game of Kuba. There are descriptions and classes for Marble, Player, and KubaGame
#               objects.

# %%
class Player:
    """represents a player in a game of Kuba. will communicate with the KubaGame class in order to initialize a Player object and update its private data members (owned_marbles, captured_neutral, captured_opponent, legal_moves)."""

    def __init__(self, name: str, color: str) -> None:
        """takes two parameters, name:string and color:string, in order to create private data members for a new player"""
        self._name = name
        self._color = color
        self._owned_marbles = []
        self._captured_neutral = []
        self._captured_opponent = []
        self._legal_moves = True
        return

    def __repr__(self) -> str:
        """defines the representation of the Player object"""
        return self._name

    def get_name(self) -> str:
        """returns the name of the player"""
        return self._name

    def get_color(self) -> str:
        """returns the color of the player"""
        return self._color

    def get_captured_neutral(self) -> list:
        """returns a list of captured Red Marbles by the Player"""
        return self._captured_neutral

    def get_captured_opponent(self) -> list:
        """returns a list of captured opponent Marbles by the Player"""
        return self._captured_opponent

    def get_owned_marbles(self) -> list:
        """returns the marbles that are owned by the Player"""
        return self._owned_marbles

    def has_legal_moves(self) -> bool:
        """returns False if there are no legal moves for the Player to make, otherwise returns True"""
        return self._legal_moves

    def set_legal_moves(self, state: bool):
        """changes the state of legal moves for the Player"""
        self._legal_moves = state
        return

    def add_captured_neutral(self, captured_marble):
        """adds a neutral Marble to the list of captured neutral Marbles"""
        self._captured_neutral.append(captured_marble)
        return

    def add_captured_opponent(self, captured_marble):
        """adds an opponent Marble to the list of captured opponent Marbles"""
        self._captured_opponent.append(captured_marble)
        return

    def add_owned_marble(self, marble):
        """adds a marble to the ownership of the Player"""
        self._owned_marbles.append(marble)
        return


class Marble:
    """represents a marble in a game of Kuba. will commuincate with the KubaGame class to initialize each Marble object for a new game of Kuba. all private data members of the Marble class will be set and updated by the KubaGame class. KubaGame class will update it's private data members as the game progresses"""

    def __init__(self, color: str, owner, position: tuple) -> None:
        """assigns a color, owner, and position to initialize a marble. colors can only be R, B, or W (corresponding to red, black, or white)"""
        self._color = color
        self._owner = owner
        self._captured = False
        self._position = position
        return

    def __repr__(self) -> str:
        """defines the representation of the Marble object"""
        return self._color

    def get_color(self) -> str:
        """returns the color of the Marble"""
        return self._color

    def get_owner(self) -> Player:
        """returns the owner of the Marble"""
        return self._owner

    def get_position(self) -> tuple:
        """returns the position of the Marble"""
        return self._position

    def set_position(self, position: tuple):
        """upates the position (passed as a tuple) of the Marble"""
        self._position = position
        return

    def is_captured(self) -> bool:
        """returns the captured status of the Marble"""
        return self._captured

    def set_captured(self, status: bool):
        """updates the Marble's captured status"""
        self._captured = status
        return


class KubaGame:
    """represents a game of Kuba, the board game. must commuincate with the Marble and Player classes to get data about each object in the game using its built-in methods. KubaGame class will update all external object data using defined methods."""

    def __init__(self, tuple_1: tuple, tuple_2: tuple) -> None:
        """initializes a new game of Kuba. takes two tuples with parameters: (player name, player color) in order to create new Players and assign colors to them. this method will use these new Player objects to update the list of players and create a new board for the Players."""
        self._player_1 = Player(tuple_1[0], tuple_1[1])
        self._player_2 = Player(tuple_2[0], tuple_2[1])
        self._players = (self._player_1, self._player_2)
        self._marbles = []
        self._status = "UNFINISHED"
        self._current_turn = None
        self._winner = None
        self._reverse_move = None
        self._board = self.make_board()

    def get_player_1(self) -> Player:
        """returns the player_1 object"""
        return self._player_1

    def get_player_2(self) -> Player:
        """returns the player_2 object"""
        return self._player_2

    def get_players(self) -> tuple:
        """returns the current players of the game in a tuple"""
        return self._players

    def get_status(self) -> str:
        """returns the status of the game"""
        return self._status

    def set_status(self, status: str):
        """sets the status of the game"""
        self._status = status
        return

    def get_reverse_move(self):
        """returns the reverse of the last move entered in the game"""
        return self._reverse_move

    def set_reverse_move(self, coordinates: tuple, direction: str):
        """updates the reverse_move private data member with the reverse of the last move played"""
        self._reverse_move = (coordinates, direction)

    def get_winner(self) -> Player:
        """returns the winner of the game"""
        return self._winner

    def get_marbles(self) -> list:
        """returns the list of all marbles in the game"""
        return self._marbles

    def set_winner(self, winner: Player):
        """sets the winner of the game"""
        self._winner = winner
        return

    def get_current_turn(self) -> str:
        """returns the name of the player who currently has the current turn"""
        if self._current_turn == None:
            return None
        else:
            return self._current_turn.get_name()

    def set_current_turn(self, player: Player):
        """updates the current turn of the game to the player passed as parameter"""
        self._current_turn = player
        return

    def get_board(self) -> list:
        """returns the current state of the board as a two-dimensional list"""
        return self._board

    def make_board(self):
        """creates a new board and returns it as a two dimensional list. this board is created for the Players defined in the private data member for the KubaGame. new marbles are also created and assigned to the Players"""

        # creates a two dimensional 7x7 list with "X" in the cells to create an empty board
        board = [["X" for i in range(7)] for j in range(7)]

        # indentify players and set introductory coordinates to fill in board
        player_1 = self.get_player_1()
        player_1_positions = [(0, 0), (0, 1), (1, 0), (1, 1),
                              (5, 5), (5, 6), (6, 5), (6, 6)]
        player_2 = self.get_player_2()
        player_2_positions = [(0, 5), (0, 6), (1, 5), (1, 6),
                              (5, 0), (5, 1), (6, 0), (6, 1)]

        # function for creating and placing marbles for a player to reduce rewritten code
        def create_player_marbles(player, positions):
            """creates new marbles for a player and adds them to the board"""
            for position in positions:
                new_marble = Marble(player.get_color(), player, position)
                player.add_owned_marble(new_marble)
                self._marbles.append(new_marble)
                row = position[0]
                column = position[1]
                board[row][column] = new_marble

        # function to create and place neutral marbles to reduce clutter
        def create_neutral_marbles():
            """creates new neutral marbles for the board"""
            neutral_positions = [(1, 3), (2, 2), (2, 3), (2, 4), (3, 1), (3, 2),
                                 (3, 3), (3, 4), (3, 5), (4, 2), (4, 3), (4, 4), (5, 3)]
            for position in neutral_positions:
                new_marble = Marble("R", None, position)
                self._marbles.append(new_marble)
                row = position[0]
                column = position[1]
                board[row][column] = new_marble

        # call functions to solidify changes in data
        create_player_marbles(player_1, player_1_positions)
        create_player_marbles(player_2, player_2_positions)
        create_neutral_marbles()

        return board

    def print_board(self):
        """prints a representation of the current board state to the console"""
        board = self.get_board()
        for row in board:
            print(" | ", end="")
            for cell in row:
                print(f"{cell}", end=" | ")
            print()
        return

    def validate_move(self, player_name: str, coordinates: tuple, direction: str) -> bool:
        """helper function to validate a move before making a move. takes the same parameters as KubaGame.make_move() and parses through the passed parameters to make sure the move is legal. returns true if move is legal."""

        # check if the game is over
        if self.get_status() == "FINISHED":
            return False                # game is over

        # check if Player name is valid
        players = self.get_players()
        player_names = []
        for each_player in players:
            player_names.append(each_player.get_name().lower())
        if player_name.lower() not in player_names:
            return False                # player name is invalid

        # identify Players
        player = self.get_player_1()
        opponent = self.get_player_2()
        if self.get_player_2().get_name() == player_name:
            opponent = self.get_player_1()
            player = self.get_player_2()

        # check if it is the Player's turn
        if self.get_current_turn() == opponent.get_name():
            return False                # it is the other player's turn

        # check if player has legal moves
        if player.has_legal_moves() == False:
            return False

        # identify cell to move
        row_cood = coordinates[0]
        col_cood = coordinates[1]

        # cell requested is out of range
        if row_cood < 0:
            return False
        if row_cood > 6:
            return False
        if col_cood < 0:
            return False
        if col_cood > 6:
            return False

        # identify Marble
        marble_to_move = self.get_board()[row_cood][col_cood]
        if marble_to_move == "X":
            return False                # the cell is empty

        # Check if Player owns Marble
        if marble_to_move.get_owner() == opponent:
            return False                # Marble belongs to the opponent

        # identify coordinate behind Marble
        row_cood_behind = row_cood
        col_cood_behind = col_cood
        if direction.lower() == "r":
            col_cood_behind -= 1
        elif direction.lower() == "l":
            col_cood_behind += 1
        elif direction.lower() == "f":
            row_cood_behind += 1
        elif direction.lower() == "b":
            row_cood_behind -= 1
        else:
            return False                # direction is invalid

        # check if move requested is a reverse move
        if self.get_reverse_move() == (coordinates, direction.upper()):
            return False

        # check if the coordinate behind is empty
        while True:
            if row_cood_behind < 0:
                break
            if row_cood_behind > 6:
                break
            if col_cood_behind < 0:
                break
            if col_cood_behind > 6:
                break
            if self.get_board()[row_cood_behind][col_cood_behind] == "X":
                break
            return False

        # all checks have passed
        return True

    def make_move(self, player_name: str, coordinates: tuple, direction: str) -> bool:
        """makes a move requested by the player identified as playername. the coordinates of the marble correspond with the marble requested to move. the only possible legal directions are: L, R, F, or B (corresponding with left, right, forward, or backward respectively). will  update Marble positions as needed by updating both the private Marble data member and the board two-dimensional array. Returns True if the move has been executed; otherwise it returns False to indicate an illegal move."""

        # validate move
        valid_move = self.validate_move(player_name, coordinates, direction)
        if valid_move == False:
            # print("Sorry this is an invalid move. Try again.")
            return False

        def next_coordinate(orignal_coordinate: tuple, direction_req: str) -> tuple:
            """given a starting coordinate and direction, will return the next coordinate requested"""

            original_row = orignal_coordinate[0]
            original_col = orignal_coordinate[1]
            new_row = original_row
            new_col = original_col

            # determine new coordinates for Marble
            if direction_req.lower() == "l":
                new_col -= 1
            if direction_req.lower() == "r":
                new_col += 1
            if direction_req.lower() == "f":
                new_row -= 1
            if direction_req.lower() == "b":
                new_row += 1

            return (new_row, new_col)

        # moves a singular Marble on the board
        def move_marble(marble: Marble, dir: str) -> Marble:
            """this function will move one Marble in a particular direction on the board. If the move requested moves the Marble off of the board, then that Marble will be returned"""

            # initialize ID variables
            board = self.get_board()
            cell = marble.get_position()
            original_row = cell[0]
            original_col = cell[1]
            new_row = next_coordinate(cell, dir)[0]
            new_col = next_coordinate(cell, dir)[1]

            # replace current cell with "X"
            board[original_row][original_col] = "X"

            # determine if Marble is captured
            if new_col < 0:
                return marble
            if new_col > 6:
                return marble
            if new_row < 0:
                return marble
            if new_row > 6:
                return marble

            # otherwise, place marble in new location
            board[new_row][new_col] = marble
            marble.set_position((new_row, new_col))
            return None

        # identify player object
        current_player = self.get_player_1()
        opponent_player = self.get_player_2()
        if player_name == self.get_player_2().get_name():
            current_player = self.get_player_2()
            opponent_player = self.get_player_1()

        # identify block of Marbles to move, and store in an array
        board = self.get_board()
        marble_present = True
        current_coordinate = coordinates
        block_of_marbles = [board[coordinates[0]][coordinates[1]]]
        while marble_present == True:
            current_coordinate = next_coordinate(current_coordinate, direction)
            if current_coordinate[0] not in (0, 1, 2, 3, 4, 5, 6):
                break
            if current_coordinate[1] not in (0, 1, 2, 3, 4, 5, 6):
                break
            next_marble = board[current_coordinate[0]][current_coordinate[1]]
            if next_marble == "X":
                marble_present = False
            else:
                block_of_marbles.append(next_marble)

        # move marbles, starting from the last marble
        rev_block_marbles = block_of_marbles[::-1]
        captured = False    # will be updated to True if a Marble is captured
        for each_marble in rev_block_marbles:
            captured_marble = move_marble(each_marble, direction)
            if captured_marble != None:

                # check if captured marble is owned by current player
                if captured_marble.get_owner() == current_player:
                    false_marble_coods = captured_marble.get_position()
                    board[false_marble_coods[0]
                          ][false_marble_coods[1]] = captured_marble
                    # print("Sorry this is an invalid move. Try again.")
                    return False

                captured_marble.set_captured(True)
                captured_marble.set_position((-1, -1))
                if captured_marble.get_color().lower() == "r":
                    current_player.add_captured_neutral(captured_marble)
                    captured = True
                else:
                    current_player.add_captured_opponent(captured_marble)
                    captured = True

        # set reverse move
        if captured == False:
            rev_coordinates = rev_block_marbles[0].get_position()
            rev_direction = direction
            if rev_direction.lower() == "l":
                rev_direction = "R"
            elif rev_direction.lower() == "r":
                rev_direction = "L"
            elif rev_direction.lower() == "f":
                rev_direction = "B"
            else:
                rev_direction = "F"
            self.set_reverse_move(rev_coordinates, rev_direction)

        # determine if the game is over
        game_over = self.game_over_check()
        if game_over == True:
            winner = self.get_winner()
            loser = self.get_player_1()
            if winner == self.get_player_1():
                loser = self.get_player_2()
            # print()
            # self.print_board()
            # print()
            # print(
                # f"Game Over! {winner} has won! Sorry, {loser}, better luck next time.")
            return True
        else:
            self.set_current_turn(opponent_player)
            # print()
            # self.print_board()
            return True

    def game_over_check(self):
        """checks the status of the board and updates all data objects of the current state of the game. returns True if the game is over"""

        def player_wins(winning_player: Player, losing_player: Player):
            """function to update Player data and game data to reflect a win"""

            self.set_status("FINISHED")
            self.set_winner(winning_player)
            self.set_current_turn(None)
            winning_player.set_legal_moves(False)
            losing_player.set_legal_moves(False)

            return

        def marble_check(marble: Marble) -> bool:
            """checks a marble to see if there are any available legal moves. returns True if a marble has legal moves available"""

            # get data on the Marble
            board = self.get_board()
            marble_cood = marble.get_position()

            # check L move
            if marble_cood[1] == 6:
                return True
            if board[marble_cood[0]][marble_cood[1] + 1] == "X":
                return True

            # check R move
            if marble_cood[1] == 0:
                return True
            if board[marble_cood[0]][marble_cood[1] - 1] == "X":
                return True

            # check F move
            if marble_cood[0] == 6:
                return True
            if board[marble_cood[0] + 1][marble_cood[1]] == "X":
                return True

            # check B move
            if marble_cood[0] == 0:
                return True
            if board[marble_cood[0] - 1][marble_cood[1 - 1]] == "X":
                return True

            # no legal moves found
            return False

        # check if a player has captured 7 neutral stones or all opponent stones
        player_1 = self.get_player_1()
        player_2 = self.get_player_2()
        num_player_1_neutrals = 0
        num_player_1_opponents = 0
        num_player_2_neutrals = 0
        num_player_2_opponents = 0
        for neutral in player_1.get_captured_neutral():
            num_player_1_neutrals += 1
        for opponent in player_1.get_captured_opponent():
            num_player_1_opponents += 1
        for neutral in player_2.get_captured_neutral():
            num_player_2_neutrals += 1
        for opponent in player_2.get_captured_opponent():
            num_player_2_opponents += 1

        if num_player_1_opponents == 8:
            player_wins(player_1, player_2)
            return True
        if num_player_1_neutrals == 7:
            player_wins(player_1, player_2)
            return True
        if num_player_2_opponents == 8:
            player_wins(player_2, player_1)
            return True
        if num_player_2_neutrals == 7:
            player_wins(player_2, player_1)
            return True

        # check if a player has no legal moves left
        player_1_legal = 0
        player_2_legal = 0
        for marble in player_1.get_owned_marbles():
            if marble.is_captured():
                pass
            else:
                if marble_check(marble) == True:
                    player_1_legal += 1
        for marble in player_2.get_owned_marbles():
            if marble.is_captured():
                pass
            else:
                if marble_check(marble) == True:
                    player_2_legal += 1
        if player_1_legal == 0:
            player_wins(player_2, player_1)
            return True
        if player_2_legal == 0:
            player_wins(player_1, player_2)
            return True

        # else, the game is not over
        return False

    def get_captured(self, playername: str) -> int:
        """returns the number of red marbles captured by the player. takes a Player name as a parameter to identify the Player in question"""

        player = self.get_player_1()
        if playername == self.get_player_2().get_name():
            player = self.get_player_2()
        captured_neutrals = player.get_captured_neutral()
        qty_neutral_marbles = 0
        for marble in captured_neutrals:
            qty_neutral_marbles += 1
        return qty_neutral_marbles

    def get_marble(self, coordinates: tuple) -> str:
        """returns the marble currently present in the coordinate passed. returns "X" if no marble is present in the requested cell"""
        row = coordinates[0]
        col = coordinates[1]
        if row not in [0, 1, 2, 3, 4, 5, 6]:
            return "X"
        if col not in [0, 1, 2, 3, 4, 5, 6]:
            return "X"
        board = self.get_board()
        marble = board[row][col]
        if marble == "X":
            return marble
        marble_color = marble.get_color()
        return marble_color

    def get_marble_count(self) -> tuple:
        """returns the number of white marbles, black marbles, and red marbles remaining on the board as a tuple in order (W, B, R)"""
        white = 0
        black = 0
        red = 0
        for marble in self.get_marbles():
            if marble.get_color() == "W" and marble.is_captured() == False:
                white += 1
            if marble.get_color() == "B" and marble.is_captured() == False:
                black += 1
            if marble.get_color() == "R" and marble.is_captured() == False:
                red += 1
        return (white, black, red)
