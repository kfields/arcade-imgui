import arcade
import imgui

from imdemo.pages.nodes.node import Node
from imdemo.pages.nodes.pin import Output


class SinNode(Node):
    def __init__(self):
        super().__init__()
        self.value = 88
        self.output = Output(self, 'output')
        self.add_pin(self.output)

    def draw(self):
        width = 20
        height = 100

        imgui.set_next_window_size(160, 160, imgui.ONCE)

        imgui.begin("Sin")
        imgui.begin_group()
        changed, self.value = imgui.v_slider_int(
            "value",
            width, height, self.value,
            min_value=0, max_value=100,
            format="%d"
        )
        imgui.end_group()
        imgui.same_line(spacing=16)
        imgui.begin_group()
        imgui.text('output')
        self.mark_output(self.output)
        imgui.end_group()
        imgui.end()

