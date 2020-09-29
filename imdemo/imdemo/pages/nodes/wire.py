import arcade
import imgui

class Wire:
    def __init__(self, input, output):
        self.input = input
        self.output = output

    def draw(self):
        x, y = self.output.get_position()
        x1, y1 = self.input.get_position()
        draw_list = imgui.get_overlay_draw_list()
        #arcade.draw_line(x,y,x1,y1,(arcade.color.AQUA))
        draw_list.add_line(x,y,x1,y1, imgui.get_color_u32_rgba(1,1,1,1), 1)
