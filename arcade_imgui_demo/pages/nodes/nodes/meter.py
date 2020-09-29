from array import array
from random import random
from math import sin

import arcade
import imgui

from arcade_imgui_demo.pages.nodes.node import Node
from arcade_imgui_demo.pages.nodes.pin import Input

class MeterNode(Node):
    def __init__(self):
        super().__init__()
        self.values = array('f', [sin(x * 0.1) for x in range(100)])
        self.input = Input(self, 'input')
        self.add_pin(self.input)

    def draw(self):
        #imgui.set_next_window_position(self.window.width - 256 - 16, 32, imgui.ONCE)
        #imgui.set_next_window_size(256, 256, imgui.ONCE)

        imgui.begin("Meter")
        self.mark_input(self.input)
        imgui.text('input')
        imgui.same_line(spacing=16)
        imgui.plot_lines("Sin(t)", self.values)
        imgui.end()

