import tkinter as tk
from tkinter import messagebox, filedialog

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x600")
        self.root.config(bg="#f0f4f7")  # Light background

        self.tasks = []

        self.heading = tk.Label(root, text="📝 To-Do List", font=("Helvetica", 18, "bold"), bg="#f0f4f7", fg="#333")
        self.heading.pack(pady=10)

        self.task_entry = tk.Entry(root, font=("Helvetica", 14), bg="#e8e8e8", fg="#000")
        self.task_entry.pack(pady=10, padx=20, fill=tk.X)
        self.task_entry.bind("<Return>", self.add_task_event)

        self.add_button = tk.Button(root, text="Add Task", font=("Helvetica", 12), bg="#007acc", fg="white", command=self.add_task)
        self.add_button.pack(pady=5)

        self.update_button = tk.Button(root, text="Update Selected", font=("Helvetica", 12), bg="#007acc", fg="white", command=self.update_task)
        self.update_button.pack(pady=5)

        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, font=("Helvetica", 12), height=12, bg="white", fg="#000")
        self.task_listbox.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        self.delete_button = tk.Button(root, text="Delete Selected", font=("Helvetica", 12), bg="#d9534f", fg="white", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.save_button = tk.Button(root, text="Save Tasks", font=("Helvetica", 12), bg="#5cb85c", fg="white", command=self.save_tasks)
        self.save_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task == "":
            messagebox.showwarning("Warning", "Please enter a task")
        else:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def add_task_event(self, event):
        self.add_task()

    def update_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            updated_task = self.task_entry.get().strip()
            if updated_task == "":
                messagebox.showwarning("Warning", "Please enter a task to update")
            else:
                self.tasks[selected_index] = updated_task
                self.task_listbox.delete(selected_index)
                self.task_listbox.insert(selected_index, updated_task)
                self.task_entry.delete(0, tk.END)
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to update")

    def delete_task(self):
        try:
            selected = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected)
            del self.tasks[selected]
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete")

    def save_tasks(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                for task in self.tasks:
                    file.write(task + "\n")
            messagebox.showinfo("Saved", "Tasks saved successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
