import os
import random

import arcade
import imgui

from arcade import Point, Vector
from arcade.utils import _Vec2  # bring in "private" class

from imflo.particle import AnimatedAlphaParticle

from imflo.page import Page

from .sine import SineNode
from .scope import ScopeNode
from .spark import SparkNode

class SparksPage(Page):
    def __init__(self, window, name, title):
        super().__init__(window, name, title)
        sine_node = self.add_node(SineNode(self))
        scope_node = self.add_node(ScopeNode(self))
        spark_node = self.add_node(SparkNode(self))
        self.connect(sine_node.get_pin('output'), scope_node.get_pin('input'))
        self.connect(sine_node.get_pin('output'), spark_node.get_pin('input'))

    def reset(self):
        super().reset()

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def draw(self):
        for node in self.nodes:
            node.draw()

        for wire in self.wires:
            wire.draw()

def install(app):
    app.add_page(SparksPage, "sparks", "Sparks")
