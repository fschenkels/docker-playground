import logging
from dependency import my_ip

# FIXME: hardcoded, what a shame!
LOG_FILE = "/home/jacare/log/app.log"

logging.basicConfig(filename=LOG_FILE,
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

logger = logging.getLogger('app_log')


if __name__ == "__main__":
    logger.info("running the app...")
    print("[app says] my ip is: " + my_ip())
