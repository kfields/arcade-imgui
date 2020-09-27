import arcade
import imgui
import imgui.core

from arcade_imgui_demo.page import Page


class TextInputPage(Page):
    def reset(self):
        self.text_val = 'Type your message here.'

    def render(self):
        imgui.begin(self.title)
        changed, self.text_val = imgui.input_text(
            'Text',
            self.text_val,
            256
        )
        imgui.text('You wrote:')
        imgui.same_line()
        imgui.text(self.text_val)
        imgui.end()

class MultiTextInputPage(Page):
    def reset(self):
        self.text_val = 'Type your message here.'

    def render(self):
        imgui.begin(self.title)
        changed, self.text_val = imgui.input_text_multiline(
            'Message',
            self.text_val,
            2056
        )
        imgui.text('You wrote:')
        imgui.same_line()
        imgui.text(self.text_val)
        imgui.end()

def install(app):
    app.add_page(TextInputPage, "textinput", "Text Input")
    app.add_page(MultiTextInputPage, "multitextinput", "Multiline Text Input")
