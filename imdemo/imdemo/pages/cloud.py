import arcade
from arcade import Point, Vector
from arcade.utils import _Vec2  # bring in "private" class
import os
import random
import pyglet

import imgui
import imgui.core

from imdemo.page import Page
from imdemo.particle import AnimatedAlphaParticle

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Particle based fireworks"

CLOUD_TEXTURES = [
    arcade.make_soft_circle_texture(50, arcade.color.WHITE),
    arcade.make_soft_circle_texture(50, arcade.color.LIGHT_GRAY),
    arcade.make_soft_circle_texture(50, arcade.color.LIGHT_BLUE),
]

class CloudPage(Page):
    def reset(self):
        self.create_emitter()

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def create_emitter(self):
        self.emitter = arcade.Emitter(
            center_xy=(500, 500),
            change_xy=(0.15, 0),
            emit_controller=arcade.EmitMaintainCount(60),
            particle_factory=lambda emitter: AnimatedAlphaParticle(
                filename_or_texture=random.choice(CLOUD_TEXTURES),
                change_xy=(_Vec2(arcade.rand_in_circle((0.0, 0.0), 0.04)) + _Vec2(0.1, 0)).as_tuple(),
                start_alpha=0,
                duration1=random.uniform(5.0, 10.0),
                mid_alpha=255,
                duration2=random.uniform(5.0, 10.0),
                end_alpha=0,
                center_xy=arcade.rand_in_circle((0.0, 0.0), 50)
            )
        )

    def update(self, delta_time):
        if self.emitter.center_x > SCREEN_WIDTH:
            self.emitter.center_x = 0
        self.emitter.update()

    def draw(self):
        imgui.set_next_window_position(self.window.width - 288, 32, imgui.ONCE)
        imgui.set_next_window_size(256, 256, imgui.ONCE)

        imgui.begin("Cloud")
        if imgui.button("Reset"):
            self.reset()
        imgui.end()

        self.emitter.draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            arcade.close_window()

def install(app):
    app.add_page(CloudPage, "cloud", "Cloud")
