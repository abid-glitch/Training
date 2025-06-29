class BookHub:

    def __init__(self, books_available, lib_name):
        self.books = books_available
        self.lib_name = lib_name
        self.issued = {}

    def showBooks(self):
        print(f"Books in the library: {self.lib_name}")
        for item in self.books:
            print(item)

    def lend(self, borrower, item):
        if item not in self.books:
            print("This book is currently not in stock.")
        elif item in self.issued:
            print(f"This book is with {self.issued[item]}")
        else:
            self.issued[item] = borrower
            print("Book lending updated successfully.")

    def add(self, item):
        self.books.append(item)
        print(f"{item} added to library.")

    def returnBack(self, item):
        if item in self.issued:
            del self.issued[item]
            print("Thanks for returning the book.")
        else:
            print("This item wasn't borrowed from here.")

if __name__ == '__main__':
    lib = BookHub([
        'Python', 'Rich Dad Poor Dad', 'Harry Potter', 'C++ Basics',
        'Algorithms by CLRS'
    ], "Skill Library")
    user = input("Enter your name to access the library: ")

    while True:
        print(f"\nHi {user}, you're at {lib.lib_name}. Choose an option:")
        print("1. Show Books\n2. Lend Book\n3. Add Book\n4. Return Book\n5. Exit")
        option = input("Your choice: ")

        if option not in ['1', '2', '3', '4', '5']:
            print("Invalid input. Try again.")
            continue

        if option == '1':
            lib.showBooks()
        elif option == '2':
            name = input("Book to lend: ")
            lib.lend(user, name)
        elif option == '3':
            name = input("Book to add: ")
            lib.add(name)
        elif option == '4':
            name = input("Book to return: ")
            lib.returnBack(name)
        elif option == '5':
            print(f"Goodbye {user}, visit again!")
            break
