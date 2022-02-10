from cmath import log
import requests
import logging

# FIXME: hardcoded, what a shame!
LOG_FILE = "/home/jacare/log/dependency.log"

logging.basicConfig(filename=LOG_FILE,
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

logger = logging.getLogger('dependency_log')
logger.info("loading the dependency...")


def my_ip():
    logger.info("requesting my current ip to httpbin...")
    return requests.get("http://httpbin.org/ip").text


if __name__ == "__main__":
    print("[dependency says] my ip is: " + my_ip())
