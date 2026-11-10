import random
import tkinter as tk
from tkinter import messagebox


def generate_key():
    user_input = entry_input.get().strip()

    if not user_input.isdigit() or len(user_input) != 6:
        messagebox.showerror("Error", "Enter a valid 6-digit DEC number!")
        return

    first_half = user_input[0:3]
    second_half = user_input[3:6]
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    block1_list = list(second_half) + [random.choice(letters) for _ in range(2)]
    random.shuffle(block1_list)
    block1 = "".join(block1_list)

    block2_list = list(first_half) + [random.choice(letters) for _ in range(2)]
    random.shuffle(block2_list)
    block2 = "".join(block2_list)

    num1_digits = [char for char in block1 if char.isdigit()]
    num2_digits = [char for char in block2 if char.isdigit()]
    num1_shuffled = int("".join(num1_digits))
    num2_shuffled = int("".join(num2_digits))

    sum_result = num1_shuffled + num2_shuffled
    block3 = f"{sum_result:04d}"

    final_key = f"{block1}-{block2} {block3}"

    entry_result.config(state="normal")
    entry_result.delete(0, tk.END)
    entry_result.insert(0, final_key)
    entry_result.config(state="readonly")



root = tk.Tk()
root.title("Keygen")

window_width = 256
window_height = 256
root.geometry(f"{window_width}x{window_height}")
root.resizable(False, False)

bg_image = tk.PhotoImage(file="background.png")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

label_input = tk.Label(root, text="Enter 6-digit number:")
label_input.place(x=15, y=10)
entry_input = tk.Entry(root, justify="center", width=12)
entry_input.place(x=15, y=30)
btn_generate = tk.Button(root, text="GENERATE", command=generate_key)
btn_generate.place(x=150, y=20)
entry_result = tk.Entry(root, justify="center", width=24, state="readonly")
entry_result.place(x=50, y=220)

root.mainloop()
