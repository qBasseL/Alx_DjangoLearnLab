# Update the title from “1984” to “Nineteen Eighty-Four”
from your_app_name.models import Book

book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

print(book.title)

# Expected Output:
# Nineteen Eighty-Four
