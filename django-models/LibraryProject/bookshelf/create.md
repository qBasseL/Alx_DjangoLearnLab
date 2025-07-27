# Create a Book instance
from your_app_name.models import Book

book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)

# Expected Output:
# <Book: Book object (1)>
# (Note: The number may vary depending on your database state.)

