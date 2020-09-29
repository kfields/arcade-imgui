import os
import arcade
import imgui
import imgui.core

from arcade_imgui import ArcadeRenderer

SPRITE_SCALING = 0.5

class MyGui:
    def __init__(self, window):
        self.window = window
        # Must create or set the context before instantiating the renderer
        imgui.create_context()
        self.renderer = ArcadeRenderer(window)
        self.sprite = arcade.Sprite(":resources:images/space_shooter/playerShip1_orange.png", SPRITE_SCALING)
        image = self.sprite.texture.image
        self.texture = window.ctx.texture(image.size, components=3, data=image.convert("RGB").tobytes())

    def draw(self):
        imgui.new_frame()

        imgui.set_next_window_position(16, 32, imgui.ONCE)
        imgui.set_next_window_size(512, 512, imgui.ONCE)

        imgui.begin("Sprite")
        imgui.image(self.texture.glo, *self.texture.size)
        imgui.end()

        imgui.end_frame()

        imgui.render()

        self.renderer.render(imgui.get_draw_data())


class App(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Sprite Example", resizable=True)
        self.gui = MyGui(self)
        #
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)


    def on_draw(self):
        arcade.start_render()
        self.gui.draw()


app = App()
arcade.run()
