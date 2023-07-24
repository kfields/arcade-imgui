import arcade
import imgui
import imgui.core

from imdemo.page import Page


class FontImage(Page):
    def draw(self):
        imgui.begin("Font Image")
        fonts = imgui.get_io().fonts
        texture_id = fonts.texture_id
        texture_width = fonts.texture_width
        texture_height = fonts.texture_height
        draw_list = imgui.get_window_draw_list()
        pos = self.rel(0,0)
        pos2 = self.rel(texture_width, texture_height)
        draw_list.add_image(texture_id, pos, pos2, col=imgui.get_color_u32_rgba(0.5,0.5,1,1))
        imgui.end()

def install(app):
    app.add_page(FontImage, "fontimage", "Font Image")
