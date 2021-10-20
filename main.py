import random
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
# import pyperclip
import json
import pandas

BACKGROUND_COLOR = "#B1DDC6"
FLIP_TIME = 10
timer = None
current_card = {}


def remove_card():
    to_learn.remove(current_card)
    print(len(to_learn))
    df3 = pandas.DataFrame(to_learn)
    df3.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


# ---------------------------- LOAD CSV ------------------------------- #


try:
    with open("./data/words_to_learn.csv.csv", mode="r") as f:
        df = pandas.read_csv(f)
except FileNotFoundError:
    with open("./data/french_words.csv", mode="r") as f:
        df2 = pandas.read_csv(f)
        to_learn = df2.to_dict(orient="records")
else:
    to_learn = df.to_dict(orient="records")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


# --------------------- CREATE NEW FLASH CARDS ------------------------ #


def next_card():
    global current_card, flip_timer
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    window.after_cancel(flip_timer)
    flip_timer = window.after(3000, flip_card)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()

window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="./images/card_front.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_back_img = PhotoImage(file="./images/card_back.png")
card_title = canvas.create_text(400, 150, text="", fill="black", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", fill="black", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2, sticky="ew")

wrong_button_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

right_button_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_button_img, highlightthickness=0, command=remove_card)
right_button.grid(column=1, row=1)

next_card()

window.mainloop()
