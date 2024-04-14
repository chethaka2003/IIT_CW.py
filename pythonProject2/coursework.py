import random

projects = {}  # This is the main dictionary

category_1 = []  #This is a sub list which used to insert projects according to category types
category_2 = []
category_3 = []
category_4 = []
category_5 = []
category_6 = []

winners = []    #This is for add winners from text file


def adding_project_details():  #creatiing new dictionary in projects
  '''This function is for add project details all the details saved into multi valued variable'''
  project_id_input = input("Enter the project ID: ")
  project_id = "AAM" + project_id_input
  projects[project_id] = {}  #creating another dictionary in main dictianary by using project ID as the key of sub dictionary
  projects[project_id]['project_id'] = project_id   #addding project id into dictionary

  projects[project_id]['name'] = input("Enter the project name: ")
  print(                                                                                     #giving a list to select
      "Please select the matching number for your project category and enter it below \n"
      "1.For ' Business internet' press '1' \n"
      "2.For 'Business Class email' press '2' \n"
      "3.For 'Cloud Storage' press '3' \n"
      "4.For 'IT Specialists and Services' press '4' \n"
      "5.For 'Systematized business phone lines' press '5' \n"
      "6.For 'AR and VR' press '6' ")
  while True:
    projects[project_id]['category'] = input("Enter the project Category: ")
    if projects[project_id]['category'] in ('1', '2', '3', '4', '5', '6'):        #check weather category number is from the listcor not
      break
    else:
      print("invalid project category please enter again")
      continue

  while True:         #To avoid errors
    try:
      projects[project_id]['members count'] = int(input("Enter the team members count (PLEASE ENTER ONLY NUMBERS): "))  #To avoid data type errors
    except:  #check if any error occurs
      print("Wrong data type please enter only numbers")
      continue
    else:
      break
  projects[project_id]['description'] = input("Enter a brief description: ")      #getting other project deatils
  projects[project_id]['country'] = input("Enter the country: ")

  for i in range(1, projects[project_id]['members count'] +1):  #adiing members 1 after another
    projects[project_id][f'member {i} name'] = input(
        f"Enter the member {i} name : ")
  print(f"Your project {projects[project_id]['name']} is successfully added")
  print()
  print(projects)         #print showing project details


def deleting_project_details():  #deleting items in dictionary
  '''This function is for delete project details.You can delete any project detail by using this but you cant delete category and name.'''
  while True:
    search_id = input("enter the project id that you want to delete : ")  #requesting the project ID to remove elements
    if search_id in projects:           #checking the availability of the project ID
      print("project id is correct")
      break
    else:
      print("Incorrect project ID please enter the project ID again")
      continue
  print(
      " 1.press '1' to remove name\n"
      "2.press '2' to remove category\n"            #giving user a list to avoid mistakes
      "3.press '3' to remove team members\n"
      "4.press '4' to remove description\n"
      "5.press '5' to remove country\n"
      "6.press '6' to remove all elements\n"
      "7.press '7' to exit")

  while True:               #to continue the loop
    user_input2 = input("enter a subcategory number that you want to remove according to the above list (press 7 to exit from this) : ")      #asking user category number to delete
    if user_input2 == "1":
      print("you cant remove the name If you want to update it please press 7 and go to the main category and select update project details")   #avoiding the deletion of name
    elif user_input2 == "2":
      print("you cant remove the category If you want to update it please press 7 and go to the main category and select update project details")       #avoiding the deletion of category
    elif user_input2 == "3":
      while True:           #avoiding data type errors
        try:
            count = int(input("How many team members do you want to remove"))  #asking user to how many users to delete
        except:
            print("Invalid data type : Please enter numbers only")
            continue
        else:
            break
      for x in range(1, count + 1):
        while True:
          try:                  #checking the availability of that name
            projects[search_id].pop(input("enter the member name that you want to remove : "))
          except:
            print("cant find a member name according to that name please enter that name again ")
            continue
          else:
            break
    elif user_input2 == "4":
      projects[search_id].pop('description')
    elif user_input2 == "5":
      print("you cant remove the country If you want to update it please press 7 and go to the main category and select update project details")
    elif user_input2 == "6":
      approve = input(f"are you sure you want to remove all elements in {search_id} press'0' to no press '1' to yes : ")  #getting user approve
      if approve == 1:
        projects[search_id].clear()
      else:
        print("request declined")
        continue
    elif user_input2 == "7":
      break               #exiting the loop
    else:
      print("unrecognized input please enter your selection again : ")


