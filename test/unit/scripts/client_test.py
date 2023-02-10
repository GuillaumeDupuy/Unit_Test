import sys
import unittest

sys.path.append('') # permet d'importer les modules du dossier parent
from scripts.library import Book, Library, Client

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