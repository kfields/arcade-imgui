import arcade
from arcade import Point, Vector
from arcade.utils import _Vec2  # bring in "private" class
import os
import random

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
