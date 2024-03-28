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
        print("_______________________________________")
        if(user_input == 'c'):
            create_mountain()
            break
        elif(user_input == 'r'):
            retrieve_mountains()
            break
        elif(user_input == 'u'):
            update_mountain()
            break
        elif(user_input == 'd'):
            delete_mountain()
            break
        elif(user_input == 'mr'):
            retrieve_mountain_reviews()
            break
        elif(user_input == 'q'): 
            return
        else:
            print("Invalid input! Please try again!\n")

def mountain_options_menu():
    print("_______________________________________")
    print("\nHere's the Mountain options menu!\n")
    print("c: Create a new mountain")
    print("r: Retrieve mountain data")
    print("u: Update a mountain")
    print("d: Delete a mountain")
    print("mr: Retrieve a mountain's reviews")
    print("q: Return to Main Menu\n")

def retrieve_mountains():
    print("_______________________________________")
    options_for_retrieve_mountains()
    while True:
        user_input = input("Select an option from the menu: ")

        if user_input == 'a':
            print("\nHere are all of the mountains:\n")
            for mountain in Mountain.all:
                print(mountain)
            # User can press 'Enter' to continue...
            input("\nPress 'Enter' to continue...")
            break  # Exit the loop and return to the main menu
        elif user_input == '1':
            while True:
                try:
                    user_input = input("\nEnter a number for the mountain id to search: ")
                    mountain_id = int(user_input)
                    mountain = Mountain.find_by_id(mountain_id)
                    if mountain:
                        print("\nHere is the mountain you requested:\n")
                        print(Mountain.find_by_id(mountain_id))
                        input("\nPress 'Enter' to continue...")
                        return 
                    else:
                        print("\nMountain Not Found!")
                    input("\nPress 'Enter' to continue...")
                    break 
                except ValueError:
                    print("Invalid input! Please enter a valid mountain ID.")
        else:
            print("Invalid input! Please try again!\n")

def options_for_retrieve_mountains():
    print("_______________________________________")
    print("\nWould you like to retrieve all mountains or just one?")
    print("a: Retrieve all mountains")
    print("1: Retrieve one mountain\n")

def create_mountain():
    print("_______________________________________")
    while True:
        try:
            name = input("Enter a name for the new mountain: ")
            elevation = int(input("Enter the elevation for the mountain in feet: "))
            location = input("Enter the location for the mountain: ")
            
            new_mountain = Mountain.create(name, elevation, location)
            print("Here's the information for your new mountain:")
            print(new_mountain)
            user_input = input("\nPress 'Enter' to continue...")
            break
        except ValueError as e:
            print("Error:", e)
            print("Please try again!\n")


def update_mountain():
    print("_______________________________________")
    while True:
        try:
            user_input = input("\nEnter a number for the mountain id to update: ")
            user_input = int(user_input)
            mountain = Mountain.find_by_id(user_input)
            if mountain:
                new_mountain_name = input("Enter a new name for the mountain: ")
                new_elevation = input("Enter a new elevation for the mountain in feet: ")
                new_location = input("Enter a new location for the mountain: ")
                
                # Validate elevation input
                try:
                    new_elevation = int(new_elevation)
                except ValueError:
                    print("Invalid elevation input! Please enter a number.")
                    continue  # Restart the loop to prompt for input again

                # Update mountain attributes
                mountain.name = new_mountain_name
                mountain.elevation = new_elevation
                mountain.location = new_location
                mountain.update()
                
                print("\nThe mountain has been updated:\n")
                print(mountain)
                input("\nPress 'Enter' to continue...")
                break
            else:
                print("\nMountain Not Found!")
        except ValueError:
            print("Invalid input! Please enter a valid mountain ID.")

def delete_mountain():
    print("_______________________________________")
    while(True):
        try:
            user_input = input("\nEnter a number for the mountain id to delete: ")
            user_input = int(user_input)
            mountain = Mountain.find_by_id(user_input)
            if(mountain):
                mountain.delete()
                print("\nMoutain successfully deleted!")
                input("\nPress 'Enter' to continue...")
            else:
                print("\nMountain Not Found!")
                input("\nPress 'Enter' to continue...")
            break
        except:
            print("Invalid input! Please try again!")
    
def retrieve_mountain_reviews():
    print("_______________________________________")
    while(True):
        try:
            user_input = input("\nEnter a number for the mountain id to get reviews for: ")
            user_input = int(user_input)
            mountain = Mountain.find_by_id(user_input)
            if(mountain):
                print(f"\nHere are the reviews for Mountain # {mountain.id}\n:")
                print(mountain.reviews())
            else:
                print("\nMountain Not Found!")
            user_input = input("\nPress 'Enter' to continue...")
            break
        except:
            print("Invalid input! Please try again!")
           

