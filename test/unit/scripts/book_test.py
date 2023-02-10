import unittest
import sys

sys.path.append('') # permet d'importer les modules du dossier parent
from scripts.library import Book, Library, Client

class TestBookMethods(unittest.TestCase):

    def setUp(self):
        self.book = Book("To Kill a Mockingbird", "Harper Lee")

    def test_check_out(self):
        self.book.check_out()
        self.assertTrue(self.book.is_checked_out)
        self.assertEqual(f"{self.book.title} by {self.book.author} has been checked out.", 
                        "To Kill a Mockingbird by Harper Lee has been checked out.")

    def test_check_in(self):
        self.book.check_out()
        self.book.check_in()
        self.assertFalse(self.book.is_checked_out)
        self.assertEqual(f"{self.book.title} by {self.book.author} has been checked in.", 
                        "To Kill a Mockingbird by Harper Lee has been checked in.")

if __name__ == '__main__':
    unittest.main()