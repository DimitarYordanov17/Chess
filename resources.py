import colored
import random
from Rook import Rook
from Queen import Queen
from Pawn import Pawn
from King import King
from Horse import Horse
from Bishop import Bishop


# Main file to keep all the classes/methods/functions
# 2 modules are here for the improvement of the game

class Table:
    """
    Table class to keep all values in the current game
    """

    def __init__(self):  # Initialized with every chess common setup
        self.enemy_color = None
        self.you_color = None
        self.computer_turn = None
        self.list = [
            [(Rook(0, 0), "enemy"), (Horse(0, 1), "enemy"), ((Bishop(0, 2)), "enemy"), (Queen(0, 3), "enemy"),
             (King(0, 4), "enemy"), (Bishop(0, 5), "enemy"),
             (Horse(0, 6), "enemy"), (Rook(0, 7), "enemy")],
            [(Pawn(1, 0, "enemy"), "enemy"), (Pawn(1, 1, "enemy"), "enemy"), (Pawn(1, 2, "enemy"), "enemy"),
             (Pawn(1, 3, "enemy"), "enemy"), (Pawn(1, 4, "enemy"), "enemy"), (Pawn(1, 5, "enemy"), "enemy"),
             (Pawn(1, 6, "enemy"), "enemy"), (Pawn(1, 7, "enemy"), "enemy")],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [(Pawn(6, 0, "you"), "you"), (Pawn(6, 1, "you"), "you"), (Pawn(6, 2, "you"), "you"),
             (Pawn(6, 3, "you"), "you"), (Pawn(6, 4, "you"), "you"), (Pawn(6, 5, "you"), "you"),
             (Pawn(6, 6, "you"), "you"), (Pawn(6, 7, "you"), "you")],
            [(Rook(7, 0), "you"), (Horse(7, 1), "you"), ((Bishop(7, 2)), "you"), (Queen(7, 3), "you"),
             (King(7, 4), "you"), (Bishop(7, 5), "you"),
             (Horse(7, 6), "you"), (Rook(7, 7), "you")]]

    def visualise(self):  # Visualises the current state (instance list) with colors
        print("    ABCDEFGH\n"
              "    --------")
        if self.you_color == "white":
            counter = 1
        else:
            counter = 0

        row_counter = 8

        for row in self.list:
            print(row_counter, end=" | ")
            for column in row:
                if column != " ":
                    if counter % 2 == 0:
                        if column[1] == "enemy":
                            print(colored.stylize(column[0], colored.fg(self.enemy_color) + colored.bg(94)), end="")
                        else:
                            print(colored.stylize(column[0], colored.fg(self.you_color) + colored.bg(94)), end="")
                    else:
                        if column[1] == "enemy":
                            print(colored.stylize(column[0], colored.fg(self.enemy_color) + colored.bg(136)), end="")
                        else:
                            print(colored.stylize(column[0], colored.fg(self.you_color) + colored.bg(136)), end="")
                else:
                    if counter % 2 == 0:
                        print(colored.stylize(column, colored.bg(94)), end="")
                    else:
                        print(colored.stylize(column, colored.bg(136)), end="")
                counter += 1
            print(" |", end=f" {row_counter}")
            print()
            row_counter -= 1
            counter += 1
        print("    --------\n"
              "    ABCDEFGH\n")

    def introduce(self):  # Describes the game and sets color
        print(f"""
Welcome, after you read this message, you have to choose a color,
if you choose ,,black'' the computer is going to do the first move,
otherwise, you are first. The figure movement is done by you,
entering an input line which consists of:

old coordinates, new coordinates

Examples:
B2 C6
F3 G7
H7 A1

If you have the opportunity to grab the computer's king, just do so! Good luck""")
        color = input("Choose color (black/white):  ")

        if "bl" in color:
            self.enemy_color = "white"
            self.you_color = "black"
        else:
            self.enemy_color = "black"
            self.you_color = "white"

        self.visualise()

    def get_input(self):  # Gets input from player and transforms it into correct coordinates & figure

        input_line = input("Enter old place and new place\n"
                           "e.g. B4 C3  ")

        while len([i for i in input_line if i.isnumeric()]) != 2 or len([i for i in input_line if i.isalpha()]) != 2:
            input_line = input("Incorrect input please enter again\n"
                               "e.g. H4 C8  ")

        if " " in input_line:
            input_line = [i.upper() for i in input_line.split()]
        else:
            input_line = input_line[:2].upper(), input_line[2:].upper()

        old_coordinates = 8 - int(input_line[0][1]), ord(input_line[0][0]) - 65
        new_coordinates = 8 - int(input_line[1][1]), ord(input_line[1][0]) - 65

        return old_coordinates, new_coordinates

    def validate(self, coordinates):  # Validates if a coordinates are in the correct form
        if 0 <= coordinates[0] < len(self.list):
            if 0 <= coordinates[1] < len(self.list[coordinates[0]]):
                return True
        return False

    def do_work(self, old_coordinates, new_coordinates):  # Most of the things happen here
        if not self.validate(old_coordinates):  # Checks for valid coordinates
            if not self.computer_turn:
                print("Invalid coordinates")
            return False

        if self.list[old_coordinates[0]][old_coordinates[1]] == " ":  # Checks if the old move is a figure
            if not self.computer_turn:
                print("Invalid coordinates")
            return False

        old_coordinates_figure = self.list[old_coordinates[0]][
            old_coordinates[1]]  # A tuple with object, type (enemy/you)

        if not old_coordinates_figure[
                   0].__class__.__name__ == "Horse":  # Checks if there is a figure between old and new coordinates (Only if not Horse)
            current_coordinates = old_coordinates

            while current_coordinates != new_coordinates:
                current_y, current_x = current_coordinates[0], current_coordinates[1]

                if current_y < new_coordinates[0]:
                    current_y += 1
                elif current_y > new_coordinates[0]:
                    current_y -= 1

                if current_x < new_coordinates[1]:
                    current_x += 1
                elif current_x > new_coordinates[1]:
                    current_x -= 1

                current_coordinates = current_y, current_x

                if current_coordinates == new_coordinates:
                    if self.list[current_y][current_x] != " ":
                        if self.computer_turn:
                            if self.list[current_y][current_x][1] == "you":
                                break
                        else:
                            if self.list[current_y][current_x][1] == "enemy":
                                break

                if self.list[current_y][current_x] != " ":
                    if not self.computer_turn:
                        print("Invalid coordinates")
                    return False

        if not self.computer_turn and old_coordinates_figure[
            1] == "enemy":  # Checks if the user is trying to move computer's figure
            if not self.computer_turn:
                print("Invalid coordinates")
            return False

        if self.computer_turn:  # Those coordinates are for pawns, especially when attacking a right or left position/figure
            left_coordinate = old_coordinates[0] + 1, old_coordinates[1] - 1
            right_coordinate = old_coordinates[0] + 1, old_coordinates[1] + 1
        else:
            left_coordinate = old_coordinates[0] - 1, old_coordinates[1] - 1
            right_coordinate = old_coordinates[0] - 1, old_coordinates[1] + 1

        if new_coordinates not in old_coordinates_figure[0].coordinates_list:  # Checks if attacking right/left position
            if old_coordinates_figure[0].__class__.__name__ == "Pawn":
                if new_coordinates == left_coordinate or new_coordinates == right_coordinate:
                    if self.list[new_coordinates[0]][new_coordinates[1]] == " ":
                        if not self.computer_turn:
                            print("Invalid coordinates")
                        return False
                else:
                    if not self.computer_turn:
                        print("Invalid coordinates")
                    return False
            else:
                if not self.computer_turn:
                    print("Invalid coordinates")
                return False

        if self.list[new_coordinates[0]][new_coordinates[1]] != " " and \
                self.list[new_coordinates[0]][new_coordinates[1]][1] == old_coordinates_figure[
            1]:  # Checks if trying to catch your figure
            if not self.computer_turn:
                print("Invalid coordinates")
            return False

        if old_coordinates_figure[
            0].__class__.__name__ == "Pawn":  # Pawn's behavior is pretty complex, so there is a whole different case for it
            if self.list[new_coordinates[0]][new_coordinates[1]] != " " and (
                    new_coordinates != left_coordinate and new_coordinates != right_coordinate):
                if not self.computer_turn:
                    print("Invalid coordinates")
                return False

            new_object = Pawn(new_coordinates[0], new_coordinates[1], old_coordinates_figure[1])
            if self.computer_turn:
                new_object.coordinates_list = [(new_object.y + 1, new_object.x)]
            else:
                new_object.coordinates_list = [(new_object.y - 1, new_object.x)]
            self.list[old_coordinates[0]][old_coordinates[1]], self.list[new_coordinates[0]][
                new_coordinates[1]] = " ", (new_object, old_coordinates_figure[1])
        else:  # Other than Pawn figure
            self.list[old_coordinates[0]][old_coordinates[1]], self.list[new_coordinates[0]][
                new_coordinates[1]] = " ", (
                old_coordinates_figure[0].__class__(*new_coordinates), old_coordinates_figure[1])

    def do_work_computer(self):  # Does the random move for the computer
        while True:
            random_figure = random.choice([x[0] for y in self.list for x in y if x != " " and x[1] == "enemy"])  # Gets random computer figure
            random_coordinates = random.choice(random_figure.coordinates_list)  # Gets random coordinates of that figure
            if random_coordinates[0] < 0 or random_coordinates[1] < 0:  # Checks explicitly if the coordinates are valid
                continue
            if self.do_work((random_figure.y, random_figure.x), random_coordinates) is None:  # Checks if a correct move has been done
                break

    def check(self):  # Checks how many kings are there on the table
        kings = [i for i in [x for y in self.list for x in y] if i[0].__repr__() == "K"]

        if len(kings) == 1:  # Only one king case
            if kings[0][1] == "enemy":
                print("You lost!")
            else:
                print("You won!")
            exit()
