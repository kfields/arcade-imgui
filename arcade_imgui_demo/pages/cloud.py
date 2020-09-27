import arcade
from arcade import Point, Vector
from arcade.utils import _Vec2  # bring in "private" class
import os
import random
import pyglet

import imgui
import imgui.core

from arcade_imgui_demo.page import Page

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Particle based fireworks"

CLOUD_TEXTURES = [
    arcade.make_soft_circle_texture(50, arcade.color.WHITE),
    arcade.make_soft_circle_texture(50, arcade.color.LIGHT_GRAY),
    arcade.make_soft_circle_texture(50, arcade.color.LIGHT_BLUE),
]

def clamp(a, low, high):
    if a > high:
        return high
    elif a < low:
        return low
    else:
        return a

class AnimatedAlphaParticle(arcade.LifetimeParticle):
    """A custom particle that animates between three different alpha levels"""

    def __init__(
            self,
            filename_or_texture: arcade.FilenameOrTexture,
            change_xy: Vector,
            start_alpha: int = 0,
            duration1: float = 1.0,
            mid_alpha: int = 255,
            duration2: float = 1.0,
            end_alpha: int = 0,
            center_xy: Point = (0.0, 0.0),
            angle: float = 0,
            change_angle: float = 0,
            scale: float = 1.0,
            mutation_callback=None,
    ):
        super().__init__(filename_or_texture, change_xy, duration1 + duration2, center_xy, angle, change_angle, scale,
                         start_alpha, mutation_callback)
        self.start_alpha = start_alpha
        self.in_duration = duration1
        self.mid_alpha = mid_alpha
        self.out_duration = duration2
        self.end_alpha = end_alpha

    def update(self):
        super().update()
        if self.lifetime_elapsed <= self.in_duration:
            u = self.lifetime_elapsed / self.in_duration
            self.alpha = clamp(arcade.lerp(self.start_alpha, self.mid_alpha, u), 0, 255)
        else:
            u = (self.lifetime_elapsed - self.in_duration) / self.out_duration
            self.alpha = clamp(arcade.lerp(self.mid_alpha, self.end_alpha, u), 0, 255)


class CloudPage(Page):
    def __init__(self, window):
        super().__init__(window, "cloud", "Cloud")

        arcade.set_background_color(arcade.color.BLACK)
        self.reset()

    def reset(self):
        self.create_emitter()

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

    def on_render(self):
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
    app.add_page(CloudPage(app))
