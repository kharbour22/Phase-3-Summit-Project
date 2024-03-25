from models.mountain import Mountain
from models.review import Review

def initialize_database():
    Mountain.create_table()
    Review.create_table()

    Mountain.get_all()
    Review.get_all()

def exit_program():
    print("Goodbye!\n")
    quit()

def interact_with_mountain_data():
    while(True):
        mountain_options_menu()
        user_input = input("Select an option from the menu: ")
        if(user_input == 'c'):
            create_mountain()
            break
        elif(user_input == 'r'):
            retrieve_mountain()
            break
        elif(user_input == 'u'):
            update_mountain()
            break
        elif(user_input == 'd'):
            delete_mountain()
            break
        elif(user_input == 'hr'):
            retrieve_mountain_reviews()
            break
        else:
            print("Invalid input! Please try again!\n")

def interact_with_review_data():
    print("You are now interacting with the Review data!")

def mountain_options_menu():
    print("\nHere's the Mountain options menu!")
    print("c: Create a new mountain")
    print("r: Retrieve mountain data")
    print("u: Update a mountain")
    print("d: Delete a mountain")
    print("mr: Retrieve a mountain's reviews\n")

def retrieve_mountains():
    options_for_retrieve_mountains()
    user_input = input("Select an option from the menu: ")

    while(True):
        if(user_input == 'a'):
            print("\nHere are all of the mountains:")
            for mountain in Mountain.all:
                print(mountain)
            # User can press 'return' to continue...
            user_input = input("\nPress 'Enter' to continue...")
            break
        elif(user_input == '1'):
            while(True):
                try:
                    user_input = input("\nEnter a number for the mountain id to search: ")
                    user_input = int(user_input)
                    mountain = Mountain.find_by_id(user_input)
                    if(mountain):
                        print("\nHere is the mountain you requested:")
                        print(Mountain.find_by_id(user_input))
                    else:
                        print("\nMountain Not Found!")
                    user_input = input("\nPress 'Enter' to continue...")
                    break
                except:
                    print("Invalid input! Please try again!")
            break
        else:
            print("Invalid input! Please try again!\n")

def options_for_retrieve_mountains():
    print("\nWould you like to retrieve all mountains or just one?")
    print("a: Retrieve all mountains")
    print("1: Retrieve one mountain\n")

def create_mountain():
    name = input("Enter a name for the new mountain: ")
    new_mountain = Mountain.create(name)
    print("Here's the information for your new mountain:")
    print(new_mountain)
    user_input = input("\nPress 'Enter' to continue...")

def update_mountain():
    while(True):
        try:
            user_input = input("\nEnter a number for the mountain id to update: ")
            user_input = int(user_input)
            mountain = Mountain.find_by_id(user_input)
            if(mountain):
                new_mountain_name = input("Enter a new name for the mountain: ")
                mountain.name = new_mountain_name
                mountain.update()
                print("The mountain has been updated:")
                print(mountain)
                user_input = input("\nPress 'Enter' to continue...")
            else:
                print("\nMountain Not Found!")
            break
        except:
            print("Invalid input! Please try again!")

def delete_mountain():
    while(True):
        try:
            user_input = input("\nEnter a number for the mountain id to delete: ")
            user_input = int(user_input)
            mountain = Mountain.find_by_id(user_input)
            if(mountain):
                mountain.delete()
                print("Moutain successfully deleted!")
            else:
                print("\nMountain Not Found!")
            break
        except:
            print("Invalid input! Please try again!")
    
def retrieve_mountain_reviews():
    while(True):
        try:
            user_input = input("\nEnter a number for the mountain id to get reviews for: ")
            user_input = int(user_input)
            mountain = Moutain.find_by_id(user_input)
            if(mountain):
                print(f"\nHere are the reviews for Mountain # {mountain.id}:")
                print(mountain.reviews())
            else:
                print("\nMountain Not Found!")
            user_input = input("\nPress 'Enter' to continue...")
            break
        except:
            print("Invalid input! Please try again!")
