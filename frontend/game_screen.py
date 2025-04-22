import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

class GameScreen:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x800")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(self.root, width=800, height=800, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        og_image = Image.open("background.jpeg")
        resized_image = og_image.resize((800, 800), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(resized_image)
        self.canvas.create_image(0,0,image=self.photo, anchor="nw")

        self.create_how_to_play_button()

        self.tries_remaining = 3
        self.game_started = False

    def create_rounded_rectangle(self, x1, y1, x2, y2, radius=25, **kwargs):
        """Create a rounded rectangle on the canvas"""
        points = [
            x1 + radius, y1,
            x2 - radius, y1,
            x2, y1,
            x2, y1 + radius,
            x2, y2 - radius,
            x2, y2,
            x2 - radius, y2,
            x1 + radius, y2,
            x1, y2,
            x1, y2 - radius,
            x1, y1 + radius,
            x1, y1
        ]
        return self.canvas.create_polygon(points, smooth=True, **kwargs)

    def create_how_to_play_button(self):
        how_to_play_btn_bg = self.create_rounded_rectangle(
            20, 20, 150, 60,
            radius=25,
            fill="white",
            outline="lightblue",
            width=2,
            tags="how_to_play_btn_bg"
        )

        how_to_play_btn_text = self.canvas.create_text(
            85, 40,
            text="How To Play",
            font=("Comic Sans MS", 18, "bold"),
            fill="black",
            tags="how_to_play_btn_text"
        )

        how_to_play_hitbox = self.canvas.create_rectangle(
            20, 20, 150, 60,
            fill="",
            outline="",
            width=0,
            tags="how_to_play_btn"
        )

        # Bind hover and click events
        self.canvas.tag_bind("how_to_play_btn", "<Enter>",
                             lambda e: self.button_hover_effect("how_to_play", True))
        self.canvas.tag_bind("how_to_play_btn", "<Leave>",
                             lambda e: self.button_hover_effect("how_to_play", False))
        self.canvas.tag_bind("how_to_play_btn", "<Button-1>",
                             self.show_instructions)

    def button_hover_effect(self, btn_type, hovering):
        """Apply hover effect without moving the button"""
        bg_tag = f"{btn_type}_btn_bg"
        if hovering:
            self.canvas.itemconfig(bg_tag, fill="lightblue", width=9)
        else:
            self.canvas.itemconfig(bg_tag, fill="white", width=2)

    def show_instructions(self, event=None):
        instructions = """
        HOW TO PLAY:

        Welcome to the Word Guessing Game!

        Rules:
        • You have 3 attempts to guess the hidden word correctly
        • Each incorrect guess will cost you one life
        • No hints will be provided during gameplay
        • After 3 incorrect guesses, the game is over

        To play:
        1. Type your guess in the input field
        2. Click the Submit button to check your answer
        3. Watch your remaining lives at the bottom of the screen

        Good luck!
        """
        messagebox.showinfo("Game Instructions", instructions)

