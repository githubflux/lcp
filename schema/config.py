from marshmallow import fields, Schema


class ConfigActionRequestSchema(Schema):
    """
    Action part in a single item of the code request.
    """
    cmd = fields.String(required=True,
                        description='Command.')
    args = fields.List(fields.String(description='Single command argument.', example='-al'),
                       description='Command arguments.')


class ConfigParameterRequestSchema(Schema):
    """
    Parameter part in a single item of the code request.
    """
    destination = fields.String(required=True, description='Destination filename.', example='filebeat.yml')
    name = fields.String(required=True, description='Parameter name.', example='period')
    sep = fields.String(required=True, description='Separator between name and value.', example='=')
    value = fields.String(required=True, description='Parameter new value.', example='10s')


class ConfigResourceRequestSchema(Schema):
    """
    Resource part in a single item of the code request.
    """
    destination = fields.String(required=True, description='Destination filename', example='filebeat.yml')
    content = fields.String(required=True, description='Resource content.')


class ConfigRequestSchema(Schema):
    """
    Request for config endpoint.
    """
    actions = fields.List(fields.Nested(ConfigActionRequestSchema()), description='List of actions.')
    parameters = fields.List(fields.Nested(ConfigParameterRequestSchema()), description='List of parameters.')
    resources = fields.List(fields.Nested(ConfigResourceRequestSchema()), description='List of resources.')


class ConfigResultResponseSchema(Schema):
    """
    Single item of the config response.
    """
    type = fields.String(required=True, description='Configuration type.')
    warning = fields.String(description='Warning message', example='Useless property: id')

class ConfigErrorResponseSchema(ConfigResultResponseSchema):
    """
    Error related to a single item of config response.
    """
    error = fields.Boolean(required=True, enum=[True], description='Indicate the presence of an error.', example=True)
    description = fields.String(required=True, description='Human readable message that describes the error.',
                                example='Request type unknown')


class ConfigActionResponseSchema(ConfigResultResponseSchema):
    """
    Action part in a single item of the config response.
    """
    execute = fields.String(required=True, description='Command executed.', example='ls -al')
    stdout = fields.String(description='Standard output of the execution.')
    stderr = fields.String(description='Standard error output of the execution.')
    return_code = fields.Integer(data_key='return-code', required=True,
                                 description='Exit code of the execution (0: no error).', example=0)


class ConfigParameterResponseSchema(ConfigResultResponseSchema):
    """
    Parameter part in a single item of the config response.
    """
    destination = fields.String(required=True, description='Destination filename.', example='filebeat.yml')
    name = fields.String(required=True, description='Parameter name', example='period')
    value = fields.String(required=True, description='Parameter new value', example='10s')


class ConfigResourceResponseSchema(ConfigResultResponseSchema):
    """
    Resource part in a single item of the config response.
    """
    destination = fields.String(required=True, description='Destination filename', example='filebeat.yml')


class ConfigResponseSchema(Schema):
    """
    Response for config endpoint.
    TODO one of results of above schemes
    """
    when = fields.DateTime(required=True, description='Datetime of the configuration changes', example='2020/02/13-15:27:06')
    results = fields.List(fields.Nested(ConfigResultResponseSchema()), required=True)
