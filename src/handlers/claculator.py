import json
import tornado
from dacite import from_dict
from tornado_swagger.model import register_swagger_model

from config.logger import logger
from utils.request import catch_error_request
from api_types.calculator import DeliveryFeeRequest


class Calculator(tornado.web.RequestHandler):

    def initialize(self) -> None:
        self.logger = logger

    def prepare(self) -> None:
        request_body_data = json.loads(self.request.body)
        self.delivery_fee_data = from_dict(data_class=DeliveryFeeRequest, data=request_body_data)

    @catch_error_request
    def post(self) -> None:
        """
        Description end-point

        ---
        tags:
        - Calculator
        summary: Delivery Fee Calculator
        produces:
        - application/json
        parameters:
        - in: body
          name: body
          description: Calculate Delivery Fee
          required: true
          schema:
            $ref: '#/definitions/PostCalculatorRequest'
        responses:
            200:
                description: Ok
                schema:
                  $ref: '#/definitions/PostCalculatorResponse'
            400:
                description: Bad request
        """
        self.write(json.dumps({}))


@register_swagger_model
class PostCalculatorRequest:
    """
    ---
    type: object
    properties:
        cart_value:
            type: integer
            format: int64
        delivery_distance:
            type: integer
            format: int64
        number_of_items:
            type: integer
            format: int64
        time:
            type: string
    """

@register_swagger_model
class PostCalculatorResponse:
    """
    ---
    type: object
    properties:
        delivery_fee:
            type: integer
            format: int64
    """