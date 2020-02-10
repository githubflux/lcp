from datetime import datetime
import falcon
from marshmallow import fields, Schema
import subprocess


class CodeResource(object):
    request_schema = CodeRequestSchema()
    response_schema = CodeResponseSchema()

    def on_post(self, req, resp):
        res = {
            'when': datetime.now().strftime("%Y/%m/%d-%H:%M:%S"),
            'cmds': [],
            'return-code': 0
        }
        code = req.context['json']
        for cmd in code['cmds']:
            process = subprocess.run(cmd['prog'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
            res['cmds'].append({
                'when': datetime.now().strftime("%Y/%m/%d-%H:%M:%S"),
                'cmd': cmd['prog'],
                'args': cmd['args'],
                'stdout': process.stdout,
                'stderr': process.stderr,
                'return-code': process.returncode
            })
            res['return-code'] = res['return-code'] | process.returncode
        req.context['result'] = res
