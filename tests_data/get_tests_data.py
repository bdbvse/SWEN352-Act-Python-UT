import sys
sys.path.append('.')

from library import ext_api_interface
import json


class GetData:
    def __init__(self):
        self.api = ext_api_interface.Books_API()

    def get_ebooks(self, book):
        print("get ebooks: " + book)
        ebooks = self.api.get_ebooks(book)
        with open('tests_data/ebooks.json', 'w') as f:
            f.write(json.dumps(ebooks))

    def get_json(self, book):
        json_data = self.api.gather_test_data({'q': book.lower()})
        with open('tests_data/openlib_sample_data.json', 'w') as f:
            f.write(json.dumps(json_data))

if __name__ == "__main__":
    getdata = GetData()
    getdata.get_ebooks('learning python')
    getdata.get_json('learning python')
