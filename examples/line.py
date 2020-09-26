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
        imgui.set_next_window_size(512, 512, imgui.ONCE)

        imgui.begin("Line")
        draw_list = imgui.get_window_draw_list()
        draw_list.add_line(20, 35, 180, 80, imgui.get_color_u32_rgba(1,1,0,1), 3)
        draw_list.add_line(180, 35, 20, 80, imgui.get_color_u32_rgba(1,0,0,1), 3)
        imgui.end()

        imgui.begin("Poly Line")
        draw_list = imgui.get_window_draw_list()
        draw_list.add_polyline([(20, 35), (90, 35), (55, 80)], imgui.get_color_u32_rgba(1,1,0,1), closed=False, thickness=3)
        draw_list.add_polyline([(110, 35), (180, 35), (145, 80)], imgui.get_color_u32_rgba(1,0,0,1), closed=True, thickness=3)
        imgui.end()

        imgui.end_frame()

        imgui.render()

        self.renderer.render(imgui.get_draw_data())


class App(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Line Example", resizable=True)
        self.gui = MyGui(self)

    def on_draw(self):
        arcade.start_render()
        self.gui.render()


app = App()
arcade.run()
