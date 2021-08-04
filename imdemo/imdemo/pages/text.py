import arcade
import imgui
import imgui.core

from imdemo.page import Page

class DrawTextPage(Page):
    def draw(self):
        imgui.begin("Text")
        draw_list = imgui.get_window_draw_list()
        p1 = self.rel(100, 60)
        draw_list.add_text(*p1, imgui.get_color_u32_rgba(1,1,0,1), "Hello!")
        imgui.end()

class TextPage(Page):
    def draw(self):
        imgui.begin("Example: simple text")
        imgui.text("Simple text")
        imgui.end()

class ColoredTextPage(Page):
    def draw(self):
        imgui.begin("Example: colored text")
        imgui.text_colored("Colored text", 1, 0, 0)
        imgui.end()

class UnformattedTextPage(Page):
    def reset(self):
        self.text = '''
            Really ... 
            long ... 
            text
        '''

    def draw(self):
        imgui.begin("Example: unformatted text")
        imgui.text_unformatted(self.text)
        imgui.end()

class LabelTextPage(Page):
    def draw(self):
        imgui.begin("Example: text with label")
        imgui.label_text("my label", "my text")
        imgui.end()

def install(app):
    app.add_page(DrawTextPage, "drawtext", "Draw Text")
    app.add_page(TextPage, "text", "Text")
    app.add_page(ColoredTextPage, "coloredtext", "Colored Text")
    app.add_page(UnformattedTextPage, "unformattedtext", "Unformatted Text")
    app.add_page(LabelTextPage, "labeltext", "Text with Label")
