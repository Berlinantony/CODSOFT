import tkinter as tk
from tkinter import messagebox

class SimpleTodo:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")
        self.master.geometry("450x500")
        self.master.configure(bg="white")
        self.tasks = []
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="MY TASK LIST", font=("Helvetica", 18, "bold"),
                 fg="black", bg="white").pack(pady=15)

        entry_frame = tk.Frame(self.master, bg="white")
        entry_frame.pack(pady=5)

        self.task_entry = tk.Entry(entry_frame, width=30, font=("Arial", 12),
                                   bg="#f2f2f2", fg="black", bd=1, relief="solid")
        self.task_entry.grid(row=0, column=0, padx=5)

        tk.Button(entry_frame, text="Add", command=self.add_task,
                  font=("Arial", 10), bg="black", fg="white", width=10).grid(row=0, column=1, padx=5)

        list_frame = tk.Frame(self.master, bg="white")
        list_frame.pack(pady=10)

        self.listbox = tk.Listbox(list_frame, width=40, height=12, font=("Arial", 11),
                                  bg="#f7f7f7", fg="black", selectbackground="gray", relief="solid")
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)

        btn_frame = tk.Frame(self.master, bg="white")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Mark Done", command=self.mark_done,
                  font=("Arial", 10), bg="black", fg="white", width=12).grid(row=0, column=0, padx=5)

        tk.Button(btn_frame, text="Delete Task", command=self.delete_task,
                  font=("Arial", 10), bg="black", fg="white", width=12).grid(row=0, column=1, padx=5)

        tk.Button(btn_frame, text="Clear All", command=self.clear_all,
                  font=("Arial", 10), bg="black", fg="white", width=12).grid(row=0, column=2, padx=5)

        tk.Label(self.master, text="Developed by M BERLIN - URK24CS9013",
                 font=("Arial", 9), fg="gray", bg="white").pack(side=tk.BOTTOM, pady=10)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            display = f"☐ {task}"
            self.tasks.append(display)
            self.listbox.insert(tk.END, display)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Empty Field", "Please enter a task.")

    def delete_task(self):
        try:
            index = self.listbox.curselection()[0]
            self.listbox.delete(index)
            del self.tasks[index]
        except IndexError:
            messagebox.showerror("No Selection", "Please select a task to delete.")

    def clear_all(self):
        if messagebox.askyesno("Confirmation", "Clear all tasks?"):
            self.listbox.delete(0, tk.END)
            self.tasks.clear()

    def mark_done(self):
        try:
            index = self.listbox.curselection()[0]
            current = self.tasks[index]
            if current.startswith("☐"):
                updated = current.replace("☐", "✔", 1)
            else:
                updated = current.replace("✔", "☐", 1)
            self.tasks[index] = updated
            self.listbox.delete(index)
            self.listbox.insert(index, updated)
        except IndexError:
            messagebox.showinfo("Select a Task", "Click a task to mark it done.")

root = tk.Tk()
app = SimpleTodo(root)
root.mainloop()
