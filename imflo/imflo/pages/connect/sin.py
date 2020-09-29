import time
from math import sin
import numpy as np
from rx.subject import Subject

import arcade
import imgui

from imflo.node import Node
from imflo.pin import Output

sampling_rate = 44100
freq = 440
samples = 44100
#x = np.arange(samples)
#y = 100*np.sin(2 * np.pi * freq * x / sampling_rate)

class SinNode(Node):
    def __init__(self, page):
        super().__init__(page)
        self._value = 88
        self.subject = Subject()
        self.output = Output(self, 'output', self.subject)
        self.add_pin(self.output)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        #self._value = value
        self._value = value
        freq = value
        x = time.time_ns()
        #y = 100*np.sin(2 * np.pi * freq * x / sampling_rate)
        y = 100*np.sin(2 * np.pi * freq * x)
        #self.subject.on_next(value)
        self.subject.on_next(y)

    def draw(self):
        width = 20
        height = 100

        imgui.set_next_window_size(160, 160, imgui.ONCE)

        imgui.begin("Sin")
        changed, self.value = imgui.v_slider_int(
            "freq",
            width, height, self.value,
            min_value=0, max_value=100,
            format="%d"
        )
        imgui.same_line(spacing=16)
        self.mark_output(self.output)
        imgui.button('output')
        if imgui.begin_drag_drop_source():
            imgui.set_drag_drop_payload('itemtype', b'payload')
            self.page.start_dnd(self.output)
            imgui.button('dragged source')
            imgui.end_drag_drop_source()

        imgui.end()

