import arcade
import imgui as gui

from arcade_imgui import ArcadeRenderer

SPRITE_SCALING = 0.5
FBSIZE = (512, 256)

class MyGui:
    def __init__(self, window):
        self.window = window
        # Must create or set the context before instantiating the renderer
        gui.create_context()
        self.renderer = ArcadeRenderer(window)
        self.sprite = arcade.Sprite(
            ":resources:images/space_shooter/playerShip1_orange.png",
            SPRITE_SCALING,
            center_x = 256,
            center_y = 128
            )
        image = self.sprite.texture.image
        self.texture = window.ctx.texture(image.size, components=3, data=image.convert("RGB").tobytes())
        self.offscreen = window.ctx.framebuffer(color_attachments=window.ctx.texture(FBSIZE))
        #self.offscreen_color_attachment = window.ctx.texture(FBSIZE)
        #self.offscreen = window.ctx.framebuffer(color_attachments=[self.offscreen_color_attachment])
        self.reset()

    def reset(self):
        self.rotation = 0
        self.scale = 1
        self.alpha = 255
        self.color_enabled = True
        self.color = 1,1,1

    def draw(self):
        gui.new_frame()

        #with self.offscreen:
        #    self.sprite.draw()


        gui.set_next_window_position(self.window.width - 256 - 16, 32, gui.ONCE)
        gui.set_next_window_size(256, 256, gui.ONCE)

        gui.begin("Framebuffer Example")

        # Rotation
        gui.image(self.texture.glo.value, *self.texture.size)
        changed, self.rotation = gui.drag_float(
            "Rotation", self.rotation,
        )
        self.sprite.angle = self.rotation

        # Scale
        changed, self.scale = gui.drag_float(
            "Scale", self.scale, .1
        )
        self.sprite.scale = self.scale

        # Alpha
        changed, self.alpha = gui.drag_int(
            "Alpha", self.alpha, 1, 0, 255
        )
        self.sprite.alpha = self.alpha

        # Color
        _, self.color_enabled = gui.checkbox("Tint", self.color_enabled)
        if self.color_enabled:
            changed, self.color = gui.color_edit3("Color", *self.color)
            self.sprite.color = (int(self.color[0] * 255), int(self.color[1] * 255), int(self.color[2] * 255))
        else:
            self.sprite.color = 255, 255, 255

        if gui.button("Reset"):
            self.reset()

        gui.image(self.offscreen.glo.value, *FBSIZE)

        gui.end()

        self.offscreen.use()
        self.offscreen.clear((0, 0, 0, 0))
        vp = arcade.get_viewport()
        #arcade.set_viewport(0, FBSIZE[0], 0, FBSIZE[1])
        self.sprite.draw()
        self.window.use()
        #self.window.ctx.screen.use()
        arcade.set_viewport(*vp)
        self.sprite.draw()

        gui.end_frame()

        gui.render()

        self.renderer.render(gui.get_draw_data())


class App(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Framebuffer Example", resizable=True)
        self.gui = MyGui(self)

    def on_draw(self):
        arcade.start_render()
        self.gui.draw()


app = App()
arcade.run()
