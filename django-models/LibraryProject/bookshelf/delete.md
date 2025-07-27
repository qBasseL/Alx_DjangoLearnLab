# Delete the book
from bookshelf.models import Book


book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion
books = Book.objects.all()
print(list(books))

# Expected Output:
# []
# (An empty list indicates the book was deleted successfully.)
