import arcade
import imgui
import imgui.core

from arcade_imgui_demo.page import Page


class Checkbox(Page):
    def reset(self):
        self.checkbox1_enabled = True
        self.checkbox2_enabled = False

    def render(self):
        imgui.begin("Example: checkboxes")

        # note: first element of return two-tuple notifies if there was a click
        #       event in currently processed frame and second element is actual
        #       checkbox state.
        _, self.checkbox1_enabled = imgui.checkbox("Checkbox 1", self.checkbox1_enabled)
        _, self.checkbox2_enabled = imgui.checkbox("Checkbox 2", self.checkbox2_enabled)

        imgui.text("Checkbox 1 state value: {}".format(self.checkbox1_enabled))
        imgui.text("Checkbox 2 state value: {}".format(self.checkbox2_enabled))

        imgui.end()

class CheckboxFlags(Page):
    def reset(self):
        self.flags = imgui.WINDOW_NO_RESIZE | imgui.WINDOW_NO_MOVE

    def render(self):
        imgui.begin("Example: checkboxes for flags", flags=self.flags)

        clicked, self.flags = imgui.checkbox_flags(
            "No resize", self.flags, imgui.WINDOW_NO_RESIZE
        )
        clicked, self.flags = imgui.checkbox_flags(
            "No move", self.flags, imgui.WINDOW_NO_MOVE
        )
        clicked, self.flags = imgui.checkbox_flags(
            "No collapse", self.flags, imgui.WINDOW_NO_COLLAPSE
        )
        # note: it also allows to use multiple flags at once
        clicked, self.flags = imgui.checkbox_flags(
            "No resize & no move", self.flags,
            imgui.WINDOW_NO_RESIZE | imgui.WINDOW_NO_MOVE
        )
        imgui.text("Current flags value: {0:b}".format(self.flags))
        imgui.end()

def install(app):
    app.add_page(Checkbox, "checkbox", "Checkbox")
    app.add_page(CheckboxFlags, "checkboxflags", "CheckboxFlags")


