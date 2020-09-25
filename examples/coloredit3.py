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
        # note: the variable that contains the color data, should be initialized
        #       outside of the main interaction loop
        self.color_1 = 1., .0, .5
        self.color_2 = 0., .8, .3

    def render(self):
        imgui.new_frame()


        imgui.begin("Example: color edit without alpha")

        # note: first element of return two-tuple notifies if the color was changed
        #       in currently processed frame and second element is current value
        #       of color
        changed, self.color_1 = imgui.color_edit3("Color 1", *self.color_1)
        changed, self.color_2 = imgui.color_edit3("Color 2", *self.color_2)

        imgui.end()

        imgui.end_frame()

        imgui.render()

        self.renderer.render(imgui.get_draw_data())


class App(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Color Edit 3 Example")
        self.gui = MyGui(self)

    def on_draw(self):
        arcade.start_render()
        self.gui.render()


app = App()
arcade.run()
