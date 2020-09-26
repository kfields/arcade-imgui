import arcade
import imgui
import imgui.core

# from arcade_imgui import ArcadeRenderer

class Page:
    def __init__(self, window, name, title):
        self.window = window
        self.name = name
        self.title = title

        # Must create or set the context before instantiating the renderer
        #imgui.create_context()
        #self.renderer = ArcadeRenderer(window)
        #self.current = 0

    def render(self):
        imgui.new_frame()
        
        imgui.set_next_window_position(16, 32, imgui.ONCE)
        imgui.set_next_window_size(256, 732, imgui.ONCE)
        
        imgui.begin("Examples")

        titles = [page.title for page in self.window.pages.values()]
        names = [page.name for page in self.window.pages.values()]

        imgui.listbox_header("", 256, 1024)

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

        #imgui.render()

        #self.renderer.render(imgui.get_draw_data())
        #self.window.gui.render()

    def on_render(self):
        pass