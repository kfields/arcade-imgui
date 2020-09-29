import sys

import arcade
import imgui
import imgui.core

from arcade_imgui import ArcadeRenderer

sys.path.append('.')

from imflo.nodes.sin import SinNode
from imflo.nodes.meter import MeterNode
from imflo.wire import Wire

class MyGui:
    def __init__(self, window):
        self.window = window
        # Must create or set the context before instantiating the renderer
        imgui.create_context()
        self.renderer = ArcadeRenderer(window)
        #
        self.nodes = []
        self.wires = []
        sin_node = SinNode()
        meter_node = MeterNode()
        self.nodes.append(sin_node)
        self.nodes.append(meter_node)
        self.wires.append(Wire(sin_node.get_pin('output'), meter_node.get_pin('input')))

    def render(self):
        imgui.new_frame()

        for node in self.nodes:
            node.draw()

        for wire in self.wires:
            wire.draw()

        imgui.end_frame()

        imgui.render()

        self.renderer.render(imgui.get_draw_data())


class App(arcade.Window):
    def __init__(self):
        super().__init__(1024, 768, "ImFlo", resizable=True)
        self.gui = MyGui(self)

    def on_draw(self):
        arcade.start_render()
        self.gui.render()


app = App()
arcade.run()
