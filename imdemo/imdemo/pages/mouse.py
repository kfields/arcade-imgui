import imgui

from imdemo.page import Page


class MousePage(Page):
    def draw(self):
        imgui.begin(self.title)

        #imgui.text(str(imgui.is_mouse_down(0)))
        imgui.label_text(str(imgui.get_mouse_pos()), "position")
        imgui.label_text(str(imgui.is_mouse_down(0)), "left button")
        imgui.label_text(str(imgui.is_mouse_down(1)), "right button")
        imgui.label_text(str(imgui.is_mouse_down(2)), "middle button")

        imgui.end()

def install(app):
    app.add_page(MousePage, "mouse", "Mouse")
