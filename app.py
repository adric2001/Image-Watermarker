from tkinter import *
from PIL import Image, ImageTk


window = Tk()
window.title("MarkItUp")
window.config(padx=50, pady=50)

canvas = Canvas(height=400, width=400)
image = Image.open('logo.png')
resize_image = image.resize((100, 100))
new_image = ImageTk.PhotoImage(resize_image)
canvas.create_image(200, 100, image=new_image)
canvas.grid(row=1, column=1)

app_label = Label(text="Welcome to MarkItUp!", font=("Arial", 20))
app_label.grid(row=0, column=1)


window.mainloop()




