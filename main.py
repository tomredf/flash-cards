from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
# import pyperclip
import json
import pandas

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- LOAD CSV ------------------------------- #

with open("./data/french_words.csv", mode="r") as f:
    df = pandas.read_csv(f)
    words_dict = df.to_dict(orient="records")
    words_list = []
    for n in words_dict:
        d = {n["French"]: n["English"]}
        words_list.append(d)


# --------------------- CREATE NEW FLASH CARDS ------------------------ #


def get_new_word():
    n = randint(0, len(words_list) - 1)
    dic = words_list[n]
    new_french_word = list(dic.keys())[0]
    en = dic[new_french_word]
    print(en)
    canvas.itemconfig(word_text, text=new_french_word)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
lang_text = canvas.create_text(400, 150, text="French", fill="black", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="word", fill="black", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2, sticky="ew")

wrong_button_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=get_new_word)
wrong_button.grid(column=0, row=1)

right_button_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_button_img, highlightthickness=0, command=get_new_word)
right_button.grid(column=1, row=1)


window.mainloop()