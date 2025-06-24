
#Build a simple script  to manage tasks using dictionary.
 
#Ask user to enter task 1 name
#Ask user to enter task 2 name
#Ask user to enter task 3 name
#Ask user to update task 2
#Ask user to delete task 3
#print final tasks

task1=input("enter the task 1:")
task2=input("enter the task 2:")
task3=input("enter the task 3:")
tasks={}
tasks.update({"task1":task1,"task2":task2,"task3":task3})
print(tasks)
updated_task2=input("enter the updated task 2:")
tasks.update({"task2":updated_task2})
print(tasks)
a=bool(input("enter true or false:"))
if a==True:
    print(tasks.pop("task3"))
    print(tasks)
else:
    print(tasks)





