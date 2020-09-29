import arcade
import imgui
import imgui.core

from imdemo.page import Page


class WindowDraw(Page):
    def draw(self):
        pos_x = 10
        pos_y = 10
        sz = 20

        draw_list = imgui.get_window_draw_list()

        for i in range(0, imgui.COLOR_COUNT):
            name = imgui.get_style_color_name(i)
            draw_list.add_rect_filled(pos_x, pos_y, pos_x+sz, pos_y+sz, imgui.get_color_u32_idx(i))
            imgui.dummy(sz, sz)
            imgui.same_line()

        rgba_color = imgui.get_color_u32_rgba(1, 1, 0, 1)
        draw_list.add_rect_filled(pos_x, pos_y, pos_x+sz, pos_y+sz, rgba_color)

def install(app):
    app.add_page(WindowDraw, "windowdraw", "Window Draw")
