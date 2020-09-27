import arcade
import imgui
import imgui.core

from arcade_imgui_demo.page import Page


class DragFloat(Page):
    def reset(self):
        self.value = 42.0

    def render(self):
        imgui.begin("Example: drag float")
        changed, self.value = imgui.drag_float(
            "Default", self.value,
        )
        changed, self.value = imgui.drag_float(
            "Less precise", self.value, format="%.1f"
        )
        imgui.text("Changed: %s, Value: %s" % (changed, self.value))
        imgui.end()

class DragFloat2(Page):
    def reset(self):
        self.values = 88.0, 42.0

    def render(self):
        imgui.begin("Example: drag float 2")
        changed, self.values = imgui.drag_float2(
            "Default", *self.values
        )
        changed, self.values = imgui.drag_float2(
            "Less precise", *self.values, format="%.1f"
        )
        imgui.text("Changed: %s, Values: %s" % (changed, self.values))
        imgui.end()

class DragFloat3(Page):
    def reset(self):
        self.values = 88.0, 42.0, 69.0

    def render(self):
        imgui.begin("Example: drag float 3")
        changed, self.values = imgui.drag_float3(
            "Default", *self.values
        )
        changed, self.values = imgui.drag_float3(
            "Less precise", *self.values, format="%.1f"
        )
        imgui.text("Changed: %s, Values: %s" % (changed, self.values))
        imgui.end()

class DragFloat4(Page):
    def reset(self):
        self.values = 88.0, 42.0, 69.0, 0.0

    def render(self):
        imgui.begin("Example: drag float 4")
        changed, self.values = imgui.drag_float4(
            "Default", *self.values
        )
        changed, self.values = imgui.drag_float4(
            "Less precise", *self.values, format="%.1f"
        )
        imgui.text("Changed: %s, Values: %s" % (changed, self.values))
        imgui.end()

def install(app):
    app.add_page(DragFloat, "dragfloat", "Drag Float")
    app.add_page(DragFloat2, "dragfloat2", "Drag Float 2")
    app.add_page(DragFloat3, "dragfloat3", "Drag Float 3")
    app.add_page(DragFloat4, "dragfloat4", "Drag Float 4")
