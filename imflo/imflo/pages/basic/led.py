from array import array
from random import random
from math import sin

import arcade
import imgui

from imflo.node import Node
from imflo.pin import Input

class LedNode(Node):
    def __init__(self, page):
        super().__init__(page)
        self.value = 0
        self.input = Input(self, 'input', self.process)
        self.add_pin(self.input)

    def process(self, value):
        self.value = value

    def draw(self):
        #imgui.set_next_window_position(self.window.width - 256 - 16, 32, imgui.ONCE)
        #imgui.set_next_window_size(256, 256, imgui.ONCE)

        imgui.begin("Led")
        self.mark_input(self.input)
        imgui.text('input')
        imgui.same_line(spacing=16)
        imgui.text(str(self.value))
        imgui.end()

