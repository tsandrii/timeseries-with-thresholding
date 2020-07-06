from enum import Enum

"""
Enum for the type of position / action: BUY or SELL
"""


class PositionType(Enum):
    BUY = 1
    SHORT = 2


"""
Position / action class
"""


class Position:
    def __init__(self, position_type, amount):
        self.type = position_type
        self.amount = amount
