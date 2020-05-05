from Figure import Figure


class Rook(Figure):
    def __init__(self, y, x):
        super().__init__(y, x)
        self.y = y
        self.x = x
        horizontal_coordinates = [(self.y, x) for x in range(8) if x != self.x]
        vertical_coordinates = [(y, self.x) for y in range(8) if y != self.y]
        self.coordinates_list = horizontal_coordinates + vertical_coordinates

    def __repr__(self):
        return "R"