def updating_project_details():
  '''This is function is for update project details after adding project details but remember you cant change the project details on text file'''
  while True:
    search_id = input("enter the project id that you want to update : ")  # requesting the project ID to update elements
    if search_id in projects:
      print("project id is correct")
      break
    else:
      print("Incorrect project ID please enter the project ID again")
      continue

  while True:
    print(
        " 1.press '1' to update name\n"
        "2.press '2' to update category\n"      # giving user a list to avoid mistakes
        "3.press '3' to update team members count\n"
        "4.press '4' to update team members name\n"
        "5.press '5' to update country\n"
        "7.press '7' to exit")

    sub_ID = input("enter the sub category you want to delete : ")      #getting sub id through the list
    if sub_ID == "1":
      projects[search_id]['name'] = input("Enter the new project name : ")      #updating elements
    elif sub_ID == "2":
      print(
          "Please select the matching number for your project category and enter it below \n"
          "1.For ' Business internet' press '1' \n"
          "2.For 'Business Class email' press '2' \n"
          "3.For 'Cloud Storage' press '3' \n"                      #giving the cetegory list to change
          "4.For 'IT Specialists and Services' press '4' \n"
          "5.For 'Systematized business phone lines' press '5' \n"
          "6.For 'AR and VR' press '6' ")
      while True:
        projects[search_id]['category'] = input("enter the new category : ")
        if projects[search_id]['category'] in ('1', '2', '3', '4', '5', '6'):         #checking the availablity of user inputs
          break
        else:
          print("invalid project category please enter again")
          continue
    elif sub_ID == "3":
      old_member_count = projects['search_ID']['members count']         #assigning current memmber count into new variable
      new_member_count = input("enter the new member count : ")         #getting new member count from the user
      if old_member_count < new_member_count:                           #checking user is updating or deleting members
        for x in range(1, projects[search_id]['members count'] -old_member_count):    #adding new members name
          old_member_count+=1                                           #updating count value
          projects[search_id][f'member {old_member_count} name'] = input("enter the member name that you want to add : ")     #asking user input with correct member number
        projects['search_ID']['members count'] = new_member_count       #assigning new count
      else:
        print("you cant remove team members if you want to do that please select delete project details")         #giving user a messege

    elif sub_ID == "4":
      member_name = input("Enter the member name that you want to change : ")
      projects[search_id][member_name] = input("enter the new member name that you want to update : ")

    elif sub_ID == "5":
      projects[search_id]['country'] = input("enter the new country : ")

    elif sub_ID == "7":
      break
    else:
      print("wrong input please enter again")


def viewing_project_details():
  all_keys = list(projects.keys())  #getting all project IDs into a list
  all_keys.sort()  #sorting project IDs into  ascending order
  for x in all_keys:  #iterating through order
    print(x, '=',projects[x],'\n')


