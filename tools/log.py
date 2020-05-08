import os
import logging
from logging.handlers import TimedRotatingFileHandler


class AppLog:
    @staticmethod
    def init_log(path):
        if not os.path.exists(path):
            os.makedirs(path)
        formatter = "\033[37m%(asctime)s %(filename)15s:%(lineno)-5d %(funcName)5s() %(levelname)6s\033" \
                    "[0m : %(message)s"
        logging.basicConfig(
            level=logging.DEBUG,
            format=formatter,
            datefmt='%a, %d %b %Y %H:%M:%S',
        )
        handler = TimedRotatingFileHandler(path + '/flask.log', when="d",
                                           backupCount=7)
        handler.setFormatter(logging.Formatter(formatter))
        handler.setLevel(logging.DEBUG)
        logging.getLogger('').addHandler(handler)
        logging.getLogger('sqlalchemy.engine').addHandler(handler)
