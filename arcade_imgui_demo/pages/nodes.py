import arcade
import imgui
import imgui.core

from arcade_imgui_demo.page import Page


class NodesPage(Page):
    def reset(self):
        self.value = 88

    def render(self):
        width = 20
        height = 100
        draw_list = imgui.get_overlay_draw_list()

        imgui.begin("Node 1")
        imgui.begin_group()
        imgui.text('input')
        imgui.end_group()
        imgui.same_line(spacing=16)
        imgui.begin_group()
        changed, self.value = imgui.v_slider_int(
            "value",
            width, height, self.value,
            min_value=0, max_value=100,
            format="%d"
        )
        imgui.end_group()
        imgui.same_line(spacing=16)
        imgui.begin_group()
        imgui.text('output')
        x, y = imgui.get_cursor_screen_pos()
        imgui.end_group()
        imgui.end()

        imgui.begin("Node 2")
        x1, y1 = imgui.get_cursor_screen_pos()
        imgui.text('input')
        imgui.end()

        #arcade.draw_line(x,y,x1,y1,(arcade.color.AQUA))
        draw_list.add_line(x,y,x1,y1, imgui.get_color_u32_rgba(1,1,0,1), 3)

def install(app):
    app.add_page(NodesPage, "nodes", "Nodes")
