import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Create sample data
author_name = "J.K. Rowling"
author = Author.objects.create(name=author_name)

book1 = Book.objects.create(title="HP1", author=author)
book2 = Book.objects.create(title="HP2", author=author)

library_name = "My Library"
library = Library.objects.create(name=library_name)
library.books.add(book1, book2)

librarian = Librarian.objects.create(name="Sarah", library=library)

# ✅ REQUIRED: Author.objects.get(name=author_name)
author = Author.objects.get(name=author_name)

# ✅ REQUIRED: Book.objects.filter(author=author)
books_by_author = Book.objects.filter(author=author)
print("Books by J.K. Rowling:")
for book in books_by_author:
    print(f"- {book.title}")

# ✅ REQUIRED: Library.objects.get(name=library_name)
library_instance = Library.objects.get(name=library_name)
print(f"\nBooks in {library_name}:")
for book in library_instance.books.all():
    print(f"- {book.title}")

# ✅ REQUIRED: Librarian.objects.get(library=...)
librarian_for_library = Librarian.objects.get(library=library_instance)
print(f"\nLibrarian of {library_name}: {librarian_for_library.name}")

