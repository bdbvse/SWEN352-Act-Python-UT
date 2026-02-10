import unittest
from unittest.mock import Mock, call
from library import library_db_interface
from library.patron import Patron


class TestLibraryDBInterface(unittest.TestCase):

    def setUp(self):
        self.db_interface = library_db_interface.Library_DB()
        self.patron = Patron('Fred', 'Cartz', 60, '47')

    def tearDown(self):
        self.db_interface.close_db()
        self.db_interface = None
        self.patron = None

    def test_insert_patron_not_in_db(self):
        # setup test
        self.db_interface.retrieve_patron = Mock(return_value=None)
        data = self.db_interface.convert_patron_to_db_format(self.patron)
        self.db_interface.db.insert = Mock(side_effect = lambda x: 10 if x==data else 0)
        # run test
        result = self.db_interface.insert_patron(self.patron)
        # validate test
        self.assertEqual(10, result)

    def test_update_patron(self):
        # setup test
        db_update_mock = Mock(return_value=[1])
        self.db_interface.db.update = db_update_mock
        # run test
        is_successful = self.db_interface.update_patron(self.patron)
        # validate test
        self.assertTrue(is_successful)
        db_update_mock.assert_called()

    def test_convert_patron_to_db_format(self):
        # setup test: N/A
        # run test
        result = self.db_interface.convert_patron_to_db_format(self.patron)
        # validate test
        self.assertEqual({'fname': 'Fred', 'lname': 'Cartz', 'age': 60, 'memberID': '47', 'borrowed_books': []},
                         result)
