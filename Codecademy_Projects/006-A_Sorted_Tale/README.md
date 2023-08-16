# A Sorted Tale

You recently began employment at **"A Sorted Tale"**, an independent bookshop. Every morning, the owner decides to sort the books in a new way.

Some of his favorite methods include:

- By author name
- By title
- By the number of characters in the title
- By the reverse of the author’s name

Throughout the day, patrons of the bookshop remove books from the shelf. Given the strange ordering of the store, they do not always get the books placed back in exactly the correct location.

The owner wants you to research methods of fixing the book ordering throughout the day and sorting the books in the morning. It is currently taking too long!

## Tasks

- [x] Get to know the data
   1. The owner provides the current state of the bookshelf in a comma-separated values, or csv, file. To get you started, we have provided a function `load_books`, defined in `utils.py`.
   2. Add a for loop to print the titles within the bookshelf.

- [x] Fix the midday errors
   3. Determine the code point of certain characters using Python’s `ord` function.
   4. Convert everything to lowercase prior to comparison.
   5. Implement bubble sort with a flexible comparison function.

- [x] A new sorting order
   6. Define a comparison function, `by_title_ascending`, for sorting by title.
   7. Sort the bookshelf using bubble sort.
   8. Define a new comparison function, `by_author_ascending`, for sorting by author.

- [x] A new sorting algorithm
   9. Create a copy of the bookshelf.
   10. Sort the bookshelf copy using quicksort and the `by_author_ascending` comparison function.

- [x] The last sort
   11. Create a new comparison function, `by_total_length`, based on the sum of characters in the title and author's name.
   12. Load a long list of books from `books_large.csv` into a new variable, `long_bookshelf`.
   13. Sort `long_bookshelf` using bubble sort with `by_total_length` comparison.
   14. Comment out the bubble sort attempt and use quicksort with the `by_total_length` comparison.

- [x] More sorting
   15. Explore creating your own comparison operators or other sorting functions.

