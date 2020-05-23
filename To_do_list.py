#global vars
user_name = ''
todo_items = []

#To print out simple string
def line_break():
    print('|')

#to check if the user is new
def welcome():
    global user_name, todo_items
    try:
        user_name = input('|-Enter your name: ')
        with open(user_name + '_to_do_list.txt') as file:
            todo_items = [line.rstrip() for line in file]
        print('|-Welcome back,', user_name)
    except FileNotFoundError:
        print('|-Hello new user:', user_name )

#to print out the list
def list_showcase():
    global todo_items
    print('|-Here is your to do list')
    line_break()
    for i in range(0, len(todo_items)):
        print(f"|--- {str(i + 1)}.{todo_items[i]}")

#function that can add multiple items at once
def add_multiple_tasks():
    global todo_items
    print('|-To stop adding tasks, type end')
    while True:
        user_input = input('|-: ')
        if user_input != 'end':
            todo_items.append(user_input)
        else:
            break

#Function that does list modifaction
def list_modification():
    global todo_items
    while True:
        try:
            line_break()
            user_choice = int(input('|-1 To make to do list sorted by ABC'+'\n'+'|-2 To add new item to to do list'+'\n'+'|-3 To delete item on to do list'+'\n'+'|-4 To add multiple tasks'+'\n'+'|-5 To close to do list program'+'\n'+'|-: '))
            if user_choice == 1:
                todo_items.sort(key=str.lower) #ignores upper case chars
            elif user_choice == 2:
                todo_items.append(input('|-Enter a new task that you want to add: '))
                print('|-New task was added to to do list')
            elif user_choice == 3:
                task_remove = int(input('|-Which task you want to remove from the list? '))
                del todo_items[task_remove - 1]
                print('|-Task from the to do list, was removed')
            elif user_choice == 4:
                add_multiple_tasks()
            elif user_choice == 5:
                break
            else:
                print('|-Enter a number between 1-5')
        except ValueError:
            print('|-Enter a number between 1-5')
        list_showcase()

#function for saving todo files
def file_save():
    global todo_items
    text_documment = open(user_name + '_to_do_list.txt', 'w+')
    for i in range(0, len(todo_items)):
        text_documment.write(todo_items[i] + '\n')
    text_documment.close()


welcome()
list_showcase()
list_modification()
file_save()
