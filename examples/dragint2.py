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
        self.values = 88, 42

    def render(self):
        imgui.new_frame()

        imgui.begin("Example: drag int")
        changed, self.values = imgui.drag_int2(
            "drag ints", *self.values
        )
        imgui.text("Changed: %s, Values: %s" % (changed, self.values))
        imgui.end()

        imgui.end_frame()

        imgui.render()

        self.renderer.render(imgui.get_draw_data())


class App(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Drag Integer 2 Example")
        self.gui = MyGui(self)

    def on_draw(self):
        arcade.start_render()
        self.gui.render()


app = App()
arcade.run()
