import falcon

class Code(object):
    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200
