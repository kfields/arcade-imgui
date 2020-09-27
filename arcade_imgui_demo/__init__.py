import os

import arcade
import imgui
import imgui.core

from arcade_imgui import ArcadeRenderer

class Gui:
    def __init__(self, window):
        self.window = window
        # Must create or set the context before instantiating the renderer
        imgui.create_context()
        self.renderer = ArcadeRenderer(window)

    def render(self):
        imgui.render()
        self.renderer.render(imgui.get_draw_data())

class App(arcade.Window):
    def __init__(self):
        super().__init__(1024, 768, "Arcade ImGui Demo", resizable=True)
        self.gui = Gui(self)
        self.pages = {}
        file_path = os.path.dirname(os.path.abspath(__file__))
        print(file_path)
        os.chdir(file_path)


    def on_draw(self):
        super().on_draw()
        self.gui.render()

    def run(self):
        arcade.run()

    def use(self, name):
        import importlib.util
        spec = importlib.util.spec_from_file_location("module.name", os.path.join('pages', f"{name}.py"))
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        module, install = module, module.install
        install(self)

    def add_page(self, page):
        # print(page.__dict__)
        self.pages[page.name] = page

    def show(self, name):
        self.page = page = self.pages[name]
        self.show_view(page)