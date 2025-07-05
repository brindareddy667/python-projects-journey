#to-do list
todo_list=[]
print("TO-DO MENU")
print("1.ADD TASKS")
print("2.VIEW TASKS")
print("3.DELETE TASKS")
print("4.EXIT")
print()
ch='y'
while ch=='y':
  choice= int(input("Enter your choice of task:"))

  if choice==1:
    task=input("Enter task to add:")
    todo_list.append(task)
    print("✅ Task added!")

  elif choice==2:
    if len(todo_list)==0:
      print("NO TASKS TO VIEW")
    else:
      print(todo_list)
    
  elif choice==3:
    index=int(input("Enter task number to delete:"))
    if 0<=index<len(todo_list):
      removed=todo_list.pop(index-1)
      print(removed,"TASK DELETED")
      print('NEW TO-DO LIST IS:',todo_list)
    else:
      print("❌ Invalid task number")
  

  elif choice == 4:
        print("👋 Exiting TO-DO List")
        break

  else:
        print("⚠️ Invalid choice. Please choose from 1 to 4.")
  ch=input("do you want to continue(y/n):")
  print()
