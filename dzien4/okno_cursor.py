import tkinter as tk


def main() -> None:
    root = tk.Tk()
    root.title("Moje okno Tkinter")
    root.geometry("400x250")

    frame = tk.Frame(root, padx=16, pady=16)
    frame.pack(fill="both", expand=True)

    label = tk.Label(frame, text="Witaj w Tkinter!", font=("Segoe UI", 14))
    label.pack(pady=12)

    zamknij_btn = tk.Button(frame, text="Zamknij", command=root.destroy)
    zamknij_btn.pack(pady=8)

    root.mainloop()


if __name__ == "__main__":
    main()
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class TkinterApp:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Moje okno Tkinter")
        self.root.geometry("640x480")

        self.frame = tk.Frame(self.root, padx=16, pady=16)
        self.frame.pack(fill="both", expand=True)

        self._build_header()
        self._build_chart()
        self._build_footer()

    def _build_header(self) -> None:
        self.label = tk.Label(self.frame, text="Witaj w Tkinter!", font=("Segoe UI", 14), fg="red")
        self.label.pack(pady=12)

    def _build_chart(self) -> None:
        # Wykres Matplotlib osadzony w Tkinter
        self.figure = Figure(figsize=(5, 3), dpi=100)
        self.axis = self.figure.add_subplot(111)
        self.axis.set_title("Przykładowy wykres")
        self.axis.set_xlabel("X")
        self.axis.set_ylabel("Y")
        self.axis.grid(True, linestyle=":", linewidth=0.5)

        x_values = [0, 1, 2, 3, 4, 5]
        y_values = [v * v for v in x_values]
        self.axis.plot(x_values, y_values, marker="o", color="tab:blue", label="y = x^2")
        self.axis.legend(loc="best")

        self.canvas = FigureCanvasTkAgg(self.figure, master=self.frame)
        self.canvas.draw()
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(fill="both", expand=True, pady=8)

    def _build_footer(self) -> None:
        self.zamknij_btn = tk.Button(self.frame, text="Zamknij", command=self.root.destroy)
        self.zamknij_btn.pack(pady=8)

    def run(self) -> None:
        self.root.mainloop()


def main() -> None:
    app = TkinterApp()
    app.run()


if __name__ == "__main__":
    main()
