import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Clear all data (for testing)
Author.objects.all().delete()
Book.objects.all().delete()
Library.objects.all().delete()
Librarian.objects.all().delete()

# Create sample data
author = Author.objects.create(name="J.K. Rowling")
book1 = Book.objects.create(title="Harry Potter 1", author=author)
book2 = Book.objects.create(title="Harry Potter 2", author=author)

library = Library.objects.create(name="Downtown Library")
library = Library.objects.create(name=library_name)
library.books.add(book1, book2)

librarian = Librarian.objects.create(name="John Doe", library=library)

# 1. All books by J.K. Rowling
print("Books by J.K. Rowling:")
for book in Book.objects.filter(author__name="J.K. Rowling"):
    print(f"- {book.title}")

# 2. All books in the Downtown Library
print("\nBooks in Downtown Library:")
for book in library.books.all():
    print(f"- {book.title}")

# 3. Librarian of the Downtown Library
print(f"\nLibrarian of {library.name}: {library.librarian.name}")
