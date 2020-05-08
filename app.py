
import logging
from controller import app

if __name__ == '__main__':
    logging.info("app is starting ......")
    app.run(port=5000)
