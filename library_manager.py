# A CLI library manager. 

# UI: list: choice : action :

library:list = [];

def show_banner():
    print("\n ░░ BOOKORY -- Read. Remember. Repeat. ░░")
show_banner()

def success_message(message):
    print(f"\n ↪ {message} \n")

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
    
    
    
    #Remove book
    elif choice == '3': 
        # logic: ask for title => see if it exists in library => if it does remove the book from library, & throw an error if it doesn't exist 
        
        title = input("What's the name of the book you want to remove?")
        
        book_is_in_library: bool = False 
        
        for book in library:
            if book['title'].lower() == title.lower():  # first turn into lowercase then cmpare
                library.remove(book)
                book_is_in_library = True
                break
            
        # errors 
        if book_is_in_library:
            success_message(f"'{title}' has been moved from the shelf!")
        else:
            success_message(f"'{title}' is already missing from shelf")
        
    elif choice == '4':
        pass  # Show stats
    
    
    # Add book functionality yahan aayegi
    elif choice == '5':
        
        # Logic:  User se title, author, year, genre, aur read status pooch kr usse dictionary k thru library list me daal do.
        # Read status == boolean --- then append dictionary into library
        
        print("\n ___Please answer the following questions about the book__ \n")
        title = input("\n book title: ")
        author = input("\n author name: ")
        year = int(input("\n publication year: "))
        genre = input("\n genre: ")
        read_input = input("\n Have you ever read this book? (yes/no): ").lower()
        read_status = True if read_input == 'yes' else False

        # Book dictionary/object 
        book = {
            "title": title,
            "author": author,
            "year": year,
            "genre": genre,
            "read": read_status
        }

        library.append(book) 
        success_message(f"'{title}' — added to your Shelf!")
        
    
    
    # bye-bye
    elif choice == '6':
        print("Hope to see you again soon!")
        break
    
    # error handling (kind-of)
    else:
        print("\n-- Try again with order number of your command this time.")
        break