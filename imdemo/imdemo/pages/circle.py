import imgui

from imdemo.page import Page


class Circle(Page):
    def draw(self):
        imgui.begin("Circle")
        draw_list = imgui.get_window_draw_list()
        x, y = self.rel(100, 60)
        draw_list.add_circle(
            x, y, 30, imgui.get_color_u32_rgba(1, 1, 0, 1), thickness=3
        )
        imgui.end()


class CircleFilled(Page):
    def draw(self):
        imgui.begin("Filled")
        draw_list = imgui.get_window_draw_list()
        x, y = self.rel(100, 60)
        draw_list.add_circle_filled(x, y, 30, imgui.get_color_u32_rgba(1, 1, 0, 1))
        imgui.end()


def install(app):
    app.add_page(Circle, "circle", "Circle")
    app.add_page(CircleFilled, "circlefilled", "Filled Circle")
