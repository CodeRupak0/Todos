import json


try:
    with open("quiz.json", 'r') as file:
        data = json.load(file)  # returns the content of a file as a string file in the form of list of dictionary.
except FileNotFoundError:
    data = []  # Initialize with an empty list if file doesn't exist
except json.JSONDecodeError:
    data = []  # Initialize with an empty list if file is empty or contains invalid JSON
if not isinstance(data, list):
    data = []  # If data is not a list, start with an empty list
while True:
    alternative=[]
    quest=input("Enter the question: ")
    alt=input("Enter answer alternatives separated by comma, Eg-a,b,c,d: ")
    alternative=list(alt.split(","))   # splits the string at the place of comma and creates the list of it.
    alternative = [item.strip() for item in alternative]   # Remove leading and trailing spaces from list objects
    correct_ans=int(input("Enter the correct answer alternative number: "))
    dict={"question":quest.strip(),
          "option":alternative,
          "correct_answer": correct_ans}
    data.append(dict)   # Add the new dictionary to the existing list inside data

    # Write the updated list back to the file.
    with open("quiz.json", 'w') as file:
            json.dump(data, file, indent=2)  # indent pretty-printing
    user=input("Press - 'Y' to add new question and Press - 'N' to Finish: ")
    if user.upper().strip()=='Y':
        continue
    elif user.upper().strip()=='N':
        break
    else:
        print("Invalid Command")




