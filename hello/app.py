import numpy as np
import matplotlib.pyplot as plt
from shiny import App, render, ui

def plot_input(input):
    x = 100 + 15*np.random.randn(input.n())
    plt.hist(x, bins=7, density=True)
    

def server(input, output, session):
    @output
    @render.plot
    def plot():
        plot_input(input)
    

app_ui = ui.page_fixed(
    ui.input_slider("n", "Number of bins", 0, 100, 20),
    ui.output_plot(id="plot")
)

app = App(app_ui, server)