import requests


def my_ip():
    return requests.get("http://httpbin.org/ip").text


if __name__ == "__main__":
    print("[dependency says] my ip is: " + my_ip())
