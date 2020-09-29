import arcade
import imgui

from imflo.node import Node
from imflo.pin import Output

class SinNode(Node):
    def __init__(self, page):
        super().__init__(page)
        self.value = 88
        self.output = Output(self, 'output')
        self.add_pin(self.output)

    def draw(self):
        width = 20
        height = 100

        imgui.set_next_window_size(160, 160, imgui.ONCE)

        imgui.begin("Sin")
        self.mark_output(self.output)
        changed, self.value = imgui.v_slider_int(
            "output",
            width, height, self.value,
            min_value=0, max_value=100,
            format="%d"
        )
        imgui.end()

