import arcade
import imgui
import imgui.core

from imflo.page import Page

from .sin import SinNode
from .meter import MeterNode
from imflo.wire import Wire

class ConnectPage(Page):
    def __init__(self, window, name, title):
        super().__init__(window, name, title)
        self.nodes = []
        self.wires = []
        sin_node = SinNode(self)
        meter_node = MeterNode(self)
        self.nodes.append(sin_node)
        self.nodes.append(meter_node)
        #self.wires.append(Wire(sin_node.get_pin('output'), meter_node.get_pin('input')))

    def connect(self, input, output):
        self.wires.append(Wire(input, output))
        
    def draw(self):
        for node in self.nodes:
            node.draw()

        for wire in self.wires:
            wire.draw()

def install(app):
    app.add_page(ConnectPage, "connect", "Connect")
