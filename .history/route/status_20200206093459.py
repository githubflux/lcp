from datetime import datetime
import falcon
import uuid


class StatusResource(object):
    response_schema = StatusResponseSchema()

    def __init__(self):
        self.data = {
            'id': str(uuid.uuid1()),
            'agents': [],
            'alive': datetime.now().strftime("%Y/%m/%d-%H:%M:%S")
        }

    def on_get(self, req, resp):
        req.context['result'] = self.data
