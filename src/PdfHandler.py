import tika
from tika import parser
from azure.servicebus import ServiceBusService, Message, Queue
import json

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
        split = content.replace('\n', '').split('.')
        #print(content)

        queue_data = load_queue_credentials()
        print(queue_data['namespace'])
        print(queue_data['key_name'])
        print(queue_data['key_value'])
        bus_service = ServiceBusService(
            service_namespace=queue_data['namespace'],
            shared_access_key_name=queue_data['key_name'],
            shared_access_key_value=queue_data['key_value'])

        #for part in split:
        #send part to queue
        print("sending...")
        msg = Message('test')
        bus_service.send_queue_message('texttoworker', msg)
        print("done?")
        # split content
        # package content
        # send packages

        # todo return content

def load_queue_credentials():
    #todo change path
    return json.load(open('D:/workspace/cloud hackathon/GetTextOfPdfService/src/queue.json'))
