import arcade
import imgui
import imgui.core

from arcade_imgui_demo.page import Page


class ListboxPage(Page):
    def __init__(self, window):
        super().__init__(window, "listbox", "Listbox")
        self.current = 2
    def on_render(self):    
        imgui.begin("Example: listbox widget")

        clicked, self.current = imgui.listbox(
            "List", self.current, ["first", "second", "third"]
        )

        imgui.end()

class CustomListboxPage(Page):
    def __init__(self, window):
        super().__init__(window, "customlistbox", "Listbox - Custom")
        self.current = 2
    def on_render(self):    
        imgui.begin("Example: custom listbox")

        if imgui.listbox_header("Custom List", 200, 100):
            imgui.selectable("Selected", True)
            imgui.selectable("Not Selected", False)

            imgui.listbox_footer()

        imgui.end()

def install(app):
    app.add_page(ListboxPage(app))
    app.add_page(CustomListboxPage(app))
