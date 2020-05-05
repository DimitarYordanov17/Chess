from Figure import Figure


class King(Figure):
    def __init__(self, y, x):
        super().__init__(y, x)
        self.y = y
        self.x = x

        self.coordinates_list = [(y - 1, x - 1), (y - 1, x), (y - 1, x + 1),
                                 (y, x - 1), (y, x + 1),
                                 (y + 1, x - 1), (y + 1, x), (y + 1, x + 1)]

    def __repr__(self):
        return "K"
