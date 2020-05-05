from abc import ABC, abstractmethod


class Figure(ABC):
    """
    Abstract class for all the figures
    """
    @abstractmethod
    def __init__(self, y, x):
        self.y = y
        self.x = x
