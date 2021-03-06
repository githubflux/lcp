from marshmallow.fields import Bool, DateTime as Date_Time, Nested, Str
from schema.base import Base_Schema
from utils.datetime import FORMAT
from utils.schema import List_or_One

__all__ = [
    'Code_Request_Schema'
]


# FIXME add missing required fields
class Code_Request_Schema(Base_Schema):
    """Request for code endpoint."""

    id = Str(required=True, example='firewall',
               description='Code id.')
    code = List_or_One(Str, required=True,
                       description='Code source')
