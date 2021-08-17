import logging
from app import app
import libs

if __name__ == '__main__':
    logging.info("app is starting ......")
    app.run(port=app.config.get("PORT"))
