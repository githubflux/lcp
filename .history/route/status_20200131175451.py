import falcon
import uuid
import requests

class Status(object):
    def __init__(self, cb_host, cb_port):
        self.id = uuid.uuid1()
        data = {
            'hostname': '', # TODO
            'id': str(self.id),
            'type_id': '' # TODO
        }
        response = requests.post(f'{cb_host}:{cb_port}', dat =data)
        self.connected_to_cb = False
        self.agents = []
        print(f'Execute Environment ID: {self.id}')

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.media = {
            'id': str(self.id),
            'connected-to-cb': self.connected_to_cb,
            'agents': self.agents
        }
