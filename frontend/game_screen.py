import tkinter as tk

class GameScreen:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x800")
        self.root.title("The Hangman Game")

        self.root.resizable(False, False)

        self.canvas = tk.Canvas(root, width=600, height=800, bg="#87CEEB", highlightthickness=0)  # Sky blue color
        self.canvas.pack(fill="both", expand=True)
