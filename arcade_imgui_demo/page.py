import arcade
import imgui
import imgui.core

class Page(arcade.View):
    def __init__(self, window, name, title):
        super().__init__(window)
        self.name = name
        self.title = title

    def reset(self):
        pass

    @classmethod
    def create(self, app, name, title):
        page = self(app, name, title)
        page.reset()
        return page

    def on_draw(self):
        arcade.start_render()

        imgui.new_frame()
        
        if self.window.view_metrics:
            self.window.view_metrics = imgui.show_metrics_window(closable=True)

        self.draw_mainmenu()
        self.draw_navbar()

        imgui.set_next_window_position(288, 32, imgui.ONCE)
        imgui.set_next_window_size(512, 512, imgui.ONCE)

        self.render()
        
        imgui.end_frame()

    def draw_navbar(self):
        imgui.set_next_window_position(16, 32, imgui.ONCE)
        imgui.set_next_window_size(256, 732, imgui.ONCE)
        
        imgui.begin("Examples")

        titles = [page['title'] for page in self.window.pages.values()]
        names = [page['name'] for page in self.window.pages.values()]

        if imgui.listbox_header("Examples", -1, -1):

            for entry in self.window.pages.values():
                opened, selected = imgui.selectable(entry['title'], entry['name'] == self.window.page.name)
                if opened:
                    self.window.show(entry['name'])

            imgui.listbox_footer()
        
        imgui.end()

    def draw_mainmenu(self):
        if imgui.begin_main_menu_bar():
            # File
            if imgui.begin_menu('File', True):
                clicked_quit, selected_quit = imgui.menu_item(
                    "Quit", 'Cmd+Q', False, True
                )

                if clicked_quit:
                    exit(1)

                imgui.end_menu()
            # View
            if imgui.begin_menu('View', True):
                clicked_metrics, self.window.view_metrics = imgui.menu_item(
                    "Metrics", 'Cmd+M', self.window.view_metrics, True
                )

                imgui.end_menu()

            imgui.end_main_menu_bar()

    def render(self):
        pass