def saving_project_details():
  fhandle = open("projects.txt", "a+")
  fhandle.truncate(0)
  all_ids = list(projects.keys())
  for x in all_ids:
    if projects[x]['category'] == '1':
      category_1.append(projects[x])
    elif projects[x]['category'] == '2':
      category_2.append(projects[x])
    elif projects[x]['category'] == '3':
      category_3.append(projects[x])
    elif projects[x]['category'] == '4':
      category_4.append(projects[x])
    elif projects[x]['category'] == '5':
      category_5.append(projects[x])
    elif projects[x]['category'] == '6':
      category_6.append(projects[x])
  fhandle.write('category 1 \n\n')
  for y in category_1:
    fhandle.write(str(y))
    fhandle.write('\n')
  fhandle.write('\n')
  fhandle.write('category 2\n\n')
  for z in category_2:
    fhandle.write(str(z))
    fhandle.write('\n')
  fhandle.write('\n')
  fhandle.write('category 3\n\n')
  for q in category_3:
    fhandle.write(str(q))
    fhandle.write('\n')
  fhandle.write('\n')
  fhandle.write('category 4\n\n')
  for w in category_4:
    fhandle.write(str(w))
    fhandle.write('\n')
  fhandle.write('\n')
  fhandle.write('category 5\n\n')
  for e in category_5:
    fhandle.write(str(e))
    fhandle.write('\n')
  fhandle.write('\n')
  fhandle.write('category 6\n\n')
  for r in category_6:
    fhandle.write(str(r))
    fhandle.write('\n')


def random_showing():
  selected_lines = []
  fhandle =  open("projects.txt", "r")
  for i in fhandle:
      i = i.strip()
      if i.startswith("category"):  # Skip category names
        pass
      elif not i:  # Skip empty lines
        pass
      else:
        i = i.strip("{}")
        i = i.replace(":",",").split(',')
        selected_lines.append(i)
  random.shuffle(selected_lines)
  for line in selected_lines:
        print(line)
        stars_1st_judge = input("Enter the number of stars that first judge gives (stars are given between 1-5): ")
        stars_2nd_judge = input("Enter the number of stars that second judge gives (stars are given between 1-5): ")
        stars_3rd_judge = input("Enter the number of stars that third judge gives (stars are given between 1-5): ")
        stars_4th_judge = input("Enter the number of stars that fourth judge gives (stars are given between 1-5): ")
        count1 = int(len(stars_1st_judge))
        count2 = int(len(stars_2nd_judge))
        count3 = int(len(stars_3rd_judge))
        count4 = int(len(stars_4th_judge))
        average = (count1 + count2 + count3 + count4) / 4
        print("Average stars:", average)
        string = {'name':line[3],'country':line[11],'average':average}
        winners.append(string)
  print("All the projects has given points")
  print("These are the winners who got first,second and third places")
  def get_year(element):
      return element['average']
  winners.sort(key=get_year)
  positions = ['1 st place','2nd place','3rd place']
  print(f"      *")
  print(f"      *                                           *")
  print(f"      *                                           *                                              *")
  print(f"{winners[0]['name']}{" " * (46 - len(winners[0]['name']))}{winners[1]['name']}{" " * (46 - len(winners[1]['name']))}{winners[2]['name']}")
  print(f"{winners[0]['country']}{" " * (46 - len(winners[0]['country']))}{winners[1]['country']}{" " * (46 - len(winners[1]['country']))} {winners[2]['country']}")
  print(f"  {positions[0]}{" "*(46-len(positions[0]))} {positions[1]}{" "*(46-len(positions[1]))}{positions[2]}")

def main():
  while True:
    print("press 1 to add new project\n"
        "press 2 to delete a project\n"
        "press 3 to update a project\n"
        "press 4 to view projects \n"
        "press 5 to save projects \n"
          "press 6 to randomly show and give stars\n"
          "press 7 to exit the menu")
    user_input = input("enter a number from above category : ")
    if user_input == "1":
      adding_project_details()
    elif user_input == "2":
      deleting_project_details()
    elif user_input == "3":
      updating_project_details()
    elif user_input == "4":
      viewing_project_details()
    elif user_input == "5":
      saving_project_details()
    elif user_input == "6":
      random_showing()
    elif user_input == "7":
      break

main()


print("checking weather this is correct or not")