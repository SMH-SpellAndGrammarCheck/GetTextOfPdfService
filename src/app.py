from flask import Flask, request
from flask_restful import Api
import os
from src.PdfHandler import PdfHandler

app = Flask(__name__)
api = Api(app)

local_dir = 'C:/test/local/'

pdf_handler = PdfHandler()


@app.route('/tasks', methods=['POST', 'DELETE'])
def api_task():
    if request.method == 'POST':
        print('tasks/POST')
        print(request.headers)

        local_file = local_dir + str(request.headers['correlationid']) + '.pdf'
        request.files['pdf'].save(local_file)
        pdf_handler.read_file(local_file)
        return '200'

    elif request.method == 'DELETE':
        print('tasks/DELETE')
        os.remove(local_dir + str(request.headers['correlationid']) + '.pdf')
        return '200'

    return 'error'


if __name__ == '__main__':
    app.run(port=5002)

