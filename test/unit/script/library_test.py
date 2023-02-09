import pytest

from scripts.library import Book, Library, Client

# Pytest

def test_book():
    # Test check_out method
    book = Book("To Kill a Mockingbird", "Harper Lee")
    assert not book.is_checked_out
    book.check_out()
    assert book.is_checked_out

    # Test check_in method
    book.check_in()
    assert not book.is_checked_out

def test_library():
    library = Library()

    # Test add_book method
    book = Book("To Kill a Mockingbird", "Harper Lee")
    library.add_book(book)
    assert book in library.books

    # Test check_out_book method
    library.check_out_book("To Kill a Mockingbird")
    assert book.is_checked_out
    library.check_out_book("Pride and Prejudice")
    # Check error message for not available book
    # by using assertRaises context manager
    with pytest.raises(Exception) as e:
        library.check_out_book("Pride and Prejudice")
    assert str(e.value) == "Sorry, Pride and Prejudice is not available."

    # Test check_in_book method
    library.check_in_book("To Kill a Mockingbird")
    assert not book.is_checked_out
    library.check_in_book("Pride and Prejudice")
    # Check error message for not in library book
    # by using assertRaises context manager
    with pytest.raises(Exception) as e:
        library.check_in_book("Pride and Prejudice")
    assert str(e.value) == "Sorry, Pride and Prejudice is not in the library."

def test_client():
    library = Library()
    book = Book("To Kill a Mockingbird", "Harper Lee")
    library.add_book(book)

    # Test check_out_book method
    client = Client("John Doe")
    client.check_out_book(library, "To Kill a Mockingbird")
    assert book.is_checked_out
    assert book in client.checked_out_books
    client.check_out_book(library, "Pride and Prejudice")
    # Check error message for not available book
    # by using assertRaises context manager
    with pytest.raises(Exception) as e:
        client.check_out_book(library, "Pride and Prejudice")
    assert str(e.value) == "Sorry, Pride and Prejudice is not available."

    # Test check_in_book method
    client.check_in_book(library, "To Kill a Mockingbird")
    assert not book.is_checked_out
    assert book not in client.checked_out_books
    client.check_in_book(library, "Pride and Prejudice")
    # Check error message for not checked out book
    # by using assertRaises context manager
    with pytest.raises(Exception) as e:
        client.check_in_book(library, "Pride and Prejudice")
    assert str(e.value) == "Sorry, Pride and Prejudice is not checked out."

# Unit Test
import unittest

class TestClientMethods(unittest.TestCase):

    def setUp(self):
        self.library = Library()
        self.book1 = Book("To Kill a Mockingbird", "Harper Lee")
        self.library.add_book(self.book1)
        self.book2 = Book("Pride and Prejudice", "Jane Austen")
        self.library.add_book(self.book2)
        self.client = Client("John Doe")

    def test_check_out_book(self):
        # Test check_out_book for valid input
        self.client.check_out_book(self.library, "To Kill a Mockingbird")
        self.assertTrue(self.book1.is_checked_out)
        self.assertIn(self.book1, self.client.checked_out_books)
        
        # Test check_out_book for not available book
        try:
            self.client.check_out_book(self.library, "Not a Book")
        except Exception as e:
            self.assertEqual(str(e), "Sorry, Not a Book is not available.")

    def test_check_in_book(self):
        # Test check_in_book for valid input
        self.client.check_out_book(self.library, "To Kill a Mockingbird")
        self.client.check_in_book(self.library, "To Kill a Mockingbird")
        self.assertFalse(self.book1.is_checked_out)
        self.assertNotIn(self.book1, self.client.checked_out_books)
        
        # Test check_in_book for not checked out book
        with self.assertRaises(Exception) as context:
            self.client.check_in_book(self.library, "Pride and Prejudice")
        self.assertEqual(str(context.exception), "Sorry, Pride and Prejudice is not checked out.")

if __name__ == '__main__':
    unittest.main()