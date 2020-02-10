import falcon

from middleware import Auth, RequireJSON
from route import Code, Config, Status

api = falcon.API(middleware=[
    Auth(),
    RequireJSON()
])

status = Status()
code = Code(status)
config = Config(status)

api.add_route('/code', Code())
api.add_route('/config', Config())
api.add_route('/status', Status())
