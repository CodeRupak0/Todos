def get_todos(filepath):
    with open(filepath, 'r') as file_local:
        newtodo = file_local.readlines()
        return newtodo


def write_todos(todos_arg, filepath):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


while True:
    user_action = input("Type show or add or edit or complete or exit:")
    user_action = user_action.strip().upper()
    if user_action.startswith("ADD"):
        todos= get_todos("todos.txt")
        todo = user_action[4:] + "\n"  # here \n is used to break lines in text file which creates line break in output screen.
        todos.append(todo)
        write_todos(todos,"todos.txt")
    elif user_action.startswith("SHOW"):
        todos= get_todos("todos.txt")
        newtodos = []
        for items in todos:
            newitem = items.strip('\n')  # strip is used to remove the space at the begining of the sentence
            newtodos.append(newitem)
            todos = newtodos
        print("Todos List:")
        for index, item in enumerate(todos):
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith("EDIT"):
        try:  # tries to the below block of code first and if the error occurs execute the except line of command
            todos= get_todos("todos.txt")
            number = int(user_action[5:])  # only the character after the 5 unit place is taken for consideration into the assigned variable
            number = number - 1
            newtodo = input("Enter the new todo:")
            todos[number] = newtodo + '\n'
            write_todos(todos,"todos.txt")
        except ValueError:
            print("INVALID Command")
            print("Enter the Edit command followed by white space and number to be edited: Eg-edit 4")
            continue
        except IndexError:
            print("The Item does not exist. Please give a valid item number.")
            continue  # it skips all the task and goes to the next sequence of loop.
    elif user_action.startswith("COMPLETE"):
        try:
            todos= get_todos("todos.txt")
            complete = int(user_action[9:])
            todos.pop(complete - 1)
            write_todos(todos,"todos.txt")
        except ValueError:
            print("INVALID Command")
            print("Enter the Complete command followed by white space and number to be edited: Eg-Complete 4")
            continue
        except IndexError:
            print("The Item does not exist. Please give a valid item number.")
            continue
    elif user_action.startswith("EXIT"):
        break
    else:
        print("Invalid User Command")

print("SEE YOU")