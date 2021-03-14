# Copyright (C) 2020 Claudio Marques - All Rights Reserved
import logging
import socket
import requests
import logging
import sys

from threading import Thread

from lib.enumerations import HttpResponseEnum
from utils import Constants

# logging.basicConfig(level=logging.INFO, filename=Constants.log_path, filemode="a+",
#                     format="%(asctime)-15s %(levelname)-8s %(message)s")


def doesServiceExist(ip, port):
    try:
        response = False
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP
        socket.setdefaulttimeout(2.0)
        result = sock.connect_ex((ip, port))
        if result == 0:
            response = True
        sock.close()
        return response
    except Exception as e:
        print("Error in doesServiceExist(): " + str(e) + " - domain: " + ip + " port: " + str(port))
        logging.error("Error in doesServiceExist(): " + str(e) + " - domain: " + ip + " port: " + str(port))
        return False


def getCommonPorts(port, domain):
    if doesServiceExist(domain, port):
        return 1
    return 0


def getHttpResponseCode(domain):
    try:
        response = requests.get("http://www." + domain, timeout=2)
        return httpResponseCodeToEnum(response.status_code)
    except Exception as e:
        logging.error("Error in getHttpResponseCode(): " + str(e))
        pass
    try:
        response = requests.get("https://www." + domain, timeout=2)
        return httpResponseCodeToEnum(response.status_code)
    except Exception as e:
        logging.error("Error in getHttpResponseCode(): " + str(e))
        pass
    return HttpResponseEnum.SemDados.value


def httpResponseCodeToEnum(code):
    if code < 200:
        return HttpResponseEnum.Codigos100.value
    if 200 <= code < 300:
        return HttpResponseEnum.Codigos200.value
    if 300 <= code < 400:
        return HttpResponseEnum.Codigos300.value
    if 400 <= code < 500:
        return HttpResponseEnum.Codigos400.value
    if code >= 500:
        return HttpResponseEnum.Codigos500.value


def getCommonPortsMultiThread(domain):
    thread_list = []
    result = 0

    for thr in Constants.ports:
        thread = ThreadWithReturn(target=getCommonPorts, args=(thr, domain))
        thread.start()
        thread_list.append(thread)

    for thread in thread_list:
        if thread.join() == 1:
            result = 1

    return result


if sys.version_info >= (3, 0):
    _thread_target_key = '_target'
    _thread_args_key = '_args'
    _thread_kwargs_key = '_kwargs'
else:
    _thread_target_key = '_Thread__target'
    _thread_args_key = '_Thread__args'
    _thread_kwargs_key = '_Thread__kwargs'


class ThreadWithReturn(Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._return = None

    def run(self):
        target = getattr(self, _thread_target_key)
        if not target is None:
            self._return = target(
                *getattr(self, _thread_args_key),
                **getattr(self, _thread_kwargs_key)
            )

    def join(self, *args, **kwargs):
        super().join(*args, **kwargs)
        return self._return
