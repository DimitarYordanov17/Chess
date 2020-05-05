from Figure import Figure


class Horse(Figure):
    def __init__(self, y, x):
        super().__init__(y, x)
        self.y = y
        self.x = x
        top_left = (self.y - 1, self.x - 2), (self.y - 2, self.x - 1)
        top_right = (self.y - 2, self.x + 1), (self.y - 1, self.x + 2)
        bottom_left = (self.y + 1, self.x - 2), (self.y + 2, self.x - 1)
        bottom_right = (self.y + 2, self.x + 1), (self.y + 1, self.x + 2)
        self.coordinates_list = top_left + top_right + bottom_right + bottom_left

    def __repr__(self):
        return "H"
