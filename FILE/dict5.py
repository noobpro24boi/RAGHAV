book_dict = {
  "To Kill a Mockingbird": "Harper Lee",
  "1984": "George Orwell",
  "The Catcher in the Rye": "J.D. Salinger",
  "The Great Gatsby": "F. Scott Fitzgerald",
  "Pride and Prejudice": "Jane Austen"
}
book = input("Enter a book title: ")
if book in book_dict:
  print(book + " was written by " + book_dict[book] + ".")
else:
  print("Sorry, that book is not in the library.")
