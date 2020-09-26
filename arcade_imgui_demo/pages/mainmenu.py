import arcade
import imgui
import imgui.core

from arcade_imgui_demo.page import Page


class MainMenu(Page):
    def __init__(self, window):
        super().__init__(window, "mainmenu", "Main Menu")

    def on_render(self):
        if imgui.begin_main_menu_bar():
            # first menu dropdown
            if imgui.begin_menu('File', True):
                imgui.menu_item('New', 'Ctrl+N', False, True)
                imgui.menu_item('Open ...', 'Ctrl+O', False, True)

                # submenu
                if imgui.begin_menu('Open Recent', True):
                    imgui.menu_item('doc.txt', None, False, True)
                    imgui.end_menu()

                imgui.end_menu()

            imgui.end_main_menu_bar()

def install(app):
    app.add_page(MainMenu(app))
