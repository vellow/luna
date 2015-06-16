# errors

from tornado.web import RequestHandler, ErrorHandler, HTTPError
from tornado.web import traceback
from app.handlers.base import *


def write_error(self, status_code, **kwargs):
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

setattr(RequestHandler, 'write_error', write_error)



def duplicateError():

    return {
        'success': False,
        'err': HTTPError(500, log_message='Duplicate Key')
    }

def notFound():
    HTTPError(404, 'Page Not Found')

def internalError():
    return {
        'success': False,
        'err': HTTPError(500, log_message='Internal Server Error')
    }