from typing import Optional, Awaitable

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
import textwrap


define("port", default=8888, help="run on the given port", type=int)


class Reversehandler(tornado.web.RequestHandler):
    def get(self, input):
        self.write(input[::-1] + '\n')


class WrapHandler(tornado.web.RequestHandler):
    def post(self):
        text = self.get_argument('text')
        width = self.get_argument('width', 40)
        self.write(textwrap.fill(text, int(width)) + '\n')


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting', 'Hello')
        self.write(greeting + ', friendly user!')


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world!\n")

    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting', 'Hello')
        self.write(greeting + ', friendly user!')

    def write_error(self, status_code: int, **kwargs):
        self.write("Gosh darnit, user! You caused a {0} error.\n".format(status_code))


application = tornado.web.Application([(r"/", MainHandler)])

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[
        (r"/", IndexHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
