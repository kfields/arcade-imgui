import arcade
import imgui
import imgui.core

from imflo.page import Page

from .sine import SineNode
from .scope import ScopeNode

class SinePage(Page):
    def __init__(self, window, name, title):
        super().__init__(window, name, title)
        sine_node = self.add_node(SineNode(self))
        scope_node = self.add_node(ScopeNode(self))
        #self.wires.append(Wire(sine_node.get_pin('output'), scope_node.get_pin('input')))
        
    def update(self, delta_time):
        for node in self.nodes:
            node.update(delta_time)

    def draw(self):
        for node in self.nodes:
            node.draw()

        for wire in self.wires:
            wire.draw()

def install(app):
    app.add_page(SinePage, "sine", "Sine Wave")
