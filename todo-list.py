tasks=[]
def add_task():
    task=input("Enter a task:")

    if task.strip()=="":
        print("Task cannot be empty")
    else:
        tasks.append(task)
        print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks available")
    else:
        print("\n*****YOUR TASKS*****")

        for index,task in enumerate(tasks,start=1):
            print(f"{index}.{task}")

def remove_task():
    view_tasks()

    if not tasks:
        return
    try:
        task_number=int(input("Enter the task number to remove:"))
        if 1<=task_number<=len(tasks):
            removed_task=tasks.pop(task_number-1)
            print(f"Task removed:{removed_task}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

#main program
def main():
    while True:
        print("\n*****T0-DO LIST*****")
        print("1.Add Task")
        print("2.View Task")
        print("3.Remove Task")
        print("4.Exit")

        choice=input("Enter your choice:")
        if choice=="1":
            add_task()
        elif choice=="2":
            view_tasks()
        elif choice=="3":
            remove_task()
        elif choice=="4":
            print("Thank you for using the To-Do List!!!")
            break
        else:
            print("Invalid choice.Please try again.")

main()