import random

import arcade
from arcade.particles import (
    FadeParticle,
    Emitter,
    EmitBurst,
)

import imgui

from imflo.node import Node
from imflo.pin import Input


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


class SparkNode(Node):
    def __init__(self, page):
        super().__init__(page)
        self.change = 0
        self.input = Input(self, "input", self.process)
        self.add_pin(self.input)

    def reset(self):
        self.create_emitter()

    def create_emitter(self):
        ww, wh = arcade.get_window().get_size()
        spark_texture = random.choice(SPARK_TEXTURES)

        def firework_spark_mutator(particle: FadeParticle):
            """mutation_callback shared by all fireworks sparks"""
            # gravity
            particle.change_y += -0.03
            # drag
            particle.change_x += self.change
            particle.change_y += self.change

        self.emitter = Emitter(
            center_xy=(ww / 2, wh / 2),
            emit_controller=EmitBurst(random.randint(30, 40)),
            particle_factory=lambda emitter: FadeParticle(
                filename_or_texture=spark_texture,
                change_xy=arcade.math.rand_in_circle((0.0, 0.0), 9.0),
                lifetime=random.uniform(0.5, 1.2),
                mutation_callback=firework_spark_mutator,
            ),
        )

    def process(self, value):
        self.change = value

    def update(self, delta_time):
        self.emitter.update()
        if self.emitter.can_reap():
            del self.emitter
            self.reset()

    def draw(self):
        imgui.begin("Spark")

        self.begin_input(self.input)
        imgui.button("input")
        self.end_input()

        if imgui.button("Run"):
            self.reset()

        imgui.end()

        self.emitter.draw()
