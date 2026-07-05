books = ["Harry Potter", "Matilda", "The Jungle Book", "Vikines", "Tempest"]

print("Library Book List:", books)



print("\nTotal Books:", len(books))
print("First Book:", books[0])
print("Last Book:", books[-1])
print("First Three Books:", books[3])

books.append("Diary of a Wimpy Kid")
print("\nAfter Adding a Book:", books)

books.remove("The Jungle Book")
print("After Removing a Book:", books)

books.sort()
print("Books Sorted Alphabetically:", books)

books.reverse()
print("Books in Reverse Order:", books)


librarian = {
    "name": "Ms. Aisha",
    "section": "Young Readers",
    "experience": 8
}

print("\nLibrarian Profile:", librarian)




print("Librarian Name:", librarian["name"])
print("Library Section:", librarian["section"])
print("Experience:", librarian["experience"])

librarian["experience"] = 6
print("\nUpdated Experience:", librarian)

librarian["email"] = "aisha@schoollibrary.com"
print("After Adding Email:", librarian)

librarian.pop("section")
print("After Removing Section:", librarian)

book_ids = [101, 102, 103, 104, 105]
book_names = [
    "Matilda",
    "Wonder",
    "Harry Potter",
    "Vikines",
    "Diary of a Wimpy Kid"
]

book_directory = dict(zip(book_ids, book_names))

print("\nBook Directory:", book_directory)


print("\n================================")
print("LIBRARY ORGANISER SUMMARY")
print("================================")
print("Available Books:", books)
print("Librarian Details:", librarian)
print("Book ID Directory:", book_directory)
print("================================")