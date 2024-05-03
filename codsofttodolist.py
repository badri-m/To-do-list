import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("To-Do List")

        # Create listbox to display tasks
        self.task_listbox = tk.Listbox(self.root, width=50, height=15, font=("Arial", 12), selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        # Create entry for new task
        self.new_task_entry = tk.Entry(self.root, width=50, font=("Arial", 12))
        self.new_task_entry.pack()

        # Buttons
        self.add_button = tk.Button(self.root, text="Add Task", width=20, command=self.add_task)
        self.add_button.pack(pady=5)

        self.complete_button = tk.Button(self.root, text="Mark Complete", width=20, command=self.complete_task)
        self.complete_button.pack()

        self.delete_button = tk.Button(self.root, text="Delete Task", width=20, command=self.delete_task)
        self.delete_button.pack()

        self.save_button = tk.Button(self.root, text="Save Tasks", width=20, command=self.save_tasks)
        self.save_button.pack()

        self.load_button = tk.Button(self.root, text="Load Tasks", width=20, command=self.load_tasks)
        self.load_button.pack()

        # Load tasks from file if available
        self.tasks = []
        self.load_tasks()

        self.update_listbox()

        self.root.mainloop()

    def add_task(self):
        new_task = self.new_task_entry.get()
        if new_task:
            self.tasks.append(new_task)
            self.new_task_entry.delete(0, tk.END)
            self.update_listbox()

    def complete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            task = self.tasks[index]
            self.tasks[index] = "✓ " + task
            self.update_listbox()

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.tasks[index]
            self.update_listbox()

    def save_tasks(self):
        try:
            with open("tasks.txt", "w") as file:
                for task in self.tasks:
                    file.write(task + "\n")
            messagebox.showinfo("Save", "Tasks saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                self.tasks = [line.strip() for line in file.readlines()]
            self.update_listbox()
            messagebox.showinfo("Load", "Tasks loaded successfully!")
        except FileNotFoundError:
            messagebox.showinfo("Load", "No tasks found.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    TodoListApp()