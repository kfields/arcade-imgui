from array import array
from random import random
from math import sin

import arcade
import imgui

import imflo.dnd as dnd
from imflo.node import Node
from imflo.pin import Input

class MeterNode(Node):
    def __init__(self, page):
        super().__init__(page)
        self.values = array('f', [sin(x * 0.1) for x in range(100)])
        self.input = Input(self, 'input')
        self.add_pin(self.input)


    def draw(self):
        #imgui.set_next_window_position(self.window.width - 256 - 16, 32, imgui.ONCE)
        #imgui.set_next_window_size(256, 256, imgui.ONCE)

        imgui.begin("Meter")
        self.mark_input(self.input)
        imgui.button('input')
        if imgui.begin_drag_drop_target():
            payload = imgui.accept_drag_drop_payload('itemtype')
            if payload is not None:
                payload = self.page.end_dnd()
                print('Received:', payload)
                self.page.connect(self.input, payload)
            imgui.end_drag_drop_target()

        imgui.same_line(spacing=16)
        imgui.plot_lines("Sin(t)", self.values)

        imgui.end()

