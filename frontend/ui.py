import tkinter as tk
import customtkinter as ctk
from tkinter import PhotoImage

root = tk.Tk()
root.geometry("600x800")
root.title("The Hangman Game")
root.configure(bg="beige")

bg_image = PhotoImage(file="../frontend/background.png")


background_label = tk.Label(root, image=bg_image, bg='beige')
background_label.place(x=0, y=0, relwidth=1, relheight=1)


label = ctk.CTkLabel(root, text="The Hangman Game", font=("Impact", 35, "bold"), text_color= 'black', corner_radius=20, fg_color='beige')
label.pack(padx=140,pady=10)



button_frame = ctk.CTkFrame(
    root,
    fg_color="beige",  # Matches root bg
    bg_color="beige",
    corner_radius=1000000,
    width=300,
    height=150
)

button_frame.pack(pady=100)
button_frame.pack_propagate(False)  # Prevent auto-resizing


# Play Button

def play_btn():
    print("starting game..")
play_button = ctk.CTkButton(
    button_frame,
    text="Play",
    text_color='black',
    fg_color="lightblue",
    font=ctk.CTkFont(family="Comic Sans MS", size=25, weight="bold"),
    border_width=2,
    border_color="navy",
    width=170,
    height=50,
    corner_radius=25,  # Fully rounded
    command=play_btn
)
play_button.pack(pady=10)


# Exit Button
def exit_btn():
    root.destroy()

exit_button = ctk.CTkButton(
    button_frame,
    text="Exit",
    text_color='black',
    fg_color="lightblue",
    font=ctk.CTkFont(family="Comic Sans MS", size=25, weight="bold"),
    border_width=2,
    border_color="navy",
    width=170,
    height=50,
    corner_radius=25,  # Fully rounded
    command=exit_btn

)

button_frame.pack(pady=90)
button_frame.pack(side=tk.BOTTOM)
exit_button.pack(pady=10)

print("working fine")


root.mainloop()