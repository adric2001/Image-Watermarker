import tkinter
import tkinter.ttk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter.filedialog import asksaveasfilename

window = Tk()
window.title("MarkItUp")
window.config(padx=50, pady=50)

canvas = Canvas(height=400, width=400)
image = Image.open('logo.png')
resize_image = image.resize((200, 200))
new_image = ImageTk.PhotoImage(resize_image)
canvas.create_image(200, 100, image=new_image)
canvas.grid(row=1, column=2)

image_path=StringVar()
watermark_path=StringVar()
static_watermark_path = None
static_image_path = None

def import_images():
    global static_image_path
    path = image_path.get()
    static_image_path = path

    if not path:
        messagebox.showerror('Error', 'No path has been entered.')
    else:
        messagebox.showinfo('Success', 'The image has been imported!')

def import_watermark():
    global static_watermark_path
    path = watermark_path.get()
    static_watermark_path = path

    if not path:
        messagebox.showerror('Error', 'No path has been entered.')
    else:
        messagebox.showinfo('Success', 'The watermark has been imported!')


def start():
    global static_image_path
    global static_watermark_path

    print(static_image_path)
    print(static_watermark_path)

    if not static_image_path and static_watermark_path:
        messagebox.showerror('Error', 'Missing path')
    else:
        base_img = Image.open(fr"{static_image_path}")
        watermark_img = Image.open(fr"{static_watermark_path}")
        watermark_img = watermark_img.resize(base_img.size)
        watermark_img = watermark_img.convert("RGBA")

        result_img = Image.new("RGBA", base_img.size)
        result_img = Image.alpha_composite(base_img.convert("RGBA"), watermark_img)

        data = [("Images Files", "*.png *jpg")]
        filename = asksaveasfilename(filetypes=data, defaultextension=data)
        if filename:
            result_img.save(filename)



app_label = Label(text="Welcome to MarkItUp!", font=("Arial", 20))
app_label.grid(row=0, column=2)

import_watermark_button = Button(text="Import Watermark", command=import_watermark)
import_watermark_button.grid(row=2, column=1)

import_images_button = Button(text="Import Image", command=import_images)
import_images_button.grid(row=2, column=4)

start_button = Button(text="Mark", command=start)
start_button.grid(row=2, column=2)

input_bar_image = Entry(textvariable=image_path)
input_bar_image.grid(row=3, column=4)
input_label_image = Label(text="Image Path:")
input_label_image.grid(row=3, column=3)

input_bar_watermark = Entry(textvariable=watermark_path)
input_bar_watermark.grid(row=3, column=1)
input_label_watermark = Label(text="Watermark Path:")
input_label_watermark.grid(row=3, column=0)



window.mainloop()




