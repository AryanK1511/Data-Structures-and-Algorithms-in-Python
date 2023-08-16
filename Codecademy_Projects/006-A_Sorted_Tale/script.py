import utils
import sorts

def by_title_ascending(book_a, book_b):
  return book_a['title_lower'] > book_b['title_lower']

def by_author_ascending(book_a, book_b):
  return book_a['author_lower'] > book_b['author_lower']

def by_total_length(book_a, book_b):
  return len(book_a['author_lower']) > len(book_b['author_lower'])

bookshelf = utils.load_books('books_small.csv') # Put absolute path here
long_bookshelf = utils.load_books('books_large.csv') # Put absolute path here
bookshelf_v1 = bookshelf.copy()
bookshelf_v2 = bookshelf.copy()
long_bookshelf_v1 = long_bookshelf.copy()
long_bookshelf_v2 = long_bookshelf.copy()

print("==========")
sort_1 = sorts.bubble_sort(bookshelf, by_title_ascending)
for book in sort_1:
  print(book['title'])
print()

print("==========")
sort_2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)
for book in sort_2:
  print(book['author'])
print()

print("==========")
sort_3 = sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2) - 1, by_author_ascending)
for book in bookshelf_v2:
  print(book['author'])
print()

print("==========")
sort_4 = sorts.bubble_sort(long_bookshelf_v1, by_total_length)
for book in sort_4:
  print(book['title'])
print()

print("==========")
sort_5 = sorts.quicksort(long_bookshelf_v2, 0, len(bookshelf_v2) - 1, by_total_length)
for book in long_bookshelf_v2:
  print(book['title'])
print()