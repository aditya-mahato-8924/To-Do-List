import os
import pandas as pd

CSV_PATH = r"To Do List CLI\tasks.csv"

def menu():
    while True:
        print("To Do List App")
        print("""
            1. Add Task.
            2. View Task.
            3. Mark Task as Done.
            4. Delete Task.
            5. Exit.
        """)

        # store user choice into user_input
        user_input = input("Enter your choice : ")

        if user_input == "1":
            add_task()
        elif user_input == "2":
            view_task()
        elif user_input == "3":
            is_task_completed()
        elif user_input == "4":
            delete_task()
        else:
            break

def get_task_counter():
    if os.path.exists(CSV_PATH) and os.path.getsize(CSV_PATH) > 0:
        df = pd.read_csv(CSV_PATH)
        if not df.empty:
            # extract last number from Task_ID (e.g., T005 -> 5)
            last_id = df["Task_ID"].iloc[-1]
            return int(last_id[1:]) + 1
    return 1  # if file empty or doesn't exist


def add_task():
    # access the global task counter
    global task_counter

    # enter the task name
    task_name = input("Enter your task : ")

    # set priority level
    priority_level = input("Enter the priority level (High, Medium or Low) : ")

    while priority_level not in ["High", "Medium", "Low"] or task_name == "":
        if task_name == "":
            print("No task entered, please try again!")
            task_name = input("Enter your task : ")
        
        if priority_level not in ["High", "Medium", "Low"]:
            print("Invalid priority level, please try again!")
            priority_level = input("Enter the priority level (High, Medium or Low) : ")

    # open tasks.csv
    task_df = pd.read_csv(r"To Do List CLI\tasks.csv")

    # assign task id to it, task name, priority and status by creating dictionary
    new_row = pd.DataFrame([{"Task_ID": f"T00{task_counter}", "Task_Name": task_name, "Priority": priority_level, "Status": "Pending"}])

    # add the new_row into task_df
    df = pd.concat([task_df, pd.DataFrame(new_row)], ignore_index=True)

    # save the task to existing file
    df.to_csv(r"To Do List CLI\tasks.csv", sep=",", mode="w", index=False)
    print(task_df)

    # update the task_counter by 1
    task_counter += 1

def view_task():
    # open tasks.csv
    task_df = pd.read_csv(r"To Do List CLI\tasks.csv")

    print(task_df)

def delete_task():
    # open tasks.csv
    task_df = pd.read_csv(r"To Do List CLI\tasks.csv")

    print("\n--- Current Tasks ---")
    print(task_df)

    task_id = input("Enter the Task_ID to delete: ")

    if task_id in task_df["Task_ID"].values:
        # drop the row
        task_df = task_df[task_df["Task_ID"] != task_id]
        # save back
        task_df.to_csv(r"To Do List CLI\tasks.csv", sep=",", mode="w", index=False)
        print(f"Task {task_id} deleted successfully!\n")
    else:
        print(f"Task {task_id} not found!")

    # show updated tasks
    print(task_df)

def is_task_completed():
    # open tasks.csv
    task_df = pd.read_csv(r"To Do List CLI\tasks.csv")

    print(task_df)

    task_id = input("Enter the Task_ID to mark as Done: ")

    if task_id in task_df["Task_ID"].values:
        # update status
        task_df.loc[task_df["Task_ID"] == task_id, "Status"] = "Done"
        # save back
        task_df.to_csv(r"To Do List CLI\tasks.csv", sep=",", mode="w", index=False)
        print(f"Task {task_id} marked as Done!\n")
    else:
        print(f"⚠ Task {task_id} not found!")

    # show updated tasks
    print(task_df)


if __name__ == "__main__":
    task_counter = get_task_counter()
    menu()