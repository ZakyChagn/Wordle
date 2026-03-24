from enum import Enum

class LetterState(Enum):
    Valid = 1
    WrongPlace = 2
    Invalid = 3
    Unknown = 4

    def __str__(self):
        return super().__str__().split(".")[1]

class Letter:
    def __init__(self, symbol):
        self.symbol = symbol
        self.state = LetterState.Unknown
    def __eq__(self, value):
        if (self.symbol == value):
            return True
        else:
            return False
        
    def __str__(self):
        return f"{self.symbol}, {self.state}"
    
    def reset(self):
        self.state = LetterState.Unknown