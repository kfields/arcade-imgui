import arcade
import imgui
import imgui.core

from arcade_imgui_demo.page import Page


class DragInt(Page):
    def reset(self):
        self.value = 42

    def render(self):
        imgui.begin("Example: drag int")
        changed, self.value = imgui.drag_int("drag int", self.value,)
        imgui.text("Changed: %s, Value: %s" % (changed, self.value))
        imgui.end()

class DragInt2(Page):
    def reset(self):
        self.values = 88, 42

    def render(self):
        imgui.begin("Example: drag int 2")
        changed, self.values = imgui.drag_int2(
            "drag ints", *self.values
        )
        imgui.text("Changed: %s, Values: %s" % (changed, self.values))
        imgui.end()

class DragInt3(Page):
    def reset(self):
        self.values = 88, 42, 69

    def render(self):
        imgui.begin("Example: drag int 3")
        changed, self.values = imgui.drag_int3(
            "drag ints", *self.values
        )
        imgui.text("Changed: %s, Values: %s" % (changed, self.values))
        imgui.end()

class DragInt4(Page):
    def reset(self):
        self.values = 88, 42, 69, 0

    def render(self):
        imgui.begin("Example: drag int 4")
        changed, self.values = imgui.drag_int4(
            "drag ints", *self.values
        )
        imgui.text("Changed: %s, Values: %s" % (changed, self.values))
        imgui.end()

def install(app):
    app.add_page(DragInt, "dragint", "Drag Integer")
    app.add_page(DragInt2, "dragint2", "Drag Integer 2")
    app.add_page(DragInt3, "dragint3", "Drag Integer 3")
    app.add_page(DragInt4, "dragint4", "Drag Integer 4")
