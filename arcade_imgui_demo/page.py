import arcade
import imgui
import imgui.core

class Page(arcade.View):
    def __init__(self, window, name, title):
        super().__init__(window)
        self.name = name
        self.title = title

    def on_draw(self):
        arcade.start_render()

        imgui.new_frame()
        
        imgui.set_next_window_position(16, 32, imgui.ONCE)
        imgui.set_next_window_size(256, 732, imgui.ONCE)
        
        imgui.begin("Examples")

        titles = [page.title for page in self.window.pages.values()]
        names = [page.name for page in self.window.pages.values()]

        if imgui.listbox_header("Examples", -1, -1):

            for page in self.window.pages.values():
                opened, selected = imgui.selectable(page.title, page.name == self.window.page.name)
                if selected:
                    self.window.show(page.name)
                    imgui.set_next_window_position(288, 32, imgui.ONCE)
                    imgui.set_next_window_size(512, 512, imgui.ONCE)

            imgui.listbox_footer()
        
        imgui.end()

        self.on_render()
        
        imgui.end_frame()

    def on_render(self):
        pass