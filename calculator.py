import tkinter as tk
from PIL import Image, ImageTk
import os

def on_button_click(data):
    if data == 'clear.png':
        result_var.set('')
    elif data == 'equal.png':
        try:
            result = str(eval(result_var.get()))
            result_var.set(result)
        except Exception as e:
            result_var.set('Error')
    else:
        current_text = result_var.get()
        result_var.set(current_text + str(data))

root = tk.Tk()
root.title("calculator")
result_var = tk.StringVar()
entry = tk.Entry(root, textvariable=result_var, font=('Arial', 30), justify='right', background="grey",fg="white")
entry.grid(row=0, column=0, columnspan=5, sticky='nsew')

buttons = [
    ("7.png", 1, 0, 7), ("8.png", 1, 1, 8), ("9.png", 1, 2, "9"), ("divide.png", 1, 3, '/'),
    ("4.png", 2, 0, 4), ("5.png", 2, 1, 5), ("6.png", 2, 2, 6), ("multiply.png", 2, 3, '*'),
    ("1.png", 3, 0, 1), ("2.png", 3, 1, 2), ("3.png", 3, 2, 3), ("minus.png", 3, 3, '-'),
    ("0.png", 4, 0, 0), ("clear.png", 4, 1,"clear.png"), ("equal.png", 4, 2,"equal.png"), ("plus.png", 4, 3, '+')
]

for (filename, row, col, data) in buttons:
    if filename != "NULL": 
        image_path = os.path.join("C:\\Users\\hp\\OneDrive\\Desktop\\code_clause", filename)
        image = Image.open(image_path)
        image=image.resize((100,100))
        image = ImageTk.PhotoImage(image)
        btn = tk.Button(root, image=image, command=lambda d=data: on_button_click(d), bg="black", activebackground="grey")
        btn.image = image
        btn.grid(row=row, column=col, sticky='nsew')

root.mainloop()
