import logging
from auth_service.cas.auth import Login
from data_service.api_service import Data

import tornado.ioloop
import tornado.web

import uuid


authCache = {}

class MainHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.login = Login()
        self.data = Data()

    def get(self):
        try:
            user = self.get_query_argument('user')
        except Exception, e:
            user = None

        
        url = self.get_query_argument('service')
        miduuid = self.get_cookie('MIDUUID')
        auth = authCache.get(miduuid)


        if miduuid==None or auth==None or user:
            auth = self.login.login_cas_itebeta(user)
            miduuid = str(uuid.uuid1())
            authCache[miduuid] = auth
            data = self.data.get_data(url, auth)
            self.set_cookie('MIDUUID',miduuid)
            self.write(data)

        else:
            auth = authCache[miduuid]
            data = self.data.get_data(url, auth)
            self.write(data)

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8001)
    print 'http server listen on localhost:8001...'
    tornado.ioloop.IOLoop.instance().start()