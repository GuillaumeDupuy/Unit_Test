# import pytest
import sys
import unittest

sys.path.append('') # permet d'importer les modules du dossier parent
from scripts.library import Book, Library, Client

# Unit Test

class TestLibraryMethods(unittest.TestCase):

    def setUp(self):
        self.library = Library()
        self.book1 = Book("To Kill a Mockingbird", "Harper Lee")
        self.library.add_book(self.book1)
        self.book2 = Book("Pride and Prejudice", "Jane Austen")
        self.library.add_book(self.book2)

    def test_add_book(self):
        self.assertIn(self.book1, self.library.books)
        self.assertIn(self.book2, self.library.books)
        self.assertEqual(f"{self.book1.title} by {self.book1.author} has been added to the library.", 
                        "To Kill a Mockingbird by Harper Lee has been added to the library.")
        self.assertEqual(f"{self.book2.title} by {self.book2.author} has been added to the library.", 
                        "Pride and Prejudice by Jane Austen has been added to the library.")

    def test_check_out_book(self):
        self.library.check_out_book("To Kill a Mockingbird")
        self.assertTrue(self.book1.is_checked_out)
        self.library.check_out_book("Pride and Prejudice")
        self.assertTrue(self.book2.is_checked_out)

    def test_check_in_book(self):
        self.library.check_out_book("To Kill a Mockingbird")
        self.library.check_out_book("Pride and Prejudice")
        self.library.check_in_book("To Kill a Mockingbird")
        self.assertFalse(self.book1.is_checked_out)
        self.library.check_in_book("Pride and Prejudice")
        self.assertFalse(self.book2.is_checked_out)



if __name__ == '__main__':
    unittest.main()