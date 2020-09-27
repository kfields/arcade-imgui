import arcade
import imgui
import imgui.core

from arcade_imgui_demo.page import Page


class ListboxPage(Page):
    def reset(self):
        self.current = 2

    def render(self):    
        imgui.begin("Example: listbox widget")

        clicked, self.current = imgui.listbox(
            "List", self.current, ["first", "second", "third"]
        )

        imgui.end()

class CustomListboxPage(Page):
    def reset(self):
        self.current = 2

    def render(self):    
        imgui.begin("Example: custom listbox")

        if imgui.listbox_header("Custom List", 200, 100):
            imgui.selectable("Selected", True)
            imgui.selectable("Not Selected", False)

            imgui.listbox_footer()

        imgui.end()

def install(app):
    app.add_page(ListboxPage, "listbox", "Listbox")
    app.add_page(CustomListboxPage, "customlistbox", "Listbox - Custom")
