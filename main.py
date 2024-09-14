
import time

now= time.strftime("%b %d, %Y  %H:%M:%S")
print("It is ",now)


while True:
    user_action = input("Type show or add or edit or complete or exit:")
    user_action = user_action.strip().upper()
    if user_action.startswith("ADD"):
        todo = user_action[4:] + "\n"  # here \n is used to break lines in text file which creates line break in output screen.
        file = open('todos.txt', 'r')  # file opens in read mode and store in variable named file
        todos = file.readlines()  # The above two lines is used to first read the existing todos in the txt file and add the other todos in the existing list.
        file.close()
        todos.append(todo)
        file = open('todos.txt','w')  # file=open() access the text file created and 'w ' is used to write the info in the text file.
        file.writelines(todos)
        file.close()
    elif user_action.startswith("SHOW"):
        file = open('todos.txt', 'r')
        todos = file.readlines()
        file.close()
        newtodos=[]
        for items in todos:
            newitem = items.strip('\n')  #strip is used to remove the space at the begining of the sentence
            newtodos.append(newitem)
            todos = newtodos
        print("Todos List:")
        for index, item in enumerate(todos):
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith("EDIT"):
        try:       # tries to the below block of code first and if the error occurs execute the except line of command
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()
            number = int(user_action[5:])   # only the character after the 5 unit place is taken for consideration into the assigned variable
            number = number - 1
            newtodo = input("Enter the new todo:")
            todos[number] = newtodo + '\n'
            with open('todos.txt','w') as file:    # another method to directly access or handle the files
                file.writelines(todos)
        except ValueError:
            print("INVALID Command")
            print("Enter the Edit command followed by white space and number to be edited: Eg-edit 4")
            continue
        except IndexError:
            print("The Item does not exist. Please give a valid item number.")
            continue        # it skips all the task and goes to the next sequence of loop. 
    elif user_action.startswith("COMPLETE"):
        try:
            with open ('todos.txt', 'r') as file:
                todos=file.readlines()
            complete = int(user_action[9:])
            todos.pop(complete - 1)
            with open ('todos.txt', 'w') as file:
                file.writelines(todos)
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
