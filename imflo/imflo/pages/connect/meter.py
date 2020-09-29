from array import array
from collections import deque
from random import random
from math import sin
import numpy as np

import arcade
import imgui

from imflo.node import Node
from imflo.pin import Input

class MeterNode(Node):
    def __init__(self, page):
        super().__init__(page)
        #self.values = array('f', [sin(x * 0.1) for x in range(100)])
        self.values = deque([0]*100, 100)
        self.input = Input(self, 'input', self.process)
        self.add_pin(self.input)

    def process(self, value):
        print(value)
        self.values.append(value)
        if len(self.values) > 100:
            self.values.popleft()

    def draw(self):
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
        imgui.plot_lines("Sin(t)", np.array(self.values).astype(np.float32))

        imgui.end()

