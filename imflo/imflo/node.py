import arcade
import imgui

class Node:
    def __init__(self, page):
        self.page = page
        self.pins = {}

    def add_pin(self, pin):
        self.pins[pin.name] = pin

    def get_pin(self, name):
        return self.pins[name]

    def begin_input(self, pin):
        x, y = imgui.get_cursor_screen_pos()
        wx, wy = imgui.get_window_position()
        x = wx - 8
        pos = (x, y)
        pin.set_position(pos)
        return pos

    def end_input(self):
        if imgui.begin_drag_drop_target():
            payload = imgui.accept_drag_drop_payload('itemtype')
            if payload is not None:
                payload = self.page.end_dnd()
                print('Received:', payload)
                self.page.connect(self.input, payload)
            imgui.end_drag_drop_target()

    def begin_output(self, pin):
        x, y = imgui.get_cursor_screen_pos()
        wx, wy = imgui.get_window_position()
        ww, wh = imgui.get_window_size()

        x = wx + ww + 8
        pos = (x, y)
        pin.set_position(pos)
        return pos

    def end_output(self):
        if imgui.begin_drag_drop_source():
            imgui.set_drag_drop_payload('itemtype', b'payload')
            self.page.start_dnd(self.output)
            imgui.button('dragged source')
            imgui.end_drag_drop_source()

    def update(self, delta_time):
        pass

    def draw(self):
        pass