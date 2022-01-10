from tkinter import *
from timeit import default_timer as timer
import random

word_list = ["başka", "örgüt", "üretim", "meclis", "düşünce", "zevk", "bitmek", "yukarıda", "yalnızca", "belli",
             "soğuk", "art", "besin", "ad", "birey", "seyretmek", "yapmak", "tam", "vitamin", "anlayış", "unutmak",
             "güvenlik", "gider", "toplum", "üzerine", "çeşit", "yeni", "işte", "laf", "derece", "anlatmak", "sol",
             "dışarı", "artırmak", "tutulmak", "ilgili", "ayırmak", "yaklaşık"]

score = 0

def check_word(e):
    global score
    if type_area.get() == word.cget("text"):
        word.config(text = random.choice(word_list))
        score += 1
        type_area.delete(0, "end")

def finish_game():
    end = timer()
    minute = round(end - start) // 60
    if end - start < 60:
        scoreboard.config(text = f"Yazılan Kelime Sayısı : {score}\nGeçen Süre : {round(end - start)} Saniye")
    else:
        scoreboard.config(text=f"Yazılan Kelime Sayısı : {score}\nGeçen Süre : {minute} Dakika {round(end - start) - (60 * minute)} Saniye")

start = timer()
window = Tk()
window.title("On Parmak Hız Testi")
window.config(padx=50, pady=50)
window.geometry("600x350")

word = Label(window, text=random.choice(word_list), font="times 20")
word.grid(row=0, column=0, pady=10)

type_area = Entry(width=80)
type_area.grid(row=1, column=0, sticky="w", ipady=5)

check_button = Button(text="Kontrol", pady=5, padx=20, command = check_word)
check_button.grid(row=2, column=0, pady=10)

finish_button = Button(text="Testi Bitir", pady=5, padx=20, command = finish_game)
finish_button.grid(row=3, column=0, pady=10)

scoreboard = Label(window, text="", font="times 20")
scoreboard.grid(row=4, column=0, pady=5)

window.bind("<Return>", check_word)
window.mainloop()
