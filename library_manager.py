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
    
    
    # Search book
    if choice == '1':
        
        search_by = input("\n Search by, -Title -Author -Genre (1-3)")
        
        if search_by == "1":
            search_prompt = input("\n Tell me Title of the book you're looking for.")
            search_key = "title"
            
        elif search_by == "2":
            search_prompt = input("What's the name of the author you're looking for?")
            search_key = "author"
        
        elif search_by == "3":
            search_prompt = input("which genre?")
            search_key = "genre"
        
        else:
            print("\n Please select an option from the list:")
            continue
        
        # actual search functionality:
        found_books:list = [book for book in library if search_prompt.lower() in book[search_key].lower()]
        
        if found_books :
            success_message(f"Found {len(found_books)} books: \n Here's what I found:")
            for book in found_books :
                success_message(f" \nTitle: {book['title']}\nAuthor: {book['author']}\nYear: {book['year']}\nGenre: {book['genre']}\nRead Status: {'Read' if book['read'] else 'Unread'}\n")
        else :
            success_message(f"No books found matching '{search_prompt}'.")
    
    # Display all books
    elif choice == '2':
        
        if library :
            print("\n_Your Personal Shelf Space_")
            
            for index, book in enumerate(library, start=1):
                success_message(f"Book {index}:")
                print(f"  Title       : {book['title']}")
                print(f"  Author      : {book['author']}")
                print(f"  Year        : {book['year']}")
                print(f"  Genre       : {book['genre']}")
                print(f"  Read Status : {'Read' if book['read'] else 'Unread'}")
        else:
            print("\nIts Empty, Start adding books!")
            
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
        
    
    # Show stats
    elif choice == '4':
        if library:
            total_books = len(library);
            read_books = sum(1 for book in library if book['read']) # +1 if a book id read
            read_percentage = (read_books/total_books)* 100 
            
            success_message(f"You have {total_books} total books in your private shelf.")
            print(f"{read_books} books read.")
            print(f"total {total_books - read_books} books are waiting for your attention.")
            print(f"So far, your book dedication percentage is: {read_percentage:.2f}%")
                
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
        
        try:
            year = int(input("\n Publication year: "))
        except ValueError:
            print("Invalid input! Please enter a valid year.")
            continue

        

        library.append(book) 
        success_message(f"'{title}' — added to your Shelf!")
        
    
    
    # bye-bye
    elif choice == '6':
        success_message("Thank you for using Bookory! \n Hope to see you again soon!")
        break
    
    # error handling (kind-of)
    else:
        print("\n-- Try again with order number of your command this time.")
        continue