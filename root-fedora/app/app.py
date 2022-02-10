import logging
from dependency import my_ip

# FIXME: hardcoded, what a shame!
LOG_FILE = "/home/jacare/log/app.log"

logging.basicConfig(filemode='a', level=logging.DEBUG)

handler = logging.FileHandler(LOG_FILE)
handler.setFormatter(
    logging.Formatter(
        '%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s')
)

logger = logging.getLogger("app_log")
logger.addHandler(handler)


if __name__ == "__main__":
    logger.info("running the app...")
    print("[app says] my ip is: " + my_ip())
