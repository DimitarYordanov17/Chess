from Figure import Figure


class Bishop(Figure):
    def __init__(self, y, x):
        super().__init__(y, x)
        self.y = y
        self.x = x
        self.coordinates_list = []

        for y in range(8):
            for x in range(8):
                if y - x == self.y - self.x or y + x == self.y + self.x:
                    self.coordinates_list.append((y, x))

    def __repr__(self):
        return "B"
