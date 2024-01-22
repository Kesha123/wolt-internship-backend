import json
import functools
from config.logger import logger


def catch_error_request(request):
    @functools.wraps(request)
    def wrapper(*args, **kwargs):
        try:
            return request(*args, **kwargs)
        except Exception as e:
            args[0].set_status(400)
            args[0].write(json.dumps({"error": str(e)}))
            logger.error(e)

    return wrapper