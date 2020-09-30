import arcade
import imgui
import imgui.core

from imflo.page import Page

from .volume import VolumeNode
from .led import LedNode
from imflo.wire import Wire

class ConnectPage(Page):
    def __init__(self, window, name, title):
        super().__init__(window, name, title)
        self.nodes = []
        self.wires = []
        volume_node = VolumeNode(self)
        led_node = LedNode(self)
        self.nodes.append(volume_node)
        self.nodes.append(led_node)

    def draw(self):
        for node in self.nodes:
            node.draw()

        for wire in self.wires:
            wire.draw()

def install(app):
    app.add_page(ConnectPage, "connect", "Connect")
