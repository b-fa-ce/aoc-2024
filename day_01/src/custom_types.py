datalist = list[int]

class UnequalLengthError(Exception):
    def __init__(self, message):
        self.message = message
