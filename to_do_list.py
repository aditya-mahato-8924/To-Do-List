import os
import pandas as pd
from datetime import datetime
import warnings

warnings.filterwarnings("ignore")

CSV_PATH = r"tasks.csv"

# menu of the app
def menu():
    while True:
        print("To Do List App")
        print("""
            1. Add Task.
            2. View Task.
            3. Mark Task as Done.
            4. Delete Task.
            5. View Pending Task.
            6. View Completed Task.
            7. Delete all Completed Task.
            8. Exit.
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
        elif user_input == "5":
            view_pending_task()
        elif user_input == "6":
            view_completed_task()
        elif user_input == "7":
            delete_all_completed_task()
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

# add task
def add_task():
    # access the global task counter
    global task_counter

    # enter the task name
    task_name = input("Enter your task : ")

    # set priority level
    priority_level = input("Enter the priority level (High, Medium or Low) : ")

    while priority_level not in ["High", "Medium", "Low"] or task_name == "":
        if task_name == "":
            print("\nNo task entered, please try again!\n")
            task_name = input("Enter your task : ")
        
        if priority_level not in ["High", "Medium", "Low"]:
            print("\nInvalid priority level, please try again!\n")
            priority_level = input("Enter the priority level (High, Medium or Low) : ")

    today_date = datetime.now().strftime(r"%d.%m.%Y")

    # open tasks.csv
    task_df = pd.read_csv(CSV_PATH)

    # assign task id to it, task name, priority and status by creating dictionary
    new_row = pd.DataFrame([{"Task_ID": f"T00{task_counter}", 
                             "Date": today_date,
                             "Task_Name": task_name, 
                             "Priority": priority_level,
                             "Status": "Pending"}])

    # add the new_row into task_df
    df = pd.concat([task_df, pd.DataFrame(new_row)], ignore_index=True)

    # sort the task according to the priority level
    priority_order = {"High": 1, "Medium": 2, "Low": 3}
    df["Priority_Sort"] = df["Priority"].map(priority_order)
    df = df.sort_values(by=["Priority_Sort"]).drop(columns=["Priority_Sort"])

    # save the task to existing file
    df.to_csv(CSV_PATH, sep=",", mode="w", index=False)
    print("\nTask added successfully!\n")

    # update the task_counter by 1
    task_counter += 1

# view the task
def view_task():
    # open tasks.csv
    task_df = pd.read_csv(CSV_PATH)

    if task_df.empty:
        print("\nNo Task is assigned yet!\n")
        return

    print(task_df)

# delete the task
def delete_task():
    # open tasks.csv
    task_df = pd.read_csv(CSV_PATH)
    
    if task_df.empty:
        print("\nNo Task is assigned yet!\n")
        return

    print("\n--- Current Tasks ---\n")
    print(task_df)

    task_id = input("Enter the Task_ID to delete: ")

    if task_id in task_df["Task_ID"].values:
        # drop the row
        task_df = task_df[task_df["Task_ID"] != task_id]
        # save back
        task_df.to_csv(CSV_PATH, sep=",", mode="w", index=False)
        print(f"Task {task_id} deleted successfully!\n")
    else:
        print(f"\nTask {task_id} not found!\n")

    # show updated tasks
    print(task_df)

# marking the task completed
def is_task_completed():
    # open tasks.csv
    task_df = pd.read_csv(CSV_PATH)

    if task_df.empty:
        print("\nNo Task is assigned yet!\n")
        return

    print(task_df)

    task_id = input("Enter the Task_ID to mark as Done: ")

    if task_id in task_df["Task_ID"].values:
        # update status
        task_df.loc[task_df["Task_ID"] == task_id, "Status"] = "Done"
        # save back
        task_df.to_csv(CSV_PATH, sep=",", mode="w", index=False)
        print(f"\nTask {task_id} marked as Done!\n")
    else:
        print(f"\n⚠ Task {task_id} not found!\n")

    # show updated tasks
    print(task_df)

# view the pending task
def view_pending_task():
    # load the dataframe
    df = pd.read_csv(CSV_PATH)

    # check whether the dataframe is empty or not
    if df.empty:
        print("\nNo Task is assigned yet!\n")
        return
    else:
        # filter the dataframe and choose only those task which have Status value = "Pending"
        filtered_df = df[df["Status"] == "Pending"]

        if filtered_df.empty:
            print("\nNo Task is pending yet!\n")
        else:
            priority_order = {"High": 1, "Medium": 2, "Low": 3}
            filtered_df["Priority_Sort"] = filtered_df["Priority"].map(priority_order)
            filtered_df = filtered_df.sort_values(by=["Priority_Sort"]).drop(columns=["Priority_Sort"])
            print(filtered_df)

# view the completed task
def view_completed_task():
    # load the dataframe
    df = pd.read_csv(CSV_PATH)

    # check whether the dataframe is empty or not
    if df.empty:
        print("\nNo Task is assigned yet!\n")
        return
    else:
        # filter the dataframe and choose only those task which have Status value = "Done"
        filtered_df = df[df["Status"] == "Done"]
        
        if filtered_df.empty:
            print("\nNo Task is completed yet!\n")
        else:
            print(filtered_df.sort_values(by="Priority"))

# delete all completed task
def delete_all_completed_task():
    # load the csv file into dataframe
    df = pd.read_csv(CSV_PATH)

    if not df.empty:
        # now store only those task whose status value is pending
        df = df[df["Status"] != "Done"]

        # store into the csv file
        df.to_csv("tasks.csv", sep=",", mode="w", index=False)
    else:
        print("\nNo Task is assigned yet!\n")

if __name__ == "__main__":
    task_counter = get_task_counter()
    menu()