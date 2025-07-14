# Retrieve and display all attributes of the created book
from your_app_name.models import Book

book = Book.objects.get(title="1984")
print(book.title)
print(book.author)
print(book.publication_year)

# Expected Output:
# 1984
# George Orwell
# 1949
