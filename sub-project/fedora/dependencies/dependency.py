from cmath import log
import requests
import logging

# FIXME: hardcoded, what a shame!
LOG_FILE = "/home/jacare/log/dependency.log"

logging.basicConfig(filemode='a', level=logging.DEBUG)

handler = logging.FileHandler(LOG_FILE)
handler.setFormatter(
    logging.Formatter(
        '%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s')
)

logger = logging.getLogger("dependency_log")
logger.addHandler(handler)


def my_ip():
    logger.info("requesting my current ip to httpbin...")
    return requests.get("http://httpbin.org/ip").text


if __name__ == "__main__":
    print("[dependency says] my ip is: " + my_ip())
