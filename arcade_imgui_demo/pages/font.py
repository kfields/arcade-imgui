from pathlib import Path

import arcade
import imgui
import imgui.core

from arcade_imgui_demo.page import Page

RESOURCE_PATH = Path(__file__).parent.parent / 'assets'

class FontPage(Page):
    def __init__(self, window):
        super().__init__(window, "font", "Font")
        io = imgui.get_io()

        self.new_font = io.fonts.add_font_from_file_ttf(str(RESOURCE_PATH / "DroidSans.ttf"), 20)
        self.window.gui.renderer.refresh_font_texture()

    def on_render(self):
        imgui.begin("Font")

        imgui.text("Text displayed using default font")
        with imgui.font(self.new_font):
            imgui.text("Text displayed using custom font")

        imgui.end()

def install(app):
    app.add_page(FontPage(app))