import tkinter as tk
from tkinter import messagebox, Scrollbar

class FancyToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fancy To-Do List App")
        self.root.geometry("400x400")
        self.root.configure(bg="#f0f0f0") 

        # List to store tasks
        self.tasks = []

        # Create the UI elements
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        title_label = tk.Label(self.root, text="To-Do List", font=("Helvetica", 16, "bold"), bg="#f0f0f0", fg="#333")
        title_label.pack(pady=10)

        # Task entry field
        self.task_entry = tk.Entry(self.root, width=30, font=("Helvetica", 12), bd=2)
        self.task_entry.pack(pady=10)

        # Add task button
        self.add_button = tk.Button(self.root, text="Add Task", width=15, font=("Helvetica", 10, "bold"), bg="#5cb85c", fg="white", command=self.add_task)
        self.add_button.pack(pady=5)

        # Scrollable task list
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        self.task_listbox = tk.Listbox(frame, width=40, height=8, font=("Helvetica", 12), bd=2, relief="solid", selectbackground="#5cb85c")
        self.task_listbox.pack(side="left", fill="y")

        scrollbar = Scrollbar(frame, orient="vertical")
        scrollbar.pack(side="right", fill="y")
        self.task_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.task_listbox.yview)

        # Mark as completed button
        self.complete_button = tk.Button(self.root, text="Mark Completed", width=15, font=("Helvetica", 10, "bold"), bg="#0275d8", fg="white", command=self.mark_completed)
        self.complete_button.pack(pady=5)

        # Edit selected task button
        self.edit_button = tk.Button(self.root, text="Edit Task", width=15, font=("Helvetica", 10, "bold"), bg="#f0ad4e", fg="white", command=self.edit_task)
        self.edit_button.pack(pady=5)

        # Remove completed tasks button
        self.remove_button = tk.Button(self.root, text="Remove Completed", width=15, font=("Helvetica", 10, "bold"), bg="#d9534f", fg="white", command=self.remove_completed)
        self.remove_button.pack(pady=5)

    def add_task(self):
        """Add a new task to the list"""
        task_desc = self.task_entry.get()
        if task_desc:
            self.tasks.append({"description": task_desc, "completed": False})
            self.task_entry.delete(0, tk.END)  # Clear the input field
            self.update_task_list()
        else:
            messagebox.showwarning("Input Error", "Task description cannot be empty!")

    def mark_completed(self):
        """Mark the selected task as completed"""
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            self.tasks[task_index]['completed'] = True
            self.update_task_list()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to mark as completed!")

    def edit_task(self):
        """Edit the selected task"""
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            new_task_desc = self.task_entry.get()
            if new_task_desc:
                self.tasks[task_index]['description'] = new_task_desc
                self.task_entry.delete(0, tk.END)
                self.update_task_list()
                messagebox.showinfo("Task Edited", "Task updated successfully!")
            else:
                messagebox.showwarning("Input Error", "New task description cannot be empty!")
        else:
            messagebox.showwarning("Selection Error", "Please select a task to edit!")

    def remove_completed(self):
        """Remove all completed tasks from the list"""
        self.tasks = [task for task in self.tasks if not task['completed']]
        self.update_task_list()

    def update_task_list(self):
        """Update the task listbox to display the current tasks"""
        self.task_listbox.delete(0, tk.END)  # Clear the listbox
        for task in self.tasks:
            status = "✓" if task['completed'] else "✗"
            self.task_listbox.insert(tk.END, f"{task['description']} [{status}]")

if __name__ == "__main__":
    root = tk.Tk()
    app = FancyToDoApp(root)
    root.mainloop()
