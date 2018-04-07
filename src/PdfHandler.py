import tika
from tika import parser


class PdfHandler:

    def __init__(self):
        print('initializing pdf reader...')
        tika.initVM()
        print('done.')

    def read_file(self, file) -> str:
        print('file: ' + str(file))
        parsed = parser.from_file(file)
        print(parsed['metadata'])
        content = parsed['content']
        # split content
        # package content
        # send packages

        # todo return content
