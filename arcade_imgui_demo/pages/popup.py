import arcade
import imgui
import imgui.core

from arcade_imgui_demo.page import Page


class Popup(Page):
    def __init__(self, window):
        super().__init__(window, "popup", "Popup")

    def on_render(self):
        imgui.begin("Example: simple popup")

        if imgui.button("select"):
            imgui.open_popup("select-popup")

        imgui.same_line()

        if imgui.begin_popup("select-popup"):
            imgui.text("Select one")
            imgui.separator()
            imgui.selectable("One")
            imgui.selectable("Two")
            imgui.selectable("Three")
            imgui.end_popup()

        imgui.end()

class PopupContextView(Page):
    def __init__(self, window):
        super().__init__(window, "popupcontextview", "Popup Context View")

    def on_render(self):
        imgui.begin("Example: popup context view")
        imgui.text("Right-click to set value.")
        if imgui.begin_popup_context_item("Item Context Menu", mouse_button=0):
            imgui.selectable("Set to Zero")
            imgui.end_popup()
        imgui.end()

class PopupContextWindow(Page):
    def __init__(self, window):
        super().__init__(window, "popupcontextwindow", "Popup Context Window")

    def on_render(self):
        imgui.begin("Example: popup context window")
        if imgui.begin_popup_context_window(mouse_button=0):
            imgui.selectable("Clear")
            imgui.end_popup()
        imgui.end()

class PopupModal(Page):
    def __init__(self, window):
        super().__init__(window, "popupmodal", "Popup Modal")

    def on_render(self):
        imgui.begin("Example: simple popup modal")

        if imgui.button("Open Modal popup"):
            imgui.open_popup("select-popup")

        imgui.same_line()

        if imgui.begin_popup_modal("select-popup")[0]:
            imgui.text("Select an option:")
            imgui.separator()
            imgui.selectable("One")
            imgui.selectable("Two")
            imgui.selectable("Three")
            imgui.end_popup()

        imgui.end()

def install(app):
    app.add_page(Popup(app))
    app.add_page(PopupContextView(app))
    app.add_page(PopupContextWindow(app))
    app.add_page(PopupModal(app))

