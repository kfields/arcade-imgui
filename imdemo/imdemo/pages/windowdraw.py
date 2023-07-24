import imgui

from imdemo.page import Page


class WindowDraw(Page):
    def draw(self):
        pos_x = 10
        pos_y = 10
        sz = 20

        draw_list = imgui.get_window_draw_list()
        rgba_color = imgui.get_color_u32_rgba(1, 1, 1, 1)
        for i in range(0, imgui.COLOR_COUNT):
            name = imgui.get_style_color_name(i)
            color = imgui.get_color_u32_idx(i)
            p1 = self.rel(0, i * 16)
            p2 = (p1[0] + sz, p1[1] + sz)
            draw_list.add_rect_filled(*p1, *p2, color)
            p1 = self.rel(22, i * 16)
            draw_list.add_text(*p1, rgba_color, name)

        rgba_color = imgui.get_color_u32_rgba(1, 1, 0, 1)
        draw_list.add_rect_filled(pos_x, pos_y, pos_x + sz, pos_y + sz, rgba_color)


def install(app):
    app.add_page(WindowDraw, "windowdraw", "Window Draw")
