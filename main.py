from resources import Table

table = Table()
table.introduce()  # Introduces the player with the legend

if table.you_color == "white":  # Picks color, depending on it, the turns are selected
    table.computer_turn = False
else:
    table.computer_turn = True

while True:  # Looping till one of the kings die
    if table.computer_turn:  # Computer turn
        table.do_work_computer()
        table.computer_turn = False
        table.visualise()
        continue

    result = table.do_work(*table.get_input())  # Changes the element, with the given input

    while result == False:  # Not correct form, warning is thrown, awaits for new input
        result = table.do_work(*table.get_input())

    table.visualise()  # Visualises the table itself

    if not table.computer_turn:  # Swapping turns
        table.computer_turn = True

    table.check()  # Checks for the kings
