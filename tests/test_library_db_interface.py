import unittest
from unittest.mock import Mock, call
from library import library_db_interface
from library.patron import Patron


class TestLibraryDBInterface(unittest.TestCase):

    def setUp(self):
        self.db_interface = library_db_interface.Library_DB()

    def tearDown(self):
        self.db_interface.close_db()

    def test_insert_patron_not_in_db(self):
        patron_mock = Mock()
        self.db_interface.retrieve_patron = Mock(return_value=None)
        data = {'fname': 'name', 'lname': 'name', 'age': 'age', 'memberID': 'memberID',
                'borrowed_books': []}
        self.db_interface.convert_patron_to_db_format = Mock(return_value=data)
        self.db_interface.db.insert = Mock(side_effect=lambda x: 10 if x==data else 0)
        self.assertEqual(self.db_interface.insert_patron(patron_mock), 10)

    def test_update_patron(self):
        data = {'fname': 'name', 'lname': 'name', 'age': 'age', 'memberID': 'memberID',
                'borrowed_books': []}
        self.db_interface.convert_patron_to_db_format = Mock(return_value=data)
        db_update_mock = Mock()
        self.db_interface.db.update = db_update_mock
        self.db_interface.update_patron(Mock())
        db_update_mock.assert_called()

    def test_convert_patron_to_db_format(self):
        patron = Patron('Fred', 'Cartz', 3, '4')
        self.assertEqual(self.db_interface.convert_patron_to_db_format(patron),
                         {'fname': 'Fred', 'lname': 'Cartz', 'age': 3, 'memberID': '4',
                          'borrowed_books': []})
