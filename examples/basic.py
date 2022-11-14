import arcade
import imgui
from arcade_imgui import ArcadeRenderer


class BasicExample(arcade.Window):

    def __init__(self):
        super().__init__(800, 600, "Basic Example", resizable=True)

        imgui.create_context()
        self.renderer = ArcadeRenderer(self)

    def on_draw(self):
        self.clear()

        imgui.new_frame()

        imgui.show_demo_window(False)

        imgui.render()
        self.renderer.render(imgui.get_draw_data())


if __name__ == '__main__':
    window = BasicExample()
    arcade.run()