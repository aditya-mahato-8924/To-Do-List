# 📝 Personal To-Do List Application (Python CLI)

A simple command-line application to manage daily tasks. Users can add tasks, view them, mark them as completed, and delete tasks. All tasks are stored in a CSV file to ensure persistence between sessions.

---

## 📌 Features
- Add new tasks with Task_ID, Date, Task_Name, Priority, Status
- Tasks are automatically sorted by priority (High → Medium → Low)
- View all tasks in a tabular format
- Mark tasks as **Done**
- Delete tasks by **Task_ID**
- View Pending tasks only
- View Completed tasks only
- Delete all completed tasks at once
- Persistent storage using **CSV file**

---

## 🔧 Prerequisites
- Python 3.8+ installed  
- Libraries:
  - `pandas`
  - `os` (built-in)

Install pandas if not installed:
```bash
pip install pandas
```

---

## 🚀 How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/todo-list-cli.git
   cd todo-list-cli
   ```

2. Run the program:
   ```bash
   python todo_cli.py
   ```

---

## 📂 Project Structure
```
todo-list-cli/
│
├── todo_cli.py        # Main CLI Application
├── tasks.csv          # Stores all tasks
└── README.md          # Project documentation
```

---

## 📖 Usage
- **Add Task** → Input task name and priority (High/Medium/Low).  
- **View Tasks** → Displays all tasks with details.  
- **Mark Task as Done** → Enter Task_ID to update status to Done.  
- **Delete Task** → Remove task by Task_ID.  
- **Exit** → Close the app.  

Example:
```
1. Add Task
2. View Task
3. Mark Task as Done
4. Delete Task
5. View Pending Task.
6. View Completed Task.
7. Delete all Completed Task.
8. Exit.
```

---

## ✅ Example Workflow
```
Enter your choice: 1
Enter your task: Submit assignment
Enter the priority level (High, Medium or Low): High
✅ Task added successfully!

Enter your choice: 2
  Task_ID   Date     Task_Name Priority   Status
0    T001  10.09.2025 Submit assignment    High  Pending
```

---

## 🎯 Future Improvements
- Add due dates for tasks  
- Export completed tasks history  

---
