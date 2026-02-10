import sys
sys.path.append('.')

from library import ext_api_interface
import json


class GetData:
    def __init__(self):
        self.api = ext_api_interface.Books_API()

    def get_ebooks(self, book: str) -> None:
        print("get ebooks: " + book)
        ebooks = self.api.get_ebooks(book)
        print(ebooks)
        with open('tests_data/ebooks.json', 'w') as f:
            f.write(json.dumps(ebooks))

    def get_json(self, book:str):
        json_data = self.api.make_request({'q': book})
        print(json_data)
        with open('tests_data/openlib_sample_data.json', 'w') as f:
            f.write(json.dumps(json_data))

if __name__ == "__main__":
    getdata = GetData()
    getdata.get_ebooks('learning python')
    getdata.get_json('learning python')
