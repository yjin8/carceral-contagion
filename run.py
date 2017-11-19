# ..................................................................
# : Carceral Contagion: An Agent-Based Model of Mass Incarceration :
# : Yuchen Jin, Adam Rahman | WHACK 2017                           :
# : carceral-contagion/run.py                                      :
# : -- Launches a model visualization server.                      :
# :................................................................:

import os
import tornado.autoreload
import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.escape
import tornado.gen
import webbrowser
import tornado.httpserver

from server import server
#server.launch()

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello world")

def main():
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    port = int(os.environ.get("PORT", 5000))
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()
 
if __name__ == "__main__":
    main()