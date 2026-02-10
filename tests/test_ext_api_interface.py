import os
import unittest
from library import ext_api_interface
from unittest.mock import Mock
import requests
import json

class TestExtApiInterface(unittest.TestCase):
    def setUp(self):
        self.api = ext_api_interface.Books_API()
        self.book = "Learning Python"
        self.rootPath = './'
        if os.getcwd().__contains__('tests'):
            self.rootPath = '../'
        with open(self.rootPath + 'tests_data/ebooks.json', 'r') as f:
            self.books_data = json.loads(f.read())
        with open(self.rootPath + 'tests_data/openlib_sample_data.json', 'r') as f:
            self.json_data = json.loads(f.read())

    def test_is_book_available_connection_error(self):
        ext_api_interface.requests.get = Mock(side_effect=requests.ConnectionError)
        self.assertFalse(self.api.is_book_available('bogus book'))

    def test_get_ebooks(self):
        self.api.make_request = Mock(return_value=self.json_data)
        self.assertEqual(self.api.get_ebooks(self.book), self.books_data)
