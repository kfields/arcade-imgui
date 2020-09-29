from rx.subject import Subject

import arcade
import imgui

from imflo.node import Node
from imflo.pin import Output

class VolumeNode(Node):
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
        self._value = value
        self.subject.on_next(value)

    def draw(self):
        width = 20
        height = 100

        imgui.set_next_window_size(160, 160, imgui.ONCE)

        imgui.begin("Volume")
        self.mark_output(self.output)
        changed, self.value = imgui.v_slider_int(
            "output",
            width, height, self.value,
            min_value=0, max_value=100,
            format="%d"
        )
        imgui.end()

