import arcade
import imgui
import imgui.core

from arcade_imgui_demo.page import Page


class TestPage(Page):
    def render(self):
        if imgui.begin_main_menu_bar():
            if imgui.begin_menu("File", True):

                clicked_quit, selected_quit = imgui.menu_item(
                    "Quit", 'Cmd+Q', False, True
                )

                if clicked_quit:
                    exit(1)

                imgui.end_menu()
            imgui.end_main_menu_bar()

        imgui.show_test_window()

def install(app):
    app.add_page(TestPage, 'test', 'ImGui Test')
