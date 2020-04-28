import pyglet
import imgui
import imgui.core
from imgui.integrations.pyglet import PygletRenderer


class MyGui:
    def __init__(self, window):
        self.window = window
        # Must create or set the context before instantiating the renderer
        imgui.create_context()
        self.renderer = PygletRenderer(window)
        # Window variables
        self.test_input = 0

    def render(self):
        imgui.new_frame()

        imgui.begin("Test Window")
        imgui.text("This is the test window.")
        changed, self.test_input = imgui.input_int("Integer Input Test", self.test_input)

        imgui.end()

        imgui.end_frame()

        imgui.render()
        
        self.renderer.render(imgui.get_draw_data())

class App(pyglet.window.Window):
    def __init__(self):
        super().__init__(800, 600, "Pyglet Imgui Test")
        pyglet.clock.schedule_interval(self.update_gui, 1/60)
        self.gui = MyGui(self)

    def on_draw(self):
        self.clear()
        self.gui.render()
    
    def update_gui(self, dt):
        #self.clear()
        #self.UI_test.render()
        pass

app = App()
pyglet.app.run()