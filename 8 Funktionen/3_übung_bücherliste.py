books = []

def add_book(book_name):
  books.append(book_name)
  print(f"Added {book_name} to list")

add_book("Es")
add_book("Harry Potter")
add_book("C Programmieren")

print(books)