import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Initialize x and y data
x, y = np.array([]), np.array([])

# Function to load data from a CSV file
def load_data():
    global x, y
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])

    if file_path:
        try:
            data = np.genfromtxt(file_path, delimiter=",", skip_header=1)
            if data.shape[1] < 2:
                raise ValueError("The file must have at least two columns (x and y).")

            x, y = data[:, 0], data[:, 1]
            messagebox.showinfo("Success", "Data loaded successfully!")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to load data: {e}")

# Function to interpolate and plot the data
def plot_interpolation():
    if x.size == 0 or y.size == 0:
        messagebox.showerror("Error", "No data loaded!")
        return

    if len(np.unique(x)) != len(x):
        messagebox.showerror("Error", "Duplicate x-values detected. Interpolation requires unique x.")
        return

    method = method_var.get()
    xp = np.linspace(min(x), max(x), 500)

    try:
        if method == "Linear":
            interpolator = interp1d(x, y, kind="linear")
        elif method == "Cubic Spline":
            interpolator = interp1d(x, y, kind="cubic")
        elif method == "Nearest":
            interpolator = interp1d(x, y, kind="nearest")
        else:
            messagebox.showerror("Error", "Invalid interpolation method selected!")
            return

        yp = interpolator(xp)

        # Plot
        ax.clear()
        ax.plot(x, y, 'o', label="Data Points")
        ax.plot(xp, yp, label=f"{method} Interpolation")
        ax.set_title(f"{method} Interpolation")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.legend()
        canvas.draw()

    except Exception as e:
        messagebox.showerror("Error", f"Failed to interpolate: {e}")

# Function to justify the method
def update_justification():
    justification_text.set(
        "Method Selection Justification:\n"
        "- Linear: Best for sparse or linearly varying data.\n"
        "- Cubic Spline: Best for smooth data with gradual changes.\n"
        "- Nearest: Useful for step-like or discontinuous data."
    )

# Function to save the plot
def save_plot():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png")]
    )

    if file_path:
        try:
            fig.savefig(file_path)
            messagebox.showinfo("Success", "Plot saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save plot: {e}")

# Main Tkinter window
root = tk.Tk()
root.title("Interpolation Viewer")

# Frame for controls
frame = tk.Frame(root)
frame.pack(pady=10)

# Buttons and dropdown
load_button = tk.Button(frame, text="Load Data", command=load_data)
load_button.grid(row=0, column=0, padx=5)

method_var = tk.StringVar()
method_var.set("Linear")

method_menu = ttk.OptionMenu(frame, method_var, "Linear", "Linear", "Cubic Spline", "Nearest")
method_menu.grid(row=0, column=1, padx=5)

plot_button = tk.Button(frame, text="Plot", command=plot_interpolation)
plot_button.grid(row=0, column=2, padx=5)

save_button = tk.Button(frame, text="Save Plot", command=save_plot)
save_button.grid(row=0, column=3, padx=5)

justify_button = tk.Button(frame, text="Justify Method", command=update_justification)
justify_button.grid(row=0, column=4, padx=5)

# Matplotlib figure
fig, ax = plt.subplots(figsize=(6, 4))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Justification label
justification_text = tk.StringVar()
justification_label = tk.Label(root, textvariable=justification_text, justify="left", wraplength=500)
justification_label.pack(pady=10)

# Run app
root.mainloop()
