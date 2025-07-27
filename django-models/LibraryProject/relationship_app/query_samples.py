import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Create sample data
author = Author.objects.create(name="J.K. Rowling")
book1 = Book.objects.create(title="HP1", author=author)
book2 = Book.objects.create(title="HP2", author=author)

library_name = "My Library"
library = Library.objects.create(name=library_name)
library.books.add(book1, book2)

Librarian.objects.create(name="Sarah", library=library)

# Required queries
books = Book.objects.filter(author__name="J.K. Rowling")

library_instance = Library.objects.get(name=library_name)  # ✅ THIS LINE EXACTLY

books_in_library = library_instance.books.all()
librarian_name = library_instance.librarian.name

