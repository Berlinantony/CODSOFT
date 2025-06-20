import tkinter as tk
from tkinter import messagebox

def display_result(value):
    result.set(f"{value}")

def add():
    try:
        total = float(entry1.get()) + float(entry2.get())
        display_result(total)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers")

def subtract():
    try:
        total = float(entry1.get()) - float(entry2.get())
        display_result(total)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers")

def multiply():
    try:
        total = float(entry1.get()) * float(entry2.get())
        display_result(total)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers")

def divide():
    try:
        val2 = float(entry2.get())
        if val2 == 0:
            messagebox.showerror("Math Error", "Cannot divide by zero")
        else:
            total = float(entry1.get()) / val2
            display_result(total)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers")

root = tk.Tk()
root.title("Calculator")
root.geometry("350x280")
root.configure(bg="white")

tk.Label(root, text="CALCULATOR", font=("Arial", 16, "bold"), bg="white", fg="black").grid(row=0, column=0, columnspan=2, pady=15)

tk.Label(root, text="Enter Number 1:", font=("Arial", 11), bg="white").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry1 = tk.Entry(root, width=25, font=("Arial", 11), bg="#f1f1f1", fg="black")
entry1.grid(row=1, column=1, pady=5)

tk.Label(root, text="Enter Number 2:", font=("Arial", 11), bg="white").grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry2 = tk.Entry(root, width=25, font=("Arial", 11), bg="#f1f1f1", fg="black")
entry2.grid(row=2, column=1, pady=5)

btn_frame = tk.Frame(root, bg="white")
btn_frame.grid(row=3, column=0, columnspan=2, pady=10)

btn_style = {"bg": "black", "fg": "white", "width": 5, "font": ("Arial", 11)}

tk.Button(btn_frame, text="+", command=add, **btn_style).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="-", command=subtract, **btn_style).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="×", command=multiply, **btn_style).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="÷", command=divide, **btn_style).grid(row=0, column=3, padx=5)

tk.Label(root, text="Result:", font=("Arial", 11), bg="white").grid(row=4, column=0, padx=10, pady=10, sticky="e")
result = tk.StringVar()
result_entry = tk.Entry(root, textvariable=result, state="readonly", width=28, font=("Arial", 11), bg="#f1f1f1")
result_entry.grid(row=4, column=1)

tk.Label(root, text="M BERLIN - URK24CS9013", font=("Arial", 8), bg="white", fg="gray").grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()
