import customtkinter as ctk
from tkinter import END, messagebox

def clear():
    entryField.delete(0, END)

def click(number):
    entryField.insert(END, number)

def answer():
    expression = entryField.get()
    try:
        result = eval(expression)
        ans = round(result, 2)
        entryField.delete(0, END)
        entryField.insert(0, ans)
    except SyntaxError:
        messagebox.showerror("Error", "Invalid expression")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero")

root = ctk.CTk()
root.title("Calculator")
root.geometry("320x340")
root.config(bg="#1e1e2f") 

entryField = ctk.CTkEntry(root, font=("Arial", 20, "bold"),
                          text_color="black", bg_color="#1e1e2f",
                          border_color="white", width=280, height=50)
entryField.grid(row=0, column=0, padx=10, pady=10, columnspan=4)

# Color palette
button_bg = "#2c2c3c"
text_white = "black"
accent_orange = "#ff9500"
accent_red = "#ff3b30"
accent_green = "#34c759"
accent_purple = "#5e5ce6"

# Buttons layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
    ('6', 2, 0), ('5', 2, 1), ('4', 2, 2), ('-', 2, 3),
    ('3', 3, 0), ('2', 3, 1), ('1', 3, 2), ('*', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('/', 4, 3),
    ('%', 5, 0), ('=', 5, 1, 3)
]

for btn in buttons:
    text = btn[0]
    row = btn[1]
    col = btn[2]
    colspan = btn[3] if len(btn) > 3 else 1

    if text == '=':
        fg = accent_green
        cmd = answer
    elif text == 'C':
        fg = accent_red
        cmd = clear
    elif text in ['+', '-', '*', '/', '%']:
        fg = accent_orange
        cmd = lambda x=text: click(x)
    else:
        fg = accent_purple
        cmd = lambda x=text: click(x)

    ctk.CTkButton(
        root,
        text=text,
        font=('Arial', 20, 'bold'),
        width=60 * colspan,
        height=40,
        fg_color=fg,
        hover_color="#444",
        bg_color="#1e1e2f",
        text_color=text_white,
        corner_radius=8,
        command=cmd
    ).grid(row=row, column=col, columnspan=colspan, padx=5, pady=5)

# Keyboard binding
def key_input(event):
    key = event.char
    if key in '0123456789.+-*/%':
        click(key)
    elif event.keysym == 'Return':
        answer()
    elif event.keysym in ['BackSpace', 'Delete']:
        current = entryField.get()
        entryField.delete(0, END)
        entryField.insert(0, current[:-1])
    elif key.lower() == 'c':
        clear()

root.bind('<Key>', key_input)
root.mainloop()
