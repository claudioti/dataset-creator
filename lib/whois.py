# Copyright (C) 2020 Claudio Marques - All Rights Reserved
import logging

import dateutil
from ipwhois import IPWhois

from urllib import request
from stem import Signal
from stem.control import Controller

from lib.enumerations import DatesEnum
from utils import Constants
from utils.DateUtils import dateToEnum

#logging.basicConfig(level=logging.INFO, filename=Constants.log_path, filemode="a+",
 #                   format="%(asctime)-15s %(levelname)-8s %(message)s")


def whois(ip):
    if ip is not None and ip != 'null':
        ##Using TOR Proxy
        with Controller.from_port(address='192.168.100.100', port=9051) as controller:
            controller.authenticate(password='lsirc')
            controller.signal(Signal.NEWNYM)
            controller.close()
            proxies = {"http": "http://192.168.100.100:8118"}
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit / 537.73.11(KHTML, like Gecko) Version / 7.0.1 Safari / 537.73.11'}
            try:
                handler = request.ProxyHandler(proxies)
                opener = request.build_opener(handler)
                obj = IPWhois(ip, proxy_opener=opener)
                return obj.lookup_rdap(depth=1)
            except Exception as e:
                #logging.error("Error in whois(): " + str(e))
                print("Error in whois():" + str(e))
                pass
    return None


def getLastUpdateAndCreationDate(whoIsData):
    lastUpdateDate = DatesEnum.SemDados.value
    creationDate = DatesEnum.SemDados.value
    if whoIsData is not None and whoIsData['network']['events'] and len(whoIsData['network']['events']):
        for event in whoIsData['network']['events']:
            if event['action'] == 'last changed':
                try:
                    lastUpdateDate = dateToEnum(dateutil.parser.parse(event['timestamp']).date())
                except Exception as e:
                    logging.error("Error in getLastUpdateAndCreationDate(): " + str(e))
                    pass
            if event['action'] == 'registration':
                try:
                    creationDate = dateToEnum(dateutil.parser.parse(event['timestamp']).date())
                except Exception as e:
                    logging.error("Error in getLastUpdateAndCreationDate(): " + str(e))
                    pass
    return lastUpdateDate, creationDate


def getRegisteredOrg(whoIsData):
    if whoIsData is not None and len(whoIsData['network']):
        return (whoIsData['network']['name']).replace(",", "_") if whoIsData['network']['name'] is not None else 'null'
    else:
        return 'null'


def getRegisteredCountry(whoIsData):
    if whoIsData is not None and len(whoIsData['network']):
        return whoIsData['network']['country'] if whoIsData['network']['country'] is not None else 'null'
    else:
        return 'null'
