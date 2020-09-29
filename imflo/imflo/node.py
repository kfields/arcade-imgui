import arcade
import imgui

class Node:
    def __init__(self):
        self.pins = {}

    def add_pin(self, pin):
        self.pins[pin.name] = pin

    def get_pin(self, name):
        return self.pins[name]

    def mark_input(self, pin):
        x, y = imgui.get_cursor_screen_pos()
        wx, wy = imgui.get_window_position()
        x = wx - 8
        pos = (x, y)
        pin.set_position(pos)
        return pos

    def mark_output(self, pin):
        x, y = imgui.get_cursor_screen_pos()
        wx, wy = imgui.get_window_position()
        ww, wh = imgui.get_window_size()

        x = wx + ww + 8
        pos = (x, y)
        pin.set_position(pos)
        return pos

    def draw(self):
        pass