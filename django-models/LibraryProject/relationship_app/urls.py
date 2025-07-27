from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    add_book,
    edit_book,
    delete_book,
    register,
    admin_view,
    librarian_view,
    member_view,
    LibraryDetailView,  # <-- ADD THIS
)
from .views import list_books
from . import views

urlpatterns = [
    # Authentication views
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),

    # Book views
    path('books/', list_books, name='list_books'),
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:pk>/', edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', delete_book, name='delete_book'),

    # Role-based views
    path('admin_view/', admin_view, name='admin_view'),
    path('librarian_view/', librarian_view, name='librarian_view'),
    path('member_view/', member_view, name='member_view'),

    # Class-based view for library detail
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]

