class Spot:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
