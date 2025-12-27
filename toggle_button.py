import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tkinter Toggle Button")
        self.geometry("800x480")  # friendly size for small touch screens

        self.is_green = True

        self.button = tk.Button(
            self,
            text="Tap to Toggle",
            font=("Arial", 24),
            width=16,
            height=3,
            bg="green",
            fg="white",
            activeforeground="white",
            command=self.toggle_color,
        )
        self.button.pack(expand=True)

    def toggle_color(self):
        self.is_green = not self.is_green
        new_color = "green" if self.is_green else "red"
        self.button.config(bg=new_color, activebackground=new_color)


if __name__ == "__main__":
    app = App()
    app.mainloop()
