import arcade
import imgui
import imgui.core

from arcade_imgui import ArcadeRenderer


class MyGui:
    def __init__(self, window):
        self.window = window
        # Must create or set the context before instantiating the renderer
        imgui.create_context()
        self.renderer = ArcadeRenderer(window)

    def draw(self):
        imgui.new_frame()

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

        imgui.end_frame()

        imgui.render()

        self.renderer.render(imgui.get_draw_data())


class App(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Line Example", resizable=True)
        self.gui = MyGui(self)

    def on_draw(self):
        arcade.start_render()
        self.gui.draw()


app = App()
arcade.run()
