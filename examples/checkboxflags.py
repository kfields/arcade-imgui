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
        # note: these should be initialized outside of the main interaction
        #       loop
        self.flags = imgui.WINDOW_NO_RESIZE | imgui.WINDOW_NO_MOVE

    def render(self):
        imgui.new_frame()

        imgui.begin("Example: checkboxes for flags", flags=self.flags)

        clicked, self.flags = imgui.checkbox_flags(
            "No resize", self.flags, imgui.WINDOW_NO_RESIZE
        )
        clicked, self.flags = imgui.checkbox_flags(
            "No move", self.flags, imgui.WINDOW_NO_MOVE
        )
        clicked, self.flags = imgui.checkbox_flags(
            "No collapse", self.flags, imgui.WINDOW_NO_COLLAPSE
        )
        # note: it also allows to use multiple flags at once
        clicked, self.flags = imgui.checkbox_flags(
            "No resize & no move", self.flags,
            imgui.WINDOW_NO_RESIZE | imgui.WINDOW_NO_MOVE
        )
        imgui.text("Current flags value: {0:b}".format(self.flags))
        imgui.end()

        imgui.end_frame()

        imgui.render()

        self.renderer.render(imgui.get_draw_data())


class App(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Checkbox Flags Example")
        self.gui = MyGui(self)

    def on_draw(self):
        arcade.start_render()
        self.gui.render()


app = App()
arcade.run()
