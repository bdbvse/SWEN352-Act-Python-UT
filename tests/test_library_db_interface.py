import unittest
from unittest.mock import Mock

from library import library_db_interface
from library.patron import Patron


class TestLibraryDBInterface(unittest.TestCase):

    def setUp(self):
        self.db_interface = library_db_interface.Library_DB()

    def tearDown(self):
        self.db_interface.close_db()

    def test_insert_patron_not_in_db(self):
        expected_db_id = 10
        patron = Patron('name', 'name', 60, 'memberID')
        self.db_interface.retrieve_patron = Mock(return_value=None)
        data = {'fname': 'name', 'lname': 'name', 'age': 'age', 'memberID': 'memberID',
                'borrowed_books': []}
        self.db_interface.convert_patron_to_db_format = Mock(return_value=data)
        self.db_interface.db.insert = Mock(side_effect=lambda x: expected_db_id if x==data else 0)
        self.assertEqual(self.db_interface.insert_patron(patron), expected_db_id)
