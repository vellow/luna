import logging
from auth_service.cas.auth import Login
from data_service.api_service import Data
from mock_service.mock_service import Mock


import tornado.ioloop
import tornado.web

import uuid


authCache = {}

class MainHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.login = Login()
        self.data = Data()
        self.mock = Mock()

    def get(self):
        try:
            user = self.get_query_argument('user')
        except Exception, e:
            user = None

        url = self.get_query_argument('service')
        isMock = self.get_query_argument('isMock')
        miduuid = self.get_cookie('MIDUUID')
        auth = authCache.get(miduuid)

        if miduuid==None or auth==None or user:
            auth = self.login.login_cas_itebeta(user, url)

            miduuid = str(uuid.uuid1())
            authCache[miduuid] = auth



            if isMock == 'true':

                data = self.mock.mock_data()
                self.set_cookie('MIDUUID',miduuid)
                self.write(data)
            else:
                data = self.data.get_data(url, auth)
                self.set_cookie('MIDUUID',miduuid)
                self.write(data)

        else:

            auth = authCache[miduuid]

            if isMock == 'true':
                data = self.mock.mock_data()
                self.write(data)
            else:
                data = self.data.get_data(url, auth)
                self.write(data)

settings = {
    "autoreload": True,
}

application = tornado.web.Application([
    (r"/", MainHandler),
], **settings)


if __name__ == "__main__":
    application.listen(8001)
    print 'http server listen on localhost'
    tornado.ioloop.IOLoop.instance().start()