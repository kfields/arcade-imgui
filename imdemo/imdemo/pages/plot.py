from array import array
from random import random
from math import sin

import arcade
import imgui
import imgui.core

from imdemo.page import Page


class PlotHistogramPage(Page):
    def reset(self):
        self.values = array('f', [random() for _ in range(20)])

    def draw(self):
        imgui.begin(self.title)
        imgui.plot_histogram("histogram(random())", self.values)
        imgui.end()

class PlotLinesPage(Page):
    def reset(self):
        self.values = array('f', [sin(x * 0.1) for x in range(100)])

    def draw(self):
        imgui.begin(self.title)
        imgui.plot_lines("Sin(t)", self.values)
        imgui.end()

def install(app):
    app.add_page(PlotHistogramPage, "plothistogram", "Plot - Histogram")
    app.add_page(PlotLinesPage, "plotlines", "Plot - Lines")
