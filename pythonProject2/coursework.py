import random

projects = {5456: {'project_id': 5456, 'name': '', 'category': '4', 'members count': 2, 'member 1 name': 'gjhj', 'member 2 name': 'jgjhg', 'description': 'nothing', 'country': 'srilanka'}}  # This is the main dictionary

# This is a sub list which used to insert projects according to category types
category_1 = []
category_2 = []
category_3 = []
category_4 = []
category_5 = []
category_6 = []

winners = []    # This is for add winners from text file

def reading_texts():
    fhandle1 = open("category1.txt","r")
    for x in fhandle1:
        result = eval(x)
        if int(result['project_id']) in list(projects.keys()):
            continue
        else:
            projects[int(result['project_id'])] = result
    fhandle2 = open("category2.txt", "r")
    for x in fhandle2:
        result = eval(x)
        if int(result['project_id']) in list(projects.keys()):
            continue
        else:
            projects[int(result['project_id'])] = result
    fhandle3 = open("category3.txt", "r")
    for x in fhandle3:
        result = eval(x)
        if int(result['project_id']) in list(projects.keys()):
            continue
        else:
            projects[int(result['project_id'])] = result
    fhandle4 = open("category4.txt", "r")
    for x in fhandle4:
        result = eval(x)
        if int(result['project_id']) in list(projects.keys()):
            continue
        else:
            projects[int(result['project_id'])] = result
    fhandle5 = open("category5.txt", "r")
    for x in fhandle5:
        result = eval(x)
        if int(result['project_id']) in list(projects.keys()):
            continue
        else:
            projects[int(result['project_id'])] = result
    fhandle6 = open("category6.txt", "r")
    for x in fhandle6:
        result = eval(x)
        if int(result['project_id']) in list(projects.keys()):
            continue
        else:
            projects[int(result['project_id'])] = result
def temp_saving_to_texts(pr_id,category):
    fhandle1 = open("category1.txt","a+")
    fhandle1.truncate(0)
    fhandle2 = open("category2.txt", "a+")
    fhandle2.truncate(0)
    fhandle3 = open("category3.txt", "a+")
    fhandle3.truncate(0)
    fhandle4 = open("category4.txt", "a+")
    fhandle4.truncate(0)
    fhandle5 = open("category5.txt", "a+")
    fhandle5.truncate(0)
    fhandle6 = open("category6.txt", "a+")
    fhandle6.truncate(0)
    if category == 1:
        fhandle1.write(f"{projects[pr_id]}\n")
    elif category == 2:
        fhandle2.write(f"{projects[pr_id]}\n")
    elif category == 3:
        fhandle3.write(f"{projects[pr_id]}\n")
    elif category == 4:
        fhandle4.write(f"{projects[pr_id]}\n")
    elif category == 5:
        fhandle5.write(f"{projects[pr_id]}\n")
    elif category == 6:
        fhandle6.write(f"{projects[pr_id]}\n")
def adding_project_details():  # creating new dictionary in projects
  """ This function is for add project details all the details saved into multivalued variable """
  while True:
      try:              # avoiding strings in project_ID
        project_id = int(input("Enter the project ID: "))
      except:
          print("please enter numbers only")
          continue
      else:
          break
  projects[project_id] = {}             # creating dictionary in main dictionary by using project ID as the key
  projects[project_id]['project_id'] = project_id   # adding project id into dictionary
  while True:
      projects[project_id]['name'] = input("Enter the project name: ")
      if projects[project_id]['name'] == ' ':
          print("cant be null value")
          continue
      else:
          break
  print(                                                                                     # giving a list to select
      "Please select the matching number for your project category and enter it below \n"
      "1.For ' Business internet' press '1' \n"
      "2.For 'Business Class email' press '2' \n"
      "3.For 'Cloud Storage' press '3' \n"
      "4.For 'IT Specialists and Services' press '4' \n"
      "5.For 'Systematized business phone lines' press '5' \n"
      "6.For 'AR and VR' press '6' ")
  while True:
    projects[project_id]['category'] = input("Enter the project Category: ")
    # check weather category number is from the list or not
    if projects[project_id]['category'] in ('1', '2', '3', '4', '5', '6'):
      break
    else:
      print("invalid project category please enter again")
      continue

  while True:         # To avoid errors
    try:
      projects[project_id]['members count'] = int(input("Enter the team members count (PLEASE ENTER ONLY NUMBERS): "))  #To avoid data type errors
    except:  # check if any error occurs
      print("Wrong data type please enter only numbers")
      continue
    else:
      break

  for i in range(1, projects[project_id]['members count'] +1):  # adding members 1 after another
    projects[project_id][f'member {i} name'] = input(f"Enter the member {i} name : ")

  while True:   # data validation
    projects[project_id]['description'] = input("Enter a brief description: ")      # getting other project details
    projects[project_id]['country'] = input("Enter the country: ")
    if projects[project_id]['description'] == ' ' and projects[project_id]['country'] == ' ':
        print("You cant insert empty values")
        continue
    else:
        break
  print(f"Your project {projects[project_id]['name']} is successfully added")
  print()
  print(projects)         # print showing project details
  temp_saving_to_texts((projects[project_id]['category']),project_id)

