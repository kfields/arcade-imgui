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

    def render(self):
        imgui.new_frame()

        imgui.set_next_window_position(16, 32, imgui.ONCE)
        imgui.set_next_window_size(256, 256, imgui.ONCE)

        imgui.begin("Rectangle")
        draw_list = imgui.get_window_draw_list()
        draw_list.add_rect(20, 35, 90, 80, imgui.get_color_u32_rgba(1,1,0,1), thickness=3)
        draw_list.add_rect(110, 35, 180, 80, imgui.get_color_u32_rgba(1,0,0,1), rounding=5, thickness=3)
        imgui.end()

        imgui.set_next_window_position(270, 32, imgui.ONCE)
        imgui.set_next_window_size(256, 256, imgui.ONCE)

        imgui.begin("Filled Rectangle")
        draw_list = imgui.get_window_draw_list()
        draw_list.add_rect_filled(20, 35, 90, 80, imgui.get_color_u32_rgba(1,1,0,1))
        draw_list.add_rect_filled(110, 35, 180, 80, imgui.get_color_u32_rgba(1,0,0,1), 5)
        imgui.end()

        imgui.end_frame()

        imgui.render()

        self.renderer.render(imgui.get_draw_data())


class App(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Rectangle Example", resizable=True)
        self.gui = MyGui(self)

    def on_draw(self):
        arcade.start_render()
        self.gui.render()


app = App()
arcade.run()
