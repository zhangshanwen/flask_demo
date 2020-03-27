import os

from tools.log import logger

from controller import app

if __name__ == '__main__':
    logger.info("app is starting ......")
    app.run(port=5000)
