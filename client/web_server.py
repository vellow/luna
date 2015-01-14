import logging
import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.template as template
import os
import json
from pymongo import MongoClient
from tornado.options import options, define, parse_command_line
from ..worker.mock_service.mock_service import Mock
from ..worker.http_server import MainHandler as CoreServer



define('port', type=int, default=8002)  
cwd = os.getcwd()
client = MongoClient()
db = client.luna


class MainHandler(tornado.web.RequestHandler):
    def initialize(self):
        pass

    def get(self):
        lis = list(db.app1.find({ }, {'url': 1}))
        loader = template.Loader( os.path.join(cwd, "Luna", "client", "webapp", "view"))
        self.write( loader.load('index.html').generate(lis=lis, rule="",mock_data="") )


class MockHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.mock = Mock()

    def get(self):
        pass

    def post(self):
        rule = self.get_body_argument("rule")
        data = self.mock.mock_data(rule)
        self.write(data)


class UrlDetail(tornado.web.RequestHandler):
    def initialize(self):
        pass

    def set_default_headers(self):
        self._headers['Content-Type'] = 'application/json';

    def get(self):
        try:
            url = self.get_query_argument('url')
        except Exception, e:
            url = None
        rule = list(db.app1.find({"url": url}, {'_id':0}))
        self.write(json.dumps(rule))

class addRule(tornado.web.RequestHandler):
    def initialize(self):
        pass

    def set_default_headers(self):
        self._headers['Content-Type'] = 'application/json';

    def post(self):
        try:
            url = self.get_body_argument('url')
            rule = self.get_body_argument('rule')
        except Exception, e:
            self.write({'success': False})

        db.app1.insert({"url": url, "rule": rule})
        self.write({'success': True})

class deleteRule(tornado.web.RequestHandler):
    def initialize(self):
        pass

    def set_default_headers(self):
        self._headers['Content-Type'] = 'application/json';

    def get(self):
        try:
            url = self.get_query_argument('url')
        except Exception, e:
            self.write({'success': False})

        db.app1.remove({"url": url})
        self.write({'success': True})


def main():
    settings = {
        "autoreload": True,
    }
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/url", UrlDetail),
        (r"/mock", MockHandler),
        (r"/real", CoreServer),
        (r"/add", addRule),
        (r"/delete", deleteRule),
    ], **settings)
    server = tornado.httpserver.HTTPServer(application)
    server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()



if __name__ == "__main__":
    main()
    print 'http server listen on localhost 8002 ...'