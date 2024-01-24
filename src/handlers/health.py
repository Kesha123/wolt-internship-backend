import json
import tornado
from tornado_swagger.model import register_swagger_model

from config.logger import logger


class Health(tornado.web.RequestHandler):

    def initialize(self) -> None:
        self.logger = logger

    def get(self) -> None:
        """
        Description end-point

        ---
        tags:
        - Health Check
        summary: Check API
        produces:
        - application/json
        responses:
            200:
                description: Ok
                schema:
                  $ref: '#/definitions/GetHealth'
            400:
                description: Bad request
        """
        self.write(json.dumps({"status": "ok"}))


@register_swagger_model
class GetHealth:
    """
    ---
    type: object
    properties:
        status:
            type: string
            example: "ok"
    """