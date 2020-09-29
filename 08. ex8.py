todoList = []

def add_task(task):
    ###Add a task to the todo list
    todoList.append(task)

def get_task():
    ###Ask a task to the user###
    task = input('Enter a task for your to­do list. Press <enter> when done: ')
    if (len(task) > 0):
        add_task(task)
        get_task()        

get_task()

print('Your To­Do List:')
print('-' * 15)
for task in todoList:
    print('- {}'.format(task))
