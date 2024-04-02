import random

projects = {}  # This is the main dictionary

def adding_project_details():  #creatiing new dictionary in projects
    project_id_input = input("Enter the project ID: ")
    project_id = "AAM" + project_id_input
    projects[project_id] = {           #creating another dictionary in main dictianary
        'name': input("Enter the project name: "),
        'category': input("Enter the project Category: ")}

    while True:             #To avoid errors
            try:
                projects[project_id] = {'members count': int(input("Enter the team members count (PLEASE ENTER ONLY NUMBERS): "))} #To avoid data type errors
            except :
                print("Wrong data type please enter only numbers")
                continue
            else:
                break
    print(projects[project_id].get("members count"))
    x = projects[project_id]['members count']
    print(x)
    projects[project_id] = {'description': input("Enter a brief description: "),
        'country': input("Enter the country: ")}

    for i in range(1 ,x+1): #adiing members 1 after another
         projects[project_id][f'member {i} name'] = input(f"Enter the member {i} name : ")
    print(f"Your project {projects[project_id]['name']} is successfully added")

def deleting_project_details(): #deleting items in dictionary
    search_id = input("enter the project id that you want to delete : ") #requesting the project ID to remove elements
    print(" 1.press '1' to remove name/n"   
          "2.press '2' to remove category/n"    #giving user a list to avoid mistakes
          "3.press '3' to remove team members/n"
          "4.press '4' to remove description/n"
          "5.press '5' to remove country/n"
          "6.press '0' to remove all elements/n"
          "7.press '7' to exit")
    while True:   #to continue the loop
        user_input2 = input("enter a subcategory number that you want to remove according to the above list (press 7 to exit from this) : ") #asking user inputs
        if user_input2 ==1:
            projects[search_id].pop('name') #use pop to remove name key value
        elif user_input2 == 2:
            projects[search_id].pop('category')
        elif user_input2 == 3:
            count = int(input("How many team members do you want to remove")) #asking user to how many users to delete
            if count> projects[search_id]['members count']:
                for x in range(1,count+1):
                    member_name = input(f"enter the team member {x} name that you want to remove : ")


            projects[search_id].pop('members count')
        elif user_input2 == 4:
            projects[search_id].pop('description')
        elif user_input2 == 5:
            projects[search_id].pop('country')
        elif user_input2 == 6:
            approve = input(f"are you sure you want to remove all elements in {search_id} press'0' to no press '1' to yes : ") #getting user approve
            if approve == 1:
                projects[search_id].clear()
            else:
                print("request declined")
                continue
        elif user_input2 == 7:
            break
        else:
            print("unrecognized input please enter your selection again : ")


def updating_project_details():
    search_ID = input("Enter the project ID : ")
    sub_ID = input("enter the sub category you want to delete : ")
    if sub_ID == "name":
        projects[search_ID]['name'] = input("Enter the new project name : ")
    elif sub_ID == "category":
        projects[search_ID]['category'] = input("enter the new category : ")


adding_project_details()
