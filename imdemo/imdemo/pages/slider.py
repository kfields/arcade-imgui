import arcade
import imgui
import imgui.core

from imdemo.page import Page


class FloatSliderPage(Page):
    def reset(self):
        self.value = 88

    def draw(self):
        width = 20
        height = 100

        imgui.begin(self.title)
        changed, self.value = imgui.v_slider_float(
            "vertical slider float",
            width, height, self.value,
            min_value=0, max_value=100,
            format="%0.3f"
        )
        imgui.text("Changed: %s, Values: %s" % (changed, self.value))
        imgui.end()

class IntSliderPage(Page):
    def reset(self):
        self.value = 88

    def draw(self):
        width = 20
        height = 100

        imgui.begin(self.title)
        changed, self.value = imgui.v_slider_int(
            "vertical slider int",
            width, height, self.value,
            min_value=0, max_value=100,
            format="%d"
        )
        imgui.text("Changed: %s, Values: %s" % (changed, self.value))
        imgui.end()

def install(app):
    app.add_page(FloatSliderPage, "floatslider", "Slider - Float")
    app.add_page(IntSliderPage, "intslider", "Slider - Integer")
