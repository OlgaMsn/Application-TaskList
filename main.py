import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        list_task_box.insert(tk.END, task)
        task_entry.delete(0, tk.END)
def delite_task():
    selected_task = list_task_box.curselection()
    if selected_task:
        list_task_box.delete(selected_task)

def mark_task():
    selected_task = list_task_box.curselection()
    if selected_task:
        list_task_box.itemconfig(selected_task, bg="aquamarine4", fg="white")

root = tk.Tk()
root.title("Task list")
root.configure(background="aquamarine")

text1 = tk.Label(root, text="Введите вашу задачу", bg="aquamarine")
text1.pack(pady=5)

task_entry = tk.Entry(root, width=20, bg="azure2")
task_entry.pack(pady=10, padx=10)

buttom_add_task = tk.Button(root, text="Добавить задачу", command=add_task)
buttom_add_task.pack(pady=10)

buttom_delite_task = tk.Button(root, text="Удалить задачу", command=delite_task)
buttom_delite_task.pack(pady=10)

buttom_mark_task = tk.Button(root, text="Отметить, что задача выполнена", command=mark_task)
buttom_mark_task.pack(pady=10)

text2 = tk.Label(root, text="Список задач", bg="aquamarine")
text2.pack(pady=5)

list_task_box = tk.Listbox(root, height=10, width=50, bg="azure3")
list_task_box.pack(pady=10, padx=10)

root.mainloop()