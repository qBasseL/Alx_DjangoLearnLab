import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Sample data
author_name = "J.K. Rowling"
author = Author.objects.create(name=author_name)
book1 = Book.objects.create(title="HP1", author=author)
book2 = Book.objects.create(title="HP2", author=author)

library_name = "My Library"
library = Library.objects.create(name=library_name)
library.books.add(book1, book2)

Librarian.objects.create(name="Sarah", library=library)

# 1. Get the author object by name
author = Author.objects.get(name=author_name)  # ✅ REQUIRED LINE

# 2. Query all books by that author
books_by_author = Book.objects.filter(author=author)  # ✅ REQUIRED LINE

print("Books by J.K. Rowling:")
for book in books_by_author:
    print(f"- {book.title}")

# 3. Get the library object by name
library_instance = Library.objects.get(name=library_name)  # ✅ REQUIRED LINE

# 4. List all books in the library
print(f"\nBooks in {library_name}:")
for book in library_instance.books.all():
    print(f"- {book.title}")

# 5. Retrieve the librarian for that library
print(f"\nLibrarian of {library_name}: {library_instance.librarian.name}")

