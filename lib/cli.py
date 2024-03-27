from helpers import (
    exit_program,
    initialize_database,
    interact_with_mountain_data,
    interact_with_review_data
)

def print_mountain_art():
    mountain_art = """
                            /\\             
            /\\             /  \\                    
           /  \\           /\\/\\/\\    /\\         o |_]
          /\\/\\/\\         //        // \\       `|`|
         //     \\       //        //   \\       //\\          
        //       \\/\\   //        //     \\     //  \\    
       //        // \\ //        //       \\   //    \\
      //        //   \\         //         \\ //      \\       
     //        //     \\       //           //        \\
    //        //       \\     //           //          \\
    """
    print(mountain_art)

def main():
    initialize_database()
    
    while True:
        menu()
        user_input = input("Select an option from the menu: ")
        if user_input == 'q':
            exit_program()
        elif user_input == 'm':
            interact_with_mountain_data()
        elif user_input == 'r':
            interact_with_review_data()
        else:
            print("Invalid input! Please try again!\n")

def menu():
    print_mountain_art()
    print("\nMAIN MENU!\n")
    print("m: Interact with Mountain data")
    print("r: Interact with Review data")
    print("q: Quit the program\n")

if __name__ == "__main__":
    main()