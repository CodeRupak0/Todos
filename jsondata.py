import json
# opens a quiz.json file and loads a content of file as a list for easier access
with open ("quiz.json", 'r') as file:
    content_file=file.read()        # read entire content as a single item along with spaces
    data= json.loads(content_file)  # converts the single file type into list type for easier accessibility

score=0
# accessing each dictionary from the list of json data and printing question 1st then option and checks the answer
for questions in data:
    print(questions["question"])
    for index, alternative in enumerate(questions["option"]):  # access index and data from option key
        print(index+1, "-", alternative)
    user_choice=int(input("Enter your choice number: "))
    questions["user_choice"]= user_choice       # stores the user choice as dictionary to each data list in json file used for future comparison using same data types
    if questions["user_choice"]==questions["correct_answer"]:
        score= score+1
print("Total score: ",score,"/",len(data))

"""Access each item of the list in the form of dictionary
and checks the correct option with the temporarily added
user_option as dictionary and gives the message"""

for index,questions in enumerate(data):
    if questions["user_choice"]==questions["correct_answer"]:
        message= f"Qno.{index+1}. Correct Answer"
        print(message)
    else:
        message= f"Qno.{index+1}. Your answer is Wrong. " \
                 f"Correct answer is {questions['correct_answer']}"
        print (message)




