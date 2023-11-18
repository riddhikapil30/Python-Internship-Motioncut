import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")

        # Task list
        self.tasks = []

        #GUI elements
        self.task_label = tk.Label(master, text="Task:")
        self.task_entry = tk.Entry(master, width=30)
        self.due_date_label = tk.Label(master, text="Due Date:")
        self.due_date_entry = tk.Entry(master, width=10)
        self.priority_label = tk.Label(master, text="Priority:")
        self.priority_entry = tk.Entry(master, width=10)

        #Buttons
        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.display_button = tk.Button(master, text="Display Tasks", command=self.display_tasks)
        self.complete_button = tk.Button(master, text="Mark Completed", command=self.mark_completed)
        self.update_button = tk.Button(master, text="Update Task", command=self.update_task)
        self.remove_button = tk.Button(master, text="Remove Task", command=self.remove_task)

        #layout
        self.task_label.grid(row=0, column=0, padx=5, pady=5)
        self.task_entry.grid(row=0, column=1, padx=5, pady=5)
        self.due_date_label.grid(row=0, column=2, padx=5, pady=5)
        self.due_date_entry.grid(row=0, column=3, padx=5, pady=5)
        self.priority_label.grid(row=0, column=4, padx=5, pady=5)
        self.priority_entry.grid(row=0, column=5, padx=5, pady=5)

        self.add_button.grid(row=1, column=0, padx=5, pady=5)
        self.display_button.grid(row=1, column=1, padx=5, pady=5)
        self.complete_button.grid(row=1, column=2, padx=5, pady=5)
        self.update_button.grid(row=1, column=3, padx=5, pady=5)
        self.remove_button.grid(row=1, column=4, padx=5, pady=5)

    def add_task(self):
        task_description = self.task_entry.get()
        due_date = self.due_date_entry.get()
        priority = self.priority_entry.get()
        task = {"description": task_description, "due_date": due_date, "priority": priority, "completed": False}
        self.tasks.append(task)
        messagebox.showinfo("Task Added", "Task added successfully!")

    def display_tasks(self):
        if not self.tasks:
            messagebox.showinfo("No Tasks", "No tasks available.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                task_info = f"{i}. Description: {task['description']}, Due Date: {task['due_date']}, Priority: {task['priority']}, Completed: {task['completed']}"
                print(task_info)

    def mark_completed(self):
        index = self.get_task_index()
        if index is not None:
            self.tasks[index]["completed"] = True
            messagebox.showinfo("Task Completed", "Task marked as completed!")

    def update_task(self):
        index = self.get_task_index()
        if index is not None:
            new_description = self.task_entry.get()
            new_due_date = self.due_date_entry.get()
            new_priority = self.priority_entry.get()

            self.tasks[index]["description"] = new_description
            self.tasks[index]["due_date"] = new_due_date
            self.tasks[index]["priority"] = new_priority

            messagebox.showinfo("Task Updated", "Task updated successfully!")

    def remove_task(self):
        index = self.get_task_index()
        if index is not None:
            del self.tasks[index]
            messagebox.showinfo("Task Removed", "Task removed successfully!")

    def get_task_index(self):
        try:
            index = int(input("Enter the task number: ")) - 1
            if 0 <= index < len(self.tasks):
                return index
            else:
                messagebox.showerror("Invalid Index", "Invalid task number. Please try again.")
                return None
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
            return None


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
