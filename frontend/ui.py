import tkinter as tk
import customtkinter
from tkinter import font as tkfont
from tkinter import PhotoImage

root = tk.Tk()
root.geometry("500x500")
root.title("The Hangman Game")

bg_image = PhotoImage(file="frontend/background.png")





label = tk.Label(root, text="The Hangman Game", fg= 'black', bg= 'beige', font=('Zapfino', 20), height=1)
label.pack(fill='x',padx=10)


custom_font = tkfont.Font(family="Comic Sans MS", size=25, weight="bold")
button = tk.Label(
    root,
    text="PLAY",
    fg="white",
    bg="#03ac13",
    font=custom_font,
    height=2,
    width=8,
    relief="raised",  # Gives a 3D effect
    bd=5,  # Border width
    highlightbackground="#008000",
    padx=10,
    pady=5,
)
button.pack(pady=50)
button.pack(side=tk.BOTTOM)


print("working fine")


root.mainloop()