import arcade
import imgui

from imdemo.page import Page


class Input(Page):
    def reset(self):
        self.test_input = 0

    def draw(self):
        imgui.begin("Test Window")

        imgui.text("This is the test window.")
        changed, self.test_input = imgui.input_int(
            "Integer Input Test", self.test_input
        )

        imgui.end()

        arcade.draw_text(str(self.test_input), 512, 128, arcade.color.WHITE_SMOKE, 64)


class InputDouble(Page):
    def reset(self):
        self.double_val = 3.14159265358979323846

    def draw(self):
        imgui.begin("Test Window")

        imgui.text("This is the test window.")
        changed, self.double_val = imgui.input_double(
            "Type multiplier:", self.double_val
        )
        imgui.text("You wrote: %d" % self.double_val)

        imgui.end()

        arcade.draw_text(str(self.double_val), 512, 128, arcade.color.WHITE_SMOKE, 64)


class InputFloat(Page):
    def reset(self):
        self.float_val = 0.4

    def draw(self):
        imgui.begin("Test Window")

        imgui.text("This is the test window.")
        changed, self.float_val = imgui.input_float("Type coefficient:", self.float_val)
        imgui.text("You wrote: %f" % self.float_val)
        imgui.end()

        arcade.draw_text(str(self.float_val), 512, 128, arcade.color.WHITE_SMOKE, 64)


def install(app):
    app.add_page(Input, "input", "Input")
    app.add_page(InputDouble, "inputdouble", "Input Double")
    app.add_page(InputFloat, "inputfloat", "Input Float")
