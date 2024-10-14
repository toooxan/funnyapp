import tkinter as tk
import random
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Fun App")
root.geometry("400x400")

no = 0
max_no = 5


def move():
    global no
    no += 1
    if no < max_no:
        new_x = random.randint(50, 350)
        new_y = random.randint(50, 350)
        no_button.place(x=new_x, y=new_y)
    else:
        no_button.place_forget()


def image():

    root.withdraw()

    img_window = tk.Toplevel()
    img_window.title("Gotcha!")
    img_window.attributes('-fullscreen', True)

    img = Image.open("image.jpg")
    img = img.resize((1080, 920), Image.Resampling.LANCZOS)
    img_tk = ImageTk.PhotoImage(img)

    label = tk.Label(img_window, image=img_tk)
    label.image = img_tk  # Keep a reference to avoid garbage collection
    label.pack()

    img_window.bind("<Escape>", lambda event: root.destroy())


label = tk.Label(root, text="Lol?", font=("Times New Roman", 14))
label.pack(pady=20)

yes_button = tk.Button(root, text="Yes", font=("Times New Roman", 10), command=image, width=10)
yes_button.pack(pady=10)

no_button = tk.Button(root, text="No", font=("Times New Roman", 10), command=move, width=10)
no_button.pack(pady=10)

root.mainloop()
