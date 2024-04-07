from shiny import App, render, ui, reactive
import numpy as np
import matplotlib.pyplot as plt
import shiny.experimental as x


app_ui = x.ui.page_fillable(
    x.ui.layout_sidebar(
        x.ui.sidebar(
            ui.input_slider("n", "observations", 0, 100, 20),
            ui.input_slider("bins", "Bins", min=0, max=20, value=7)
        ),
        x.ui.output_plot("plot"),
    )
)


def server(input, output, session):
    
    @reactive.Calc
    def random_data():
        return np.random.randn(input.n())
    
    @output
    @render.plot
    def plot():
        x = random_data()
        plt.hist(x, bins=input.bins(), density=True)
        plt.xlim(-5, 5)


app = App(app_ui, server)