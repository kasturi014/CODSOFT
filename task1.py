#TO-DO LIST
def add_task(tasks,task_description):
    """Add a new task to the list"""
    task_id = len(tasks) + 1
    tasks.append({"id":task_id,"description":task_description,"completed":False})
def list_tasks(tasks):
    """List all tasks with their completion status"""
    if not tasks:
        print("Task not found")
    for task in tasks:
        status="Done" if task["completed"] else "Not done"
        print(f"ID:{task['id']},Description:{task['description']}-{status}")
def update_task(tasks,task_id,new_description=None,completed=None):
    """update task description or completion status"""
    for task in tasks:
        if task['id']==task_id:
            if new_description is not None:
                task['description']=new_description
            if completed is not None:
                task['completed']=completed
            return
    print("Task ID not found")
def track_task(tasks,task_id):
    """track a specific task by ID"""
    for task in tasks:
        if task['id']==task_id:
            status="Done" if task["completed"] else "Not done"
            print(f"ID:{task['id']},Description:{task['description']}-{status}")
            return
    print("Task ID not found")
def main():
    tasks=[]
    while True:
        print("\nTo-Do list menu:")
        print("1.Add task")
        print("2.List tasks")
        print("3.Update task")
        print("4.Track task")
        print("5.Exit")
        choice=input("Enter your choice:")
        if choice =='1':
            task_description= input("Enter tha task description:")
            add_task(tasks,task_description)
        elif choice =='2':
            list_tasks(tasks)
        elif choice =='3':
            task_id= int(input("Enter the task ID to update:"))
            new_description= input("Enter new description(leave blank to keep current):")
            completed= input("Mark as completed?(y/n, leave blank to keep current):").lower()
            completed= True if completed == 'y' else False if completed == 'n' else None
            update_task(tasks,task_id,new_description or None,completed)
        elif choice =='4':
            task_id = int(input("Enter the task ID to track:"))
            track_task(tasks,task_id)
        elif choice =='5':
            print("Exit")
        else:
            print("Invalid choice")
if __name__ == "__main__":
    main()
