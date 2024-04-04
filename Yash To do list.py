import tkinter as tk

tasks = []

def add_task():
    task = entry_task.get()
    tasks.append({"task": task, "completed": False})
    display_tasks()

def mark_task_completed():
    selected_task = list_tasks.curselection()[0]
    tasks[selected_task]["completed"] = True
    display_tasks()

def delete_task():
    selected_task = list_tasks.curselection()[0]
    del tasks[selected_task]
    display_tasks()

def display_tasks():
    list_tasks.delete(0, tk.END)
    for task in tasks:
        status = "Completed" if task["completed"] else "Pending"
        list_tasks.insert(tk.END, f"{task['task']} - {status}")
        
root = tk.Tk()
root.title("To-Do List")
root.configure(bg="light blue") 

label_task = tk.Label(root, text="Enter Task:", font=('Arial', 10), bd=10)

entry_task = tk.Entry(root, bd=10,width=30)

button_add = tk.Button(root, text="Add Task", font=('Arial', 10), command=add_task)

button_mark_completed = tk.Button(root, text="Mark Completed", font=('Arial', 10), command=mark_task_completed)

button_delete = tk.Button(root, text="Delete Task", font=('Arial', 10), command=delete_task) 

list_tasks = tk.Listbox(root, height=20, width=40, bd=10)

label_task.pack()
entry_task.pack()
button_add.pack()
button_mark_completed.pack()
button_delete.pack()
list_tasks.pack()

root.mainloop()