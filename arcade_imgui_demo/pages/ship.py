import os

import arcade
import imgui
import imgui.core

from arcade_imgui_demo.page import Page

SPRITE_SCALING = 0.5


class ShipPage(Page):
    def __init__(self, window):
        super().__init__(window, "ship", "Ship")
        self.sprite = arcade.Sprite(
            ":resources:images/space_shooter/playerShip1_orange.png",
            SPRITE_SCALING,
            center_x = 512,
            center_y = 256
            )
        image = self.sprite.texture.image
        self.texture = window.ctx.texture(image.size, components=3, data=image.convert("RGB").tobytes())
        self.reset()

    def reset(self):
        self.rotation = 0
        self.scale = 1
        self.alpha = 255
        self.color_enabled = True
        self.color = 1,1,1

    def on_render(self):
        imgui.set_next_window_position(288, 32, imgui.ONCE)
        imgui.set_next_window_size(256, 256, imgui.ONCE)

        imgui.begin("Ship")

        # Rotation
        imgui.image(self.texture.glo, *self.texture.size)
        changed, self.rotation = imgui.drag_float(
            "Rotation", self.rotation,
        )
        self.sprite.angle = self.rotation

        # Scale
        changed, self.scale = imgui.drag_float(
            "Scale", self.scale, .1
        )
        self.sprite.scale = self.scale

        # Alpha
        changed, self.alpha = imgui.drag_int(
            "Alpha", self.alpha, 1, 0, 255
        )
        self.sprite.alpha = self.alpha

        # Color
        _, self.color_enabled = imgui.checkbox("Tint", self.color_enabled)
        if self.color_enabled:
            changed, self.color = imgui.color_edit3("Color", *self.color)
            self.sprite.color = (int(self.color[0] * 255), int(self.color[1] * 255), int(self.color[2] * 255))
        else:
            self.sprite.color = 255, 255, 255

        if imgui.button("Reset"):
            self.reset()

        imgui.end()

        self.sprite.draw()

def install(app):
    app.add_page(ShipPage(app))
