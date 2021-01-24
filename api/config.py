import logging
import os

DEV_ENV = "dev"
DEV_HOST = os.getenv("DEV_HOST", "127.0.0.1")
DEV_PORT = int(os.getenv("DEV_PORT", "5000"))


def setup_logging():
    """Set up logging configurations"""
    logging.basicConfig(
        filename=os.getenv("SERVICE_LOG", "server.log"),
        level=logging.DEBUG,
        format="%(levelname)s: %(asctime)s pid:%(process)s module:%(module)s %(message)s",
        datefmt="%d/%m/%y %H:%M:%S",
    )
