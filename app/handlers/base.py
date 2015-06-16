__author__ = 'YellowGlue'

import tornado.web
import tornado.escape
from tornado import gen
from app.helpers import session
import json
from tornado.web import traceback
from bson import json_util

class BaseHandler(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        tornado.web.RequestHandler.__init__(self, application, request, **kwargs)
        self.session = session.TornadoSession(application.session_manager, self)


class PageHandler(BaseHandler):
    def __init__(self, application, request, **kwargs):
        BaseHandler.__init__(self, application, request, **kwargs)

    def _write_error(self, status_code, **kwargs):

        if self.settings.get("serve_traceback") and "exc_info" in kwargs:
            # in debug mode, try to send a traceback
            self.set_header('Content-Type', 'text/plain')
            for line in traceback.format_exception(*kwargs["exc_info"]):
                self.write(line)
            self.finish()
        else:
            if 404 == status_code:
                self.render('404.html')
            else:
                self.finish("<html><title>%(code)d: %(message)s</title>"
                            "<body>%(code)d: %(message)s</body></html>" % {
                                "code": status_code,
                                "message": self._reason,
                            })

    def _render_string(self, template_name, **kwargs):

        return self.render_string(template_name,
                                  title=self.settings['app_name'],
                                  static_path=self.settings['static_path'],
                                  **kwargs
                                  )

    def _render(self, template_name, **kwargs):
        self.finish(self._render_string(template_name, **kwargs))


class XHRHandler(BaseHandler):
    def __init__(self, application, request, **kwargs):
        BaseHandler.__init__(self, application, request, **kwargs)


    def get_json_argument(self, name, default=None):
        data = self.get_body_argument(name)
        return json.loads(data)


    def _write_json(self, response):

        res_data = response
        if response['error'] == None:
            res_data['statusCode'] = 200

        else:
            # raise response['error']
            res_data = {
                'success': False,
                'statusCode': 500,
                'message': 'Some thing blew up',
                'data': None
            }
        self.set_header('Content-Type', 'application/json; charset=UTF-8')
        self.write(json.dumps(res_data, default=json_util.default))