import random

import arcade
from arcade.particles import LifetimeParticle, FadeParticle, Emitter, EmitBurst

import imgui
import imgui.core

from imdemo.page import Page
from imdemo.particle import AnimatedAlphaParticle

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Particle based fireworks"

RAINBOW_COLORS = (
    arcade.color.ELECTRIC_CRIMSON,
    arcade.color.FLUORESCENT_ORANGE,
    arcade.color.ELECTRIC_YELLOW,
    arcade.color.ELECTRIC_GREEN,
    arcade.color.ELECTRIC_CYAN,
    arcade.color.MEDIUM_ELECTRIC_BLUE,
    arcade.color.ELECTRIC_INDIGO,
    arcade.color.ELECTRIC_PURPLE,
)

SPARK_TEXTURES = [arcade.make_circle_texture(8, clr) for clr in RAINBOW_COLORS]
SPARK_PAIRS = [
    [SPARK_TEXTURES[0], SPARK_TEXTURES[3]],
    [SPARK_TEXTURES[1], SPARK_TEXTURES[5]],
    [SPARK_TEXTURES[7], SPARK_TEXTURES[2]],
]

def firework_spark_mutator(particle: FadeParticle):
    """mutation_callback shared by all fireworks sparks"""
    # gravity
    particle.change_y += -0.03
    # drag
    particle.change_x *= 0.92
    particle.change_y *= 0.92

class SparksPage(Page):
    def reset(self):
        self.create_emitter()

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def create_emitter(self):
        spark_texture = random.choice(SPARK_TEXTURES)
        self.emitter = Emitter(
            #center_xy=prev_emitter.get_pos(),
            center_xy=(500, 500),
            emit_controller=EmitBurst(random.randint(30, 40)),
            particle_factory=lambda emitter: FadeParticle(
                filename_or_texture=spark_texture,
                change_xy=arcade.math.rand_in_circle((0.0, 0.0), 9.0),
                lifetime=random.uniform(0.5, 1.2),
                mutation_callback=firework_spark_mutator
            )
        )

    def update(self, delta_time):
        if self.emitter.center_x > SCREEN_WIDTH:
            self.emitter.center_x = 0
        self.emitter.update()

    def draw(self):
        imgui.set_next_window_position(self.window.width - 288, 32, imgui.ONCE)
        imgui.set_next_window_size(256, 256, imgui.ONCE)

        imgui.begin("Sparks")
        if imgui.button("Run"):
            self.reset()
        imgui.end()

        self.emitter.draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            arcade.close_window()

def install(app):
    app.add_page(SparksPage, "sparks", "Sparks")
