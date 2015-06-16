import tornado.web
import tornado.gen
import tornado.options
import tornado.ioloop
import tornado.httpserver
from tornado.options import options, define
from app.helpers import session

define('port', type=int, default=8618, help='run on given port')
define("mongo_host", default="127.0.0.1:27017", help="database host")

from app.handlers.routings import handlers
from app.config.settings import settings


global settings

class Application(tornado.web.Application):
    def __init__(self):
        self.session_manager = session.TornadoSessionManager(settings["session_secret"], settings["session_dir"])
        tornado.web.Application.__init__(self, handlers, **settings)


def main():
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    print ('http server listen on ', options.port)
    main()