def deleting_project_details():  # deleting items in dictionary
  '''This function is for delete project details.You can delete any project detail by using this but you cant delete category and name.'''
  reading_texts()
  while True:
      try:  # avoiding data type errors
          # requesting the project ID to update elements
          search_id = int(input("enter the project id that you want to update : "))
      except:
          print("please enter numbers only")
      else:
          if search_id in list(projects.keys()):  # checking the availability of project_id
              print("project id is correct")
              break
          else:
              print("Incorrect project ID please enter the project ID again")
              continue
  print(
      " 1.press '1' to remove name\n"
      "2.press '2' to remove category\n"            # giving user a list to avoid mistakes
      "3.press '3' to remove team members\n"
      "4.press '4' to remove description\n"
      "5.press '5' to remove country\n"
      "6.press '6' to remove all elements\n"
      "7.press '7' to exit")

  while True:               # to continue the loop
    user_input2 = input("enter a subcategory number that you want to remove according to the above list (press 7 to exit from this) : ")      # asking user category number to delete
    if user_input2 == "1":
      print("you cant remove the name If you want to update it please press 7 and go to the main category and select update project details")   # avoiding the deletion of name
    elif user_input2 == "2":
      print("you cant remove the category If you want to update it please press 7 and go to the main category and select update project details")       # avoiding the deletion of category
    elif user_input2 == "3":
      while True:           # avoiding data type errors
        try:
            count = int(input("How many team members do you want to remove"))  # asking user to how many users to delete
        except:
            print("Invalid data type : Please enter numbers only")
            continue
        else:
            if count >= int(projects[search_id]['members count']):
                print('Team member count that you want to remove is higher than the existing team member count')
                continue
            else:
                for x in range(1, count + 1):
                    while True:
                        try:  # checking the availability of that name
                            projects[search_id].pop(input("enter the member name that you want to remove : "))
                        except:
                            print("cant find a member name according to that name please enter that name again ")
                            continue
                        else:
                            break
                break

    elif user_input2 == "4":
      projects[search_id].pop('description')
    elif user_input2 == "5":
      print("you cant remove the country If you want to update it please press 7 and go to the main category and select update project details")
    elif user_input2 == "6":
      approve = input(f"are you sure you want to remove all elements in {search_id} press'0' to no press '1' to yes : ")  # getting user approve
      if approve == 1:
        projects[search_id].clear()
      else:
        print("request declined")
        continue
    elif user_input2 == "7":
      break               # exiting the loop
    else:
      print("unrecognized input please enter your selection again : ")
    all_keys = list(projects.keys())
    for key in all_keys:
        temp_saving_to_texts(key,projects[key]['category'])


def updating_project_details():
  '''This is function is for update project details after adding project details but remember you cant change the project details on text file'''
  reading_texts()
  while True:
    try:        # avoiding data type errors
        # requesting the project ID to update elements
        search_id = int(input("enter the project id that you want to update : "))
    except:
        print("please enter numbers only")
    else:
        if search_id in list(projects.keys()):  # checking the availability of project_id
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

    sub_ID = input("enter the sub category that you want to update : ")      # getting sub id through the list
    if sub_ID == "1":
      projects[search_id]['name'] = input("Enter the new project name : ")      # updating elements
    elif sub_ID == "2":
      print(
          "Please select the matching number for your project category and enter it below \n"
          "1.For ' Business internet' press '1' \n"
          "2.For 'Business Class email' press '2' \n"
          "3.For 'Cloud Storage' press '3' \n"                      # giving the category list to change
          "4.For 'IT Specialists and Services' press '4' \n"
          "5.For 'Systematized business phone lines' press '5' \n"
          "6.For 'AR and VR' press '6' ")
      while True:
        projects[search_id]['category'] = input("enter the new category : ")
        # checking the availability of user inputs
        if projects[search_id]['category'] in ('1', '2', '3', '4', '5', '6'):
          break
        else:
          print("invalid project category please enter again")
          continue
    elif sub_ID == "3":
     while True:
          old_member_count = int(projects[search_id]['members count'])
          # assigning current member count into new variable
          try:              #avoiding errors
            new_member_count = int(input("enter the new member count : "))         # getting new member count from the user
          except:
              print("please enter only numbers")
              continue
          else:
              break

     if old_member_count < new_member_count:                           # checking user is updating or deleting members
        for x in range(1, projects[search_id]['members count'] -old_member_count):    # adding new members name
          old_member_count+=1                                           # updating count value
          projects[search_id][f'member {old_member_count} name'] = input("enter the member name that you want to add : ")     # asking user input with correct member number
        projects['search_ID']['members count'] = new_member_count       #assigning new count
     else:
        print("you cant remove team members if you want to do that please select delete project details")         # giving user a messege

    elif sub_ID == "4":
      member_name = input("Enter the member name that you want to change : ")
      projects[search_id][member_name] = input("enter the new member name that you want to update : ")

    elif sub_ID == "5":
      projects[search_id]['country'] = input("enter the new country : ")

    elif sub_ID == "7":
      break
    else:
      print("wrong input please enter again")
    print(f"your updated project = {projects[search_id]}")
    all_keys = list(projects.keys())
    for key in all_keys:
        temp_saving_to_texts(key, projects[key]['category'])

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