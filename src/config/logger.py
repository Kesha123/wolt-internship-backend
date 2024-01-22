import logging
from python_logger.Logger import Logger
from python_logger.handlers import HandlerLevel, StreamHandler, FileHandler


handlers = HandlerLevel(
    stream=StreamHandler(level=logging.DEBUG),
    file=FileHandler(level=logging.INFO),
)

logger = Logger(handlers=handlers)