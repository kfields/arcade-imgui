import arcade
import imgui
import imgui.core

from arcade_imgui import ArcadeRenderer


class MyGui:
    def __init__(self, window):
        self.window = window
        # Must create or set the context before instantiating the renderer
        imgui.create_context()
        self.renderer = ArcadeRenderer(window)

    def render(self):
        imgui.new_frame()

        imgui.set_next_window_position(16, 32, imgui.ONCE)
        imgui.set_next_window_size(512, 512, imgui.ONCE)

        flags = imgui.WINDOW_MENU_BAR

        imgui.begin("Child Window - File Browser", flags=flags)

        if imgui.begin_menu_bar():
            if imgui.begin_menu('File'):
                imgui.menu_item('Close')
                imgui.end_menu()

            imgui.end_menu_bar()

        imgui.end()

        imgui.end_frame()

        imgui.render()

        self.renderer.render(imgui.get_draw_data())


class App(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Window Menu Bar Example", resizable=True)
        self.gui = MyGui(self)

    def on_draw(self):
        arcade.start_render()
        self.gui.render()


app = App()
arcade.run()
