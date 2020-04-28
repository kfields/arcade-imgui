import pyglet
import imgui
import imgui.core

from arcadeimgui.integrations.arcade import ArcadeRenderer

import arcade

class MyGui:
    def __init__(self, window):
        self.window = window
        # Must create or set the context before instantiating the renderer
        imgui.create_context()
        self.renderer = ArcadeRenderer(window)
        # Window variables
        self.test_input = 0

    def render(self):
        imgui.new_frame()

        imgui.begin("Test Window")
        imgui.text("This is the test window.")
        changed, self.test_input = imgui.input_int("Integer Input Test", self.test_input)

        imgui.end()

        imgui.end_frame()

        imgui.render()
        
        self.renderer.render(imgui.get_draw_data())

class App(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Arcade Imgui Input Test")
        self.gui = MyGui(self)

    def on_draw(self):
        arcade.start_render()
        #TODO: sets the gui origin to 0,0.  Probably a simple fix
        #arcade.draw_text(str(self.gui.test_input), 128, 128, arcade.color.WHITE_SMOKE, 64)
        self.gui.render()
        arcade.draw_text(str(self.gui.test_input), 128, 128, arcade.color.WHITE_SMOKE, 64)

app = App()
arcade.run()