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

        self.create_how_to_play_button()

        # Add a word display area
        self.word_display = self.canvas.create_text(
            400, 300,
            text="_ _ _ _ _",
            font=("Comic Sans MS", 40, "bold"),
            fill="white"
        )

        # Add an input display area to show the current word being typed
        self.input_frame = tk.Frame(self.root, bg="white", bd=5, relief="ridge")
        self.input_frame.place(x=200, y=370, width=400, height=60)

        self.input_var = tk.StringVar()
        self.input_display = tk.Label(
            self.input_frame,
            textvariable=self.input_var,
            font=("Arial", 24),
            bg="white",
            fg="black"
        )
        self.input_display.pack(fill="both", expand=True)

        # Create the virtual keyboard
        self.create_keyboard()

        # Add a submit button for the word
        self.submit_btn = tk.Button(
            self.root,
            text="Submit",
            font=("Comic Sans MS", 16, "bold"),
            bg="white",
            fg="black",
            command=self.submit_guess
        )
        self.submit_btn.place(x=340, y=720, width=120, height=50)

        # Game variables
        self.tries_remaining = 3
        self.game_started = False
        self.current_word = ""  # This will store the word to be guessed
        self.input_var.set("")  # Initialize the input box as empty

    def create_keyboard(self):
        # Create a frame to hold the keyboard
        self.keyboard_frame = tk.Frame(self.root, bg="#381f09")
        self.keyboard_frame.place(x=150, y=560, width=508, height=150)

        # Define the keyboard layout
        keyboard_layout = [
            ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
            ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
            ['Z', 'X', 'C', 'V', 'B', 'N', 'M', '⌫']  # Backspace at the end
        ]

        # Create the keyboard buttons
        for i, row in enumerate(keyboard_layout):
            for j, key in enumerate(row):
                # Calculate position based on row layout
                x_offset = 15 if i == 1 else 0  # Offset second row (A-L)
                x_offset = 40 if i == 2 else x_offset  # Offset third row (Z-M)

                # Create the key button
                btn = tk.Button(
                    self.keyboard_frame,
                    text=key,
                    font=("Arial", 10, "bold"),
                    width=2 if key != '⌫' else 3,  # Make all buttons more consistent
                    height=2,
                    bg="#444444",
                    fg="black",
                    bd=1,
                    relief="raised",
                    command=lambda k=key: self.key_pressed(k) if k != '⌫' else self.backspace_pressed()
                )
                btn.grid(row=i, column=j, padx=2, pady=2)


    def key_pressed(self, key):
        """Handle key press on the virtual keyboard"""
        current_text = self.input_var.get()
        new_text = current_text + key
        self.input_var.set(new_text)


    def backspace_pressed(self):
        """Handle backspace key press"""
        current_text = self.input_var.get()
        if current_text:
            self.input_var.set(current_text[:-1])


    def submit_guess(self):
        """Handle the guess submission"""
        guess = self.input_var.get().upper()
        if not guess:
            messagebox.showinfo("Error", "Please enter a word before submitting")
            return

        # For demonstration, let's assume the word to guess is "PYTHON"
        # In a complete implementation, you would have a list of words and select one randomly
        if not self.game_started:
            self.current_word = "PYTHON"
            self.game_started = True

        if guess == self.current_word:
            messagebox.showinfo("Congratulations!", "You guessed the word correctly!")
            # Reset the game or handle win scenario
            self.input_var.set("")
        else:
            self.tries_remaining -= 1
            if self.tries_remaining > 0:
                messagebox.showinfo("Incorrect", f"Wrong guess! You have {self.tries_remaining} tries remaining.")
                self.input_var.set("")
            else:
                messagebox.showinfo("Game Over", f"You're out of tries! The word was {self.current_word}.")
                # Reset the game or handle game over scenario
                self.tries_remaining = 3
                self.game_started = False
                self.input_var.set("")











































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
        • After 3 incorrect guesses, the game is over

        To play:
        1. Type your guess in the input field
        2. Click the Submit button to check your answer
        3. Watch your remaining lives at the bottom of the screen

        Good luck!
        """
        messagebox.showinfo("Game Instructions", instructions)

