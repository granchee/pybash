#!/usr/bin/env python

import tkinter as tk
# from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import ImageTk, Image

# border_effects = {
#     "flat": tk.FLAT,
#     "sunken": tk.SUNKEN,
#     "raised": tk.RAISED,
#     "groove": tk.GROOVE,
#     "ridge": tk.RIDGE,
# }

# def increase():
#     value = int(lbl_value["text"])
#     lbl_value["text"] = f"{value + 1}"


# def decrease():
#     value = int(lbl_value["text"])
#     lbl_value["text"] = f"{value - 1}"

# def open_file():
#     """Open a file for editing."""
#     filepath = askopenfilename(
#         filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
#     )
#     if not filepath:
#         return
#     txt_edit.delete("1.0", tk.END)
#     with open(filepath, "r") as input_file:
#         text = input_file.read()
#         txt_edit.insert(tk.END, text)
#     window.title(f"Simple Text Editor - {filepath}")

# def save_file():
#     """Save the current file as a new file."""
#     filepath = asksaveasfilename(
#         defaultextension="txt",
#         filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
#     )
#     if not filepath:
#         return
#     with open(filepath, "w") as output_file:
#         text = txt_edit.get("1.0", tk.END)
#         output_file.write(text)
#     window.title(f"Simple Text Editor - {filepath}")

window = tk.Tk()
# @todo window.title() skips in ChromeOS!
# window.title("Decrease-Increase")
# window.title("Simple Text Editor")
window.title("pybash Proof-of-Concept")

# for relief_name, relief in border_effects.items():
#     frame = tk.Frame(master=window, relief=relief, borderwidth=5)
#     frame.pack(side=tk.LEFT)
#     label = tk.Label(master=frame, text=relief_name)
#     label.pack()

# frame1 = tk.Frame(master=window, width=200, height=100, bg="red")
# frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

# frame2 = tk.Frame(master=window, width=100, bg="yellow")
# frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

# frame3 = tk.Frame(master=window, width=50, bg="blue")
# frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

# for i in range(3):
#     window.columnconfigure(i, weight=1, minsize=100)
#     window.rowconfigure(i, weight=1, minsize=50)

#     for j in range(3):
#         frame = tk.Frame(
#             master=window,
#             relief=tk.RAISED,
#             borderwidth=1
#         )
#         frame.grid(row=i, column=j) # @todo padx=5, pady=5 
#         label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
#         label.pack(padx=5, pady=5)

# window.rowconfigure(0, minsize=50, weight=1)
# window.columnconfigure([0, 1, 2], minsize=50, weight=1)

# btn_decrease = tk.Button(master=window, text="-", command=decrease)
# btn_decrease.grid(row=0, column=0, sticky="nsew")

# lbl_value = tk.Label(master=window, text="0")
# lbl_value.grid(row=0, column=1)

# btn_increase = tk.Button(master=window, text="+", command=increase)
# btn_increase.grid(row=0, column=2, sticky="nsew")

# window.rowconfigure(0, minsize=800, weight=1)
# window.columnconfigure(1, minsize=800, weight=1)

# txt_edit = tk.Text(window)
# fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
# btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
# btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)

# btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
# btn_save.grid(row=1, column=0, sticky="ew", padx=5)

# fr_buttons.grid(row=0, column=0, sticky="ns")
# txt_edit.grid(row=0, column=1, sticky="nsew")

# Use tkinter to create a window to display a 240x240 image (size of Pimoroni ST7789 LCD).
# Image to be window onto larger 240x? image representing console history.
# Use up- and down-arrows to navigate history line-by-line. (Pixel-wise?)
# Multiple history images if size becomes non-performant?
# Later: write image to LCD using ST7789 library.
# Later: any typing brings focus back to window at bottom of history with prompt, typed character, cursor.
# Later: typing return adds command and response to history.
# Later: long command (more than 240 pixels) treated like nano?
# Later: long response either clipped at 240 pixels (with ellipsis) or wrapped?
# Later: use subprocess.run() to get all of bash without reimplementing bash?

WIDTH = 500
HEIGHT = 500
canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("poc.png"))
# canvas.create_image(5, 5, anchor="nw", image=img) # @todo Default anchor is tk.CENTER, needing sensible x and y
canvas.create_image(WIDTH/2, HEIGHT/2, image=img) # @todo Only centres horizontally?
window.mainloop()
