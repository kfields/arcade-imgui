import imgui

from imdemo.page import Page


class DnD(Page):
    def draw(self):
        imgui.begin("Example: drag and drop")

        imgui.button("source")
        if imgui.begin_drag_drop_source():
            imgui.set_drag_drop_payload("itemtype", b"payload")
            imgui.button("dragged source")
            imgui.end_drag_drop_source()

        imgui.button("dest")
        if imgui.begin_drag_drop_target():
            payload = imgui.accept_drag_drop_payload("itemtype")
            if payload is not None:
                print("Received:", payload)
            imgui.end_drag_drop_target()

        imgui.end()


def install(app):
    app.add_page(DnD, "dnd", "Drag & Drop")
