# Bookory: - Read. Remember. Repeat. 

#### A Command-Line Personal Library Manager

## Project Overview

**Bookory** is another command-line tool/project that helps user manage their personal book collection. 
With just a few commands, you can add, remove, search, and track your books. It’s a fun little project I built as part of an assignment, and it’s designed to help you stay organized while keeping things easy to use.

In this project, I explored Python's basics, like lists, dictionaries, loops, and user input handling, while making sure the experience felt smooth and intuitive. The process was enjoyable and gave me the chance to put my skills to good use!

## Features

- **Add Book**: Quickly add new books to your collection with details like title, author, year, genre, and read status.
- **Remove Book**: Search for a book by title and remove it from your library.
- **Search for a Book**: Look for a book by its title, author, or genre.
- **Display All Books**: View your entire book collection in a neatly formatted list.
- **View Stats**: Get an overview of your reading progress with details like total books, books read, unread books, and your overall reading percentage.

## How to Use

1. **Run the Program**: Launch the script to begin using the tool.
2. **Interact with the Menu**: You'll be presented with a list of options. Here's what you can do:
   - Find a book
   - View your personal shelf (all books in your collection)
   - Remove a book
   - Check your reading stats
   - Add a new book
   - Exit the program
3. **Follow Prompts**: Each option will ask for your input to proceed. Just follow the on-screen prompts, and the program will handle the rest.
4. **Check Your Stats**: When you want to see how much you've read, check your reading progress stats!

## Installation

To get started with **Bookory**, follow these simple steps:

1. Make sure **Python** is installed on your system (Python 3.6 or newer).
2. Clone this repository to your local machine:
   ```git clone https://github.com/aqsaaQaazi/bookery.py-CLI-library-manager.-```

3. Navigate to the project folder and run the script:

```python library_manager.py```

## Developer Details

### **Author**
- **Name**: Aqsaa Qaazi
- **Role**: Solo
- **Email**: aqsaakqaazi@gmail.com

### **Technologies Used**
- **Python**: The core programming language used to build this command-line tool.
- **Python List & Dictionary**: Used to store and manage books and their details.
- **String Manipulation**: Employed for user inputs, book searches, and displaying formatted results.

### **Project Context**
This project is part of an assignment and is intended to demonstrate basic functionality such as:
- Managing a collection of books.
- Storing book details in dictionaries.
- Handling user input and providing interactive feedback.
- Displaying basic statistics and managing a personal library efficiently.

### **Version**
- **Version**: 1.3.0
- **Date**: 04-06-2025


## Code Explanation

Here’s a quick rundown of how things work behind the scenes:

### **Library Storage**
A list of dictionaries holds all the book data. Each book is stored as a dictionary with the following attributes:

- **title**: The name of the book.
- **author**: The author(s) of the book.
- **year**: The year of publication.
- **genre**: The genre the book falls under.
- **read**: A boolean value representing whether the book has been read (`True` if read, `False` if unread).

This allows the program to easily store, retrieve, and manage the books in the library.

### **Functions**
The program is divided into functions that handle different actions such as adding, removing, and displaying books. Here are the core functions:

- **`menu()`**: Displays the main menu of the application with available options.
- **`show_banner()`**: Displays a welcome message when the program starts.
- **`success_message()`**: Prints success messages to provide feedback to the user when an action is completed.
- **`add_book()`**: Prompts the user to enter book details and adds the book to the library.
- **`remove_book()`**: Prompts the user for a book title and removes the book from the library if it exists.
- **`search_book()`**: Allows the user to search for books by title, author, or genre.
- **`show_stats()`**: Displays statistics such as the total number of books and the percentage of books that have been read.

### **User Input**
The program interacts with the user through the command line. The user is prompted to select actions from the menu by entering the corresponding number. Based on the user’s choice, the program takes the relevant input (e.g., book title, author, etc.), performs the necessary operations (e.g., adding, removing, or searching books), and displays the results.

### **Flow Control**
The program runs in a loop, continually showing the menu and waiting for user input. The loop only ends when the user chooses the exit option (`6`), which breaks the loop and ends the program. This ensures that the user can interact with the library manager until they decide to quit.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to fork the repository, create a branch, and submit a pull request.

### How to Contribute
1. Fork this repository.
2. Create a new branch (`git checkout -b feature-xyz`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-xyz`).
6. Open a pull request.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## If i get enough time, these will be expected Future Improvements

- Implement data persistence to save the library state (e.g., using file handling or a database).
- Add sorting and filtering capabilities for easier book management.
- Implement advanced search (e.g., search by multiple parameters).
- Allow users to update book details (e.g., title, author, genre).


## Acknowledgments

- [Python Official Documentation](https://docs.python.org/3/)
- Any helpful tutorials, forums, or references that helped you build the project.
