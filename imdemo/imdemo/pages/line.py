import imgui

from imdemo.page import Page


class Line(Page):
    def draw(self):
        imgui.begin("Line")
        draw_list = imgui.get_window_draw_list()
        x, y = self.rel(20, 35)
        x1, y1 = self.rel(180, 80)
        draw_list.add_line(x, y, x1, y1, imgui.get_color_u32_rgba(1, 1, 0, 1), 3)
        x, y = self.rel(180, 35)
        x1, y1 = self.rel(20, 80)
        draw_list.add_line(x, y, x1, y1, imgui.get_color_u32_rgba(1, 0, 0, 1), 3)
        imgui.end()


class PolyLine(Page):
    def draw(self):
        imgui.begin("Poly Line")
        draw_list = imgui.get_window_draw_list()
        p1 = self.rel(20, 35)
        p2 = self.rel(90, 35)
        p3 = self.rel(55, 80)
        draw_list.add_polyline(
            [p1, p2, p3], imgui.get_color_u32_rgba(1, 1, 0, 1), thickness=3
        )
        p1 = self.rel(110, 35)
        p2 = self.rel(180, 35)
        p3 = self.rel(145, 80)
        draw_list.add_polyline(
            [p1, p2, p3],
            imgui.get_color_u32_rgba(1, 0, 0, 1),
            flags=imgui.DRAW_CLOSED,
            thickness=3,
        )
        imgui.end()


def install(app):
    app.add_page(Line, "line", "Line")
    app.add_page(PolyLine, "polyline", "Poly Line")
