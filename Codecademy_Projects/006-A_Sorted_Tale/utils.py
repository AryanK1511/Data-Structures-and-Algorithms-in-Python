import csv

# This code loads the current book
# shelf data from the csv file
def load_books(filename):
  bookshelf = []
  with open(filename, "r") as file:
        if file:
            shelf = csv.DictReader(file)
            for book in shelf:
                book['author_lower'] = book['author'].lower()
                book['title_lower'] = book['title'].lower()
                bookshelf.append(book)
        else:
            print("File not found!")
  return bookshelf