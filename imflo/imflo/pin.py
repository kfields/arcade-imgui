class Pin:
    def __init__(self, node, name):
        self.node = node
        self.name = name
        self.wires = []
        self.x = 0
        self.y = 0

    def add_wire(self, wire):
        self.wires.append(wire)

    def set_position(self, pos):
        self.x, self.y = pos

    def get_position(self):
        return (self.x, self.y)

    def draw(self):
        pass

class Input(Pin):
    def __init__(self, node, name, action):
        super().__init__(node, name)
        self.action = action

    def add_wire(self, wire):
        super().add_wire(wire)
        wire.output.observable.subscribe(self.action)

class Output(Pin):
    def __init__(self, node, name, observable):
        super().__init__(node, name)
        self.observable = observable
