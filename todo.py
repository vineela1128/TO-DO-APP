from tkinter import *
from tkinter import messagebox

# Create main window
root = Tk()
root.title("To-Do List Application")
root.geometry("400x450")

# List to store tasks
tasks = []

# Functions
def add_task():
    task = task_entry.get()

    if task != "":
        tasks.append(task)
        task_listbox.insert(END, task)
        task_entry.delete(0, END)
    else:
        messagebox.showwarning("Warning", "Please enter a task")

def delete_task():
    try:
        selected = task_listbox.curselection()[0]
        task_listbox.delete(selected)
        tasks.pop(selected)
    except:
        messagebox.showwarning("Warning", "Select a task to delete")

def clear_tasks():
    if messagebox.askyesno("Confirm", "Delete all tasks?"):
        task_listbox.delete(0, END)
        tasks.clear()

# Heading
Label(root, text="To-Do List Application",
      font=("Arial", 16, "bold")).pack(pady=10)

# Entry box
task_entry = Entry(root, width=30, font=("Arial", 12))
task_entry.pack(pady=10)

# Add Button
Button(root, text="Add Task",
       command=add_task, width=15).pack(pady=5)

# Listbox
task_listbox = Listbox(root, width=40, height=12,
                       font=("Arial", 12))
task_listbox.pack(pady=10)

# Delete Button
Button(root, text="Delete Task",
       command=delete_task, width=15).pack(pady=5)

# Clear Button
Button(root, text="Clear All Tasks",
       command=clear_tasks, width=15).pack(pady=5)

# Run application
root.mainloop()