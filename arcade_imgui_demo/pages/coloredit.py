import arcade
import imgui
import imgui.core

from arcade_imgui_demo.page import Page


class ColorEdit3(Page):
    def __init__(self, window):
        super().__init__(window, "coloredit3", "Color Edit 3")
        self.color_1 = 1., .0, .5
        self.color_2 = 0., .8, .3

    def on_render(self):
        imgui.begin("Example: color edit without alpha")

        # note: first element of return two-tuple notifies if the color was changed
        #       in currently processed frame and second element is current value
        #       of color
        changed, self.color_1 = imgui.color_edit3("Color 1", *self.color_1)
        changed, self.color_2 = imgui.color_edit3("Color 2", *self.color_2)

        imgui.end()

class ColorEdit4(Page):
    def __init__(self, window):
        super().__init__(window, "coloredit4", "Color Edit 4")
        self.color = 1., .0, .5, 1.

    def on_render(self):
        imgui.begin("Example: color edit with alpha")

        # note: first element of return two-tuple notifies if the color was changed
        #       in currently processed frame and second element is current value
        #       of color and alpha
        _, self.color = imgui.color_edit4("Alpha", *self.color, show_alpha=True)
        _, self.color = imgui.color_edit4("No alpha", *self.color, show_alpha=False)

        imgui.end()

def install(app):
    app.add_page(ColorEdit3(app))
    app.add_page(ColorEdit4(app))
