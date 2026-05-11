# =================================
#     LIBRARY MANAGEMENT SYSTEM
# =================================

class LibraryManagement:

    def __init__(self):
        self.books = {}

    # 1. ADD BOOK
    def addBook(self):

        bookId = int(input("Enter Book ID : "))
        bookName = input("Enter Book Name : ")
        author = input("Enter Author Name : ")

        self.books[bookId] = [bookName, author, "Available"]

        print("Book Added Successfully!")

    # 2. VIEW BOOKS
    def viewBooks(self):

        if len(self.books) == 0:
            print("No Books Available!")
            return

        print("\n========== BOOK RECORDS ==========")

        for bookId in self.books:

            print("Book ID    :", bookId)
            print("Book Name  :", self.books[bookId][0])
            print("Author     :", self.books[bookId][1])
            print("Status     :", self.books[bookId][2])
            print("----------------------------------")

    # 3. SEARCH BOOK
    def searchBook(self):

        bookId = int(input("Enter Book ID : "))

        if bookId in self.books:

            print("\nBook Found!")
            print("Book Name :", self.books[bookId][0])
            print("Author    :", self.books[bookId][1])
            print("Status    :", self.books[bookId][2])

        else:
            print("Book Not Found!")

    # 4. ISSUE BOOK
    def issueBook(self):

        bookId = int(input("Enter Book ID : "))

        if bookId in self.books:

            if self.books[bookId][2] == "Available":

                self.books[bookId][2] = "Issued"

                print("Book Issued Successfully!")

            else:
                print("Book Already Issued!")

        else:
            print("Book Not Found!")

    # 5. RETURN BOOK
    def returnBook(self):

        bookId = int(input("Enter Book ID : "))

        if bookId in self.books:

            if self.books[bookId][2] == "Issued":

                self.books[bookId][2] = "Available"

                print("Book Returned Successfully!")

            else:
                print("Book is Already Available!")

        else:
            print("Book Not Found!")

    # 6. DELETE BOOK
    def deleteBook(self):

        bookId = int(input("Enter Book ID : "))

        if bookId in self.books:

            del self.books[bookId]

            print("Book Deleted Successfully!")

        else:
            print("Book Not Found!")


# =================================
#         MAIN PROGRAM
# =================================

obj = LibraryManagement()

while True:

    print("\n========== LIBRARY MENU ==========")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Exit")
    print("==================================")

    choice = input("Enter Your Choice : ")

    if choice == "":
        print("Please Enter a Number!")
        continue

    choice = int(choice)

    if choice == 1:
        obj.addBook()

    elif choice == 2:
        obj.viewBooks()

    elif choice == 3:
        obj.searchBook()

    elif choice == 4:
        obj.issueBook()

    elif choice == 5:
        obj.returnBook()

    elif choice == 6:
        obj.deleteBook()

    elif choice == 7:
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")