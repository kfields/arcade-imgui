import arcade
import imgui
import imgui.core

from arcade_imgui_demo.page import Page


class FontImage(Page):
    def render(self):
        imgui.begin("Image example")
        texture_id = imgui.get_io().fonts.texture_id
        draw_list = imgui.get_window_draw_list()
        draw_list.add_image(texture_id, (20, 35), (180, 80), col=imgui.get_color_u32_rgba(0.5,0.5,1,1))
        imgui.end()

def install(app):
    app.add_page(FontImage, "fontimage", "Font Image")
