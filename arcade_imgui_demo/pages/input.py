import arcade
import imgui
import imgui.core

import arcade
import imgui
import imgui.core

from arcade_imgui_demo.page import Page


class Input(Page):
    def __init__(self, window):
        super().__init__(window, "input", "Input")
        self.test_input = 0

    def on_render(self):
        imgui.begin("Test Window")

        imgui.text("This is the test window.")
        changed, self.test_input = imgui.input_int("Integer Input Test", self.test_input)

        imgui.end()

        arcade.draw_text(str(self.test_input), 512, 128, arcade.color.WHITE_SMOKE, 64)

class InputDouble(Page):
    def __init__(self, window):
        super().__init__(window, "inputdouble", "Input Double")
        self.double_val = 3.14159265358979323846

    def on_render(self):
        imgui.begin("Test Window")

        imgui.text("This is the test window.")
        changed, self.double_val = imgui.input_double('Type multiplier:', self.double_val)
        imgui.text('You wrote: %d' % self.double_val)

        imgui.end()

        arcade.draw_text(str(self.double_val), 512, 128, arcade.color.WHITE_SMOKE, 64)

class InputFloat(Page):
    def __init__(self, window):
        super().__init__(window, "inputfloat", "Input Float")
        self.float_val = 0.4

    def on_render(self):
        imgui.begin("Test Window")

        imgui.text("This is the test window.")
        changed, self.float_val = imgui.input_float('Type coefficient:', self.float_val)
        imgui.text('You wrote: %f' % self.float_val)
        imgui.end()

        arcade.draw_text(str(self.float_val), 512, 128, arcade.color.WHITE_SMOKE, 64)

def install(app):
    app.add_page(Input(app))
    app.add_page(InputDouble(app))
    app.add_page(InputFloat(app))
