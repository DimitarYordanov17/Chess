from Figure import Figure


class Pawn(Figure):
    def __init__(self, y, x, player_type="enemy"):
        super().__init__(y, x)
        self.first_time = True
        self.y = y
        self.x = x
        self.player_type = player_type
        self.coordinates_list = []
        if self.first_time:
            if player_type == "enemy":
                self.coordinates_list = [(y + 1, x), (y + 2, x)]
            else:
                self.coordinates_list = [(y - 1, x), (y - 2, x)]
        else:
            if player_type == "enemy":
                self.coordinates_list = [(y + 1, x)]
            else:
                self.coordinates_list = [(y - 1, x)]

    def __repr__(self):
        return "P"
