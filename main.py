# ..................................................................
# : Carceral Contagion: An Agent-Based Model of Mass Incarceration :
# : Yuchen Jin, Adam Rahman | WHACK 2017                           :
# : carceral-contagion/run.py                                      :
# :................................................................:
import os
import tornado.httpserver
import tornado.ioloop
import tornado.web
from servertest import server
# server.port = 8521
# server.launch()

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
    server.launch()
 
if __name__ == "__main__":
    main()