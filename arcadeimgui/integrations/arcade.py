# -*- coding: utf-8 -*-
from __future__ import absolute_import

from pyglet.window import key, mouse

import imgui.integrations

from imgui.integrations import compute_fb_scale
from imgui.integrations.opengl import ProgrammablePipelineRenderer
from imgui.integrations.pyglet import PygletMixin

class ArcadeRenderer(PygletMixin, ProgrammablePipelineRenderer):
    def __init__(self, window, attach_callbacks=True):
        super(ArcadeRenderer, self).__init__()
        window_size = window.get_size()
        viewport_size = window.get_viewport_size()

        self.io.display_size = window_size
        self.io.display_fb_scale = compute_fb_scale(window_size, viewport_size)

        self._map_keys()

        if attach_callbacks:
            window.push_handlers(
                self.on_mouse_motion,
                self.on_key_press,
                self.on_key_release,
                self.on_text,
                self.on_mouse_drag,
                self.on_mouse_press,
                self.on_mouse_release,
                self.on_mouse_scroll,
                self.on_resize,
            )
