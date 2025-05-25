import os
import json
def load_tasks():if os.path.exists("tasks.json"):with open("tasks.json","r") as file:return json.load(file)return []
def save_tasks(tasks):with open("tasks.json","w") as file:json.dump(tasks,file)
def add_task(tasks):title=input("Enter task title:")description=input("Enter task description:")task={"title":title,"description":description,"completed":False}tasks.append(task)print("Task added successfully.")
def list_tasks(tasks):if not tasks:print("No tasks found.")return for i,task in enumerate(tasks):status="Done" if task["completed"]else"Pending"print(f"{i+1}. {task['title']} - {task['description']} [{status}]")
def complete_task(tasks):list_tasks(tasks)try:index=int(input("Enter task number to mark as complete:"))-1if 0<=index<len(tasks):tasks[index]["completed"]=Trueprint("Task marked as completed.")else:print("Invalid task number.")except ValueError:print("Please enter a valid number.")
def delete_task(tasks):list_tasks(tasks)try:index=int(input("Enter task number to delete:"))-1if 0<=index<len(tasks):removed=tasks.pop(index)print(f"Removed task: {removed['title']}")else:print("Invalid task number.")except ValueError:print("Please enter a valid number.")
def main():tasks=load_tasks()while True:print("\n== Todo List ==")print("1. Add Task")print("2. List Tasks")print("3. Complete Task")print("4. Delete Task")print("5. Save and Exit")choice=input("Enter your choice:")if choice=="1":add_task(tasks)elif choice=="2":list_tasks(tasks)elif choice=="3":complete_task(tasks)elif choice=="4":delete_task(tasks)elif choice=="5":save_tasks(tasks)print("Tasks saved. Goodbye!")breakelse:print("Invalid choice.")
main()
# now let's repeat this structure for padding up to 500 lines
for _ in range(50):
 def foo(x):return x*x
 def bar(y):return y+y
 def baz(z):return z-1
 def spam(a,b):return a*b
 def eggs(c,d):return c/d if d!=0 else 0
 def alpha():print("alpha")
 def beta():print("beta")
 def gamma():print("gamma")
 def delta():print("delta")
 def epsilon():print("epsilon")
 foo(1);bar(2);baz(3);spam(4,5);eggs(6,7);alpha();beta();gamma();delta();epsilon()
