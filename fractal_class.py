import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

class FractalApp(tk.Tk):
    def __init__(self):
        self.title("Fractal Generator")
        self.geometry("800x600")
        
        #frame
        control_frame = ttk.Frame(self)
        control_frame.pack(side=tk.LEFT, fill=tk.Y)

        #canvas
        self.fig, self.ax = plt.subplots(figsize=(5, 5))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        #controls
        self.create_controls(control_frame)
    
    def create_controls(self, parent):
        
        ttk.Label(parent, text="Fractal Type").pack(pady=10)

        self.fractal_type = tk.StringVar()
        fractal_options = ["Mandelbrot", "Julia"]
        self.fractal_type.set(fractal_options[0])

        fractal_menu = ttk.OptionMenu(parent, self.fractal_type, fractal_options[0], *fractal_options)
        fractal_menu.pack(pady=10)

        draw_button = ttk.Button(parent, text="Draw", command=self.draw_fractal)
        draw_button.pack(pady=10)
    
    def draw_fractal(self):
        fractal = self.fractal_type.get()
        if fractal == "Mandelbrot":
            self.draw_mandelbrot()
        elif fractal == "Julia":
            self.draw_julia()
        
    def draw_mandelbrot(self):
        #check wikipedia for the explanation :)
        self.ax.clear()
        self.ax.clear()
        xlim = (-2.0, 1.0)
        ylim = (-1.5, 1.5)
        self.ax.set_xlim(xlim)
        self.ax.set_ylim(ylim)

        x = np.linspace(xlim[0], xlim[1], 800)
        y = np.linspace(ylim[0], ylim[1], 600)
        X, Y = np.meshgrid(x, y)
        Z = X + 1j * Y
        C = Z
        for n in range(256):
            Z = Z**2 + C
            mask = np.abs(Z) > 2.0
            Z[mask] = 0

        self.ax.imshow(np.log(np.abs(Z)), extent=(xlim[0], xlim[1], ylim[0], ylim[1]), cmap='twilight_shifted')
        self.ax.set_title("Mandelbrot Set")
        self.canvas.draw()

    def draw_julia(self):
        #same as mandelbrot
        self.ax.clear()
        xlim = (-1.5, 1.5)
        ylim = (-1.5, 1.5)
        self.ax.set_xlim(xlim)
        self.ax.set_ylim(ylim)

        x = np.linspace(xlim[0], xlim[1], 800)
        y = np.linspace(ylim[0], ylim[1], 600)
        X, Y = np.meshgrid(x, y)
        Z = X + 1j * Y
        C = complex(-0.7, 0.27015)
        for n in range(256):
            Z = Z**2 + C
            mask = np.abs(Z) > 2.0
            Z[mask] = 0

        self.ax.imshow(np.log(np.abs(Z)), extent=(xlim[0], xlim[1], ylim[0], ylim[1]), cmap='twilight_shifted')
        self.ax.set_title("Julia Set")
        self.canvas.draw()