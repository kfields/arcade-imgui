class Pin:
    def __init__(self, node, name):
        self.node = node
        self.name = name
        self.x = 0
        self.y = 0

    def set_position(self, pos):
        self.x, self.y = pos

    def get_position(self):
        return (self.x, self.y)

    def draw(self):
        pass

class Input(Pin):
    pass

class Output(Pin):
    pass