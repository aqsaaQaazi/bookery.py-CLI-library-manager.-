# A CLI library manager. 

# UI: list: choice : action :

library:list = [];

def show_banner():
    print("\n ░░ BOOKORY -- Read. Remember. Repeat. ░░")
show_banner()


# menu
def menu ():
    print("\n Librarian here, how can I help you?\n")
    print("1. Find me a Book")
    print("2. Take me to my personal shelf.")
    print("3. I Want to Remove a Book")
    print("4. What's my progress?")
    print("5. lets Add a New Book")
    print("6. Nothing.. bye!")
    
# a never ending loop so it shows menu everytime until user exits.

while True:
    menu();
    choice = input("Enter the serial of desired command. (1-6):")
    
    
    if choice == '1':
        pass  # Search book
    elif choice == '2':
        pass  # Display all books
    elif choice == '3':
        pass  #Remove book
    elif choice == '4':
        pass  # Show stats
    elif choice == '5':
        pass
        # Add book functionality yahan aayegi
        
        # Logic:  User se title, author, year, genre, aur read status pooch kr usse dictionary k thru library list me daal do.

        # Read status == boolean --- then append dictionary into library
    elif choice == '6':
        print("Hope to see you again soon!")
        break
    else:
        print("\n-- Try again with order number of your command this time.")
        break