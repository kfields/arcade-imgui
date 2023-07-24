import imgui

import arcade

from imdemo.page import Page

SPRITE_SCALING = 0.5


class SpritePage(Page):
    def __init__(self, window, name, title):
        super().__init__(window, name, title)
        self.sprite = arcade.Sprite(
            ":resources:images/space_shooter/playerShip1_orange.png", SPRITE_SCALING
        )
        image = self.sprite.texture.image
        self.texture = window.ctx.texture(
            image.size, components=3, data=image.convert("RGB").tobytes()
        )

    def draw(self):
        imgui.begin("Sprite")
        imgui.image(self.texture.glo, *self.texture.size)
        imgui.end()


def install(app):
    app.add_page(SpritePage, "sprite", "Sprite")
