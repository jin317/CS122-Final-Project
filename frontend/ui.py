import tkinter as tk
import customtkinter as ctk
import random
import time


class Cloud:
    def __init__(self, canvas, width, height):
        self.canvas = canvas
        self.width = width
        self.height = height

        # Random cloud size and position
        self.size = random.randint(60, 120)
        self.x = random.randint(0, width)
        self.y = random.randint(height, height + 500)

        # Create cloud shape
        self.cloud = self.create_cloud()

        # Speed of upward movement
        self.speed = random.uniform(0.5, 1.5)

    def create_cloud(self):
        # Create a cloud using overlapping ovals
        cloud_color = "#ffffff"  # White
        x, y = self.x, self.y
        size = self.size

        # Create main body of cloud
        oval1 = self.canvas.create_oval(x, y, x + size, y + size * 0.6, fill=cloud_color, outline=cloud_color)
        oval2 = self.canvas.create_oval(x + size * 0.4, y - size * 0.2, x + size * 1.1, y + size * 0.5,
                                        fill=cloud_color, outline=cloud_color)
        oval3 = self.canvas.create_oval(x + size * 0.8, y, x + size * 1.5, y + size * 0.6, fill=cloud_color,
                                        outline=cloud_color)

        return [oval1, oval2, oval3]

    def move(self):
        # Move cloud upward
        for part in self.cloud:
            self.canvas.move(part, 0, -self.speed)

        # Update y position
        self.y -= self.speed

        # If cloud moves out of screen, reset it to bottom
        if self.y < -self.size:
            self.reset()

    def reset(self):
        # Remove old cloud
        for part in self.cloud:
            self.canvas.delete(part)

        # Reset position
        self.x = random.randint(0, self.width)
        self.y = self.height + random.randint(50, 200)
        self.size = random.randint(60, 120)
        self.speed = random.uniform(0.5, 1.5)

        # Create new cloud
        self.cloud = self.create_cloud()


class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x800")
        self.root.title("The Hangman Game")

        self.root.resizable(False, False)

        # Create canvas for sky animation
        self.canvas = tk.Canvas(root, width=600, height=800, bg="#87CEEB", highlightthickness=0)  # Sky blue color
        self.canvas.pack(fill="both", expand=True)

        # Create clouds
        self.clouds = []
        for _ in range(8):  # Create 8 clouds
            self.clouds.append(Cloud(self.canvas, 600, 800))

        # Title
        self.title = self.canvas.create_text(300, 100, text="The Hangman Game",
                                             font=("Impact", 35, "bold"), fill="black")

        # Create buttons directly on the canvas
        self.create_buttons()

        # Start animation
        self.animate()

    def create_rounded_rectangle(self, x1, y1, x2, y2, radius=25, **kwargs):
        """Create a rounded rectangle on a canvas"""
        points = [
            x1 + radius, y1,  # Top side
            x2 - radius, y1,
            x2, y1,  # Top right corner
            x2, y1 + radius,
            x2, y2 - radius,  # Right side
            x2, y2,
            x2 - radius, y2,  # Bottom right corner
            x1 + radius, y2,  # Bottom side
            x1, y2,  # Bottom left corner
            x1, y2 - radius,
            x1, y1 + radius,  # Left side
            x1, y1
        ]
        return self.canvas.create_polygon(points, **kwargs, smooth=True)

    def create_buttons(self):
        # Create button backgrounds with gradients for 3D effect
        play_btn_bg = self.create_rounded_rectangle(215, 600, 385, 650, radius=25,
                                                    fill="white", outline="lightblue",
                                                    width=2, tags="play_btn_bg")
        play_btn_text = self.canvas.create_text(300, 625, text="Play",
                                                font=("Comic Sans MS", 25, "bold"),
                                                fill="black", tags="play_btn_text")

        exit_btn_bg = self.create_rounded_rectangle(215, 680, 385, 730, radius=25,
                                                    fill="white", outline="lightblue",
                                                    width=2, tags="exit_btn_bg")
        exit_btn_text = self.canvas.create_text(300, 705, text="Exit",
                                                font=("Comic Sans MS", 25, "bold"),
                                                fill="black", tags="exit_btn_text")

        # Create transparent areas for better mouse detection
        play_hitbox = self.canvas.create_rectangle(215, 600, 385, 650,
                                                   fill="", outline="",
                                                   width=0, tags="play_btn")
        exit_hitbox = self.canvas.create_rectangle(215, 680, 385, 730,
                                                   fill="", outline="",
                                                   width=0, tags="exit_btn")



        # Bind hover events
        self.canvas.tag_bind("play_btn", "<Enter>", lambda e: self.button_hover_effect("play", True))
        self.canvas.tag_bind("play_btn", "<Leave>", lambda e: self.button_hover_effect("play", False))
        self.canvas.tag_bind("exit_btn", "<Enter>", lambda e: self.button_hover_effect("exit", True))
        self.canvas.tag_bind("exit_btn", "<Leave>", lambda e: self.button_hover_effect("exit", False))

        # Bind click events
        self.canvas.tag_bind("play_btn", "<Button-1>", self.play_btn)
        self.canvas.tag_bind("exit_btn", "<Button-1>", self.exit_btn)

    def button_hover_effect(self, btn_type, hovering):
        """Apply hover effect without moving the button"""
        bg_tag = f"{btn_type}_btn_bg"
        shine_tag = f"{btn_type}_shine"

        if hovering:
            self.canvas.itemconfig(bg_tag, fill="lightblue" , width=6)
            self.canvas.itemconfig(shine_tag, fill="#e1f5fe")
        else:
            # Return to normal state
            self.canvas.itemconfig(bg_tag, fill="white", width=2)
            self.canvas.itemconfig(shine_tag, fill="#add8e6")


    def play_btn(self, event=None):
        print("starting game..")

    def exit_btn(self, event=None):
        self.root.destroy()

    def animate(self):
        # Move all clouds
        for cloud in self.clouds:
            cloud.move()

        # Schedule next animation frame
        self.root.after(30, self.animate)


if __name__ == "__main__":
    root = tk.Tk()
    app = HangmanGame(root)
    print("working fine")
    root.mainloop()