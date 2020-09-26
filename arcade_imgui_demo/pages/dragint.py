import arcade
import imgui
import imgui.core

from arcade_imgui_demo.page import Page


class DragInt(Page):
    def __init__(self, window):
        super().__init__(window, "dragint", "Drag Integer")
        self.value = 42

    def on_render(self):
        imgui.begin("Example: drag int")
        changed, self.value = imgui.drag_int("drag int", self.value,)
        imgui.text("Changed: %s, Value: %s" % (changed, self.value))
        imgui.end()

class DragInt2(Page):
    def __init__(self, window):
        super().__init__(window, "dragint2", "Drag Integer 2")
        self.values = 88, 42

    def on_render(self):
        imgui.begin("Example: drag int 2")
        changed, self.values = imgui.drag_int2(
            "drag ints", *self.values
        )
        imgui.text("Changed: %s, Values: %s" % (changed, self.values))
        imgui.end()

class DragInt3(Page):
    def __init__(self, window):
        super().__init__(window, "dragint3", "Drag Integer 3")
        self.values = 88, 42, 69

    def on_render(self):
        imgui.begin("Example: drag int 3")
        changed, self.values = imgui.drag_int3(
            "drag ints", *self.values
        )
        imgui.text("Changed: %s, Values: %s" % (changed, self.values))
        imgui.end()

class DragInt4(Page):
    def __init__(self, window):
        super().__init__(window, "dragint4", "Drag Integer 4")
        self.values = 88, 42, 69, 0

    def on_render(self):
        imgui.begin("Example: drag int 4")
        changed, self.values = imgui.drag_int4(
            "drag ints", *self.values
        )
        imgui.text("Changed: %s, Values: %s" % (changed, self.values))
        imgui.end()

def install(app):
    app.add_page(DragInt(app))
    app.add_page(DragInt2(app))
    app.add_page(DragInt3(app))
    app.add_page(DragInt4(app))
