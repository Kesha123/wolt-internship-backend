import tornado
from tornado_swagger.setup import setup_swagger

from config.logger import logger
from handlers.helath import Health


PORT = 8080

class Application(tornado.web.Application):
    _routes = [
        tornado.web.url(r"/api/health_", Health, name="health"),
    ]

    def log_request(self, handler: tornado.web.RequestHandler) -> None:
        logger.info(f"{handler.get_status()}; {handler._request_summary()};")

    def __init__(self, **kwargs):
        setup_swagger(
            self._routes,
            swagger_url="/api/doc",
            api_base_url="/api",
            description="",
            api_version="1.0.0",
            title="Delivery Fee Calculator Backend",
            contact="innokentiikozlov@gmail.com",
            schemes=["https"],
        )
        super(Application, self).__init__(self._routes, debug=True, **kwargs)


class Server:
    def __init__(self, PORT: int, **kwargs) -> None:
        self.app = Application()
        self.app.listen(PORT)
        self.port = PORT

    def get_app(self) -> Application:
        return self.app

    def run(self) -> None:
        print("==============================")
        print(f"Server is running on port {self.port}")
        print("==============================")
        tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    server = Server(PORT=PORT)
    server.run()