def interact_with_review_data():
    print("_______________________________________")
    while(True):
        review_options_menu()
        user_input = input("Select an option from the menu: ")
        if(user_input == 'c'):
            create_review()
            break
        elif(user_input == 'r'):
            retrieve_reviews()
            break
        elif(user_input == 'u'):
            update_reviews()
            break
        elif(user_input == 'd'):
            delete_review()
            break
        elif(user_input == 'mr'):
            retrieve_mountain_reviews()
            break
        elif(user_input == 'q'):
            return
        else:
            print("Invalid input! Please try again!\n")

def review_options_menu():
    print("_______________________________________")
    print("\nHere's the Review options menu!\n")
    print("c: Create a new review")
    print("r: Retrieve review data")
    print("u: Update a review")
    print("d: Delete a review")
    print("mr: Retrieve a mountain's reviews")
    print("q: Return to Main Menu\n")

def retrieve_reviews():
    print("_______________________________________")
    options_for_retrieve_reviews()
    user_input = input("Select an option from the menu: ")

    while True:
        if user_input == 'a':
            print("\nHere are all of the reviews:\n")
            for review in Review.all:
                print(review)
            # User can press 'Enter' to continue...
            input("\nPress 'Enter' to continue...")
            break
        elif user_input == '1':
            while True:
                try:
                    user_input = input("\nEnter a number for the review id to search: ")
                    review_id = int(user_input)
                    review = Review.find_by_id(review_id)
                    if review:
                        print("\nHere is the review you requested:\n")
                        print(Review.find_by_id(review_id))
                        input("\nPress 'Enter' to continue...")
                        return  # Exit the function after successfully retrieving one review
                    else:
                        print("\nReview Not Found!")
                    break
                except ValueError:
                    print("Invalid input! Please enter a valid review ID.")
        else:
            print("Invalid input! Please try again!\n")
            user_input = input("Select an option from the menu: ")

def options_for_retrieve_reviews():
    print("_______________________________________")
    print("\nWould you like to retrieve all reviews or just one?")
    print("a: Retrieve all reviews")
    print("1: Retrieve one review\n")

def create_review():
    print("_______________________________________")
    while True:
        mountain_id_str = input("Enter the mountain id for the new review: ")
        try:
            mountain_id = int(mountain_id_str)
            mountain = Mountain.find_by_id(mountain_id)
            if mountain:
                break
            else:
                print("This id does not exist. Please try again.")
        except ValueError:
            print("Mountain ID must be an integer. Please try again.")

    while True:
        text = input("Enter the review text here: ")
        if 3 <= len(text) <= 80:
            break
        else:
            print("Text must be between 3 and 80 characters long. Please try again.")

    while True:
        rating_str = input("Rate the difficulty (1-10): ")
        try:
            rating = int(rating_str)
            if 1 <= rating <= 10:
                break
            else:
                print("Rating must be between 1 and 10. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 10.")

    try:
        new_review = Review.create(rating, text, mountain_id)
        print("\nHere's the information for your new review:\n")
        print(new_review)
        user_input = input("\nPress 'Enter' to continue...")
    except ValueError as e:
        print("Error:", e)
        print("Review creation failed. Please try again.")

def update_reviews():
    print("_______________________________________")
    while True:
        try:
            user_input = input("\nEnter a number for the review id to update: ")
            user_input = int(user_input)
            review = Review.find_by_id(user_input)
            if review:
                new_review_text = input("Enter new text for the review: ")
                new_rating = input("Enter new rating for the review: ")  
                new_mountain_id = input("Enter new mountain id for the review: ")

                # Check if the entered mountain_id exists
                mountain = Mountain.find_by_id(int(new_mountain_id))
                if mountain:
                    review.text = new_review_text
                    review.rating = int(new_rating)
                    review.mountain_id = int(new_mountain_id)
                    review.update()
                    print("\nThe review has been updated:\n")
                    print(review)
                    input("\nPress 'Enter' to continue...")
                    break
                else:
                    print("Mountain with the provided ID does not exist.")
            else:
                print("\nReview Not Found!")
                input("\nPress 'Enter' to continue...")
                break
            
        except ValueError:
            print("Invalid input! Please enter valid integers for the review ID, rating, and mountain ID.")

def delete_review():
    print("_______________________________________")
    while(True):
        try:
            user_input = input("\nEnter a number for the review id to delete: ")
            user_input = int(user_input)
            review = Review.find_by_id(user_input)
            if(review):
                review.delete()
                print("\nReview successfully deleted!")
                input("\nPress 'Enter' to continue...")
                break
            else:
                print("\nReview Not Found!")
                input("\nPress 'Enter' to continue...")
            break
        except:
            print("Invalid input! Please try again!")
    
def retrieve_mountain_reviews():
    print("_______________________________________")
    while(True):
        try:
            user_input = input("\nEnter a number for the mountain id to get reviews for: ")
            user_input = int(user_input)
            mountain = Mountain.find_by_id(user_input)
            if(mountain):
                print(f"\nHere are the reviews for {mountain.name}:\n")
                print(mountain.reviews())
            else:
                print("\nMountain Not Found!")
            user_input = input("\nPress 'Enter' to continue...")
            break
        except:
            print("Invalid input! Please try again!")