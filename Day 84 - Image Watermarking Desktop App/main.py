from tkinter import *
from tkinter import filedialog
from tkinter import colorchooser
from PIL import Image, ImageTk, ImageDraw, ImageFont
import os

watermarked_img = None
canvas = None
img = None
color_code = None

def open_image():
    global watermarked_img
    global canvas
    global img
    canvas = Canvas(width=3000, height=600, highlightthickness=0)
    fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image",
                                     filetypes=(("JPG File", "*.jpg"), ("PNG File", "*.png"), ("All Files", "*.*")))
    img = Image.open(fln)
    watermarked_img = img.copy()
    draw = ImageDraw.Draw(watermarked_img)
    font = ImageFont.truetype("arial.ttf", 25)
    draw.text((0, 0), watermark_text.get(), (0, 0, 0), font=font)
    resized_img = watermarked_img.resize((800, 600), Image.ANTIALIAS)
    new_img = ImageTk.PhotoImage(resized_img)
    canvas.create_image(470, 300, image=new_img)
    canvas.place(x=10, y=110)
    lbl.configure(image=new_img)
    lbl.image = new_img

def update_save():
    global watermarked_img
    global canvas
    global img
    global color_code
    watermarked_img = img.copy()
    draw = ImageDraw.Draw(watermarked_img)
    font = ImageFont.truetype('arial.ttf', int(clicked.get()))
    draw.text((tuple(map(int, coord.get().split(",")))), watermark_text.get(), color_code, font=font)
    resized_img = watermarked_img.resize((800, 600), Image.ANTIALIAS)
    new_img = ImageTk.PhotoImage(resized_img)
    canvas.create_image(470, 300, image=new_img)
    canvas.place(x=10, y=110)
    lbl.configure(image=new_img)
    lbl.image = new_img
    filename = filedialog.asksaveasfilename()
    if filename:
        watermarked_img.save(filename)

def choose_color():
    global color_code
    color_code = colorchooser.askcolor(title="Choose color")[1]

window = Tk()
window.title("Image Watermarking App")
window.config(padx=50, pady=50)
window.geometry("1024x768")

lbl = Label(window)

menubar = Menu(window)
nav = Menu(menubar, tearoff=0)
nav.add_command(label="Open New Image", command=open_image)
nav.add_command(label="Save as...")

nav.add_separator()

nav.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=nav)

add_watermark_text = Label(text="Add Watermark to Your Image", font=("Arial", 25))
add_watermark_text.place(x=250, y=-50)

coord_text = Label(text="Coordinates:")
coord_text.place(x=70, y=27)

coord = Entry(width=20)
coord.insert(0, "0,0")
coord.place(x=160, y=27)

font_size_text = Label(text="Font Size:")
font_size_text.place(x=300, y=26)

options = [x for x in range(200)]
clicked = IntVar()
clicked.set(0)
dropdown = OptionMenu(window, clicked, *options)
dropdown.place(x=370, y=21)

watermark_text = Entry(width=60)
watermark_text.insert(0, "Text")
watermark_text.place(x=470, y=27)

add_watermark_button = Button(text="Update and Save", width=14, command=update_save)
add_watermark_button.place(x=400, y=65)

color_button = Button(text="Select color", command=choose_color)
color_button.place(x=840, y=23)

window.config(menu=menubar)
window.mainloop()