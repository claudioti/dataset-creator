# Copyright (C) 2020 Claudio Marques - All Rights Reserved
import logging

import dns.resolver
import pydig

from utils import Constants

dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers = ['8.8.8.8', '8.8.4.4']
dns.resolver.timeout = 5


# logging.basicConfig(level=logging.INFO, filename=Constants.log_path, filemode="a+",
#                   format="%(asctime)-15s %(levelname)-8s %(message)s")


def getDnsResponse(url):
    try:
        dns.resolver.query(url)
        return 1
    except Exception as e:
        logging.error("Error on getDnsResponse(): " + str(e))
        pass
    return 0


def getMXDnsResponse(url):
    try:
        dns.resolver.query(url, "MX")
        return 1
    except Exception as e:
        logging.error("Error on getMXDnsResponse(): " + str(e))
        pass
    return 0


def getTXTDnsResponse(url):
    try:
        return dns.resolver.query(url, "TXT")
    except Exception as e:
        logging.error("Error on getTXTDnsResponse(): " + str(e))
        pass
    return None


def getTXTDnsDmarcResponse(url):
    try:
        return dns.resolver.query("_dmarc." + url, "TXT")
    except Exception as e:
        logging.error("Error on getTXTDnsDmarcResponse(): " + str(e))
        pass
    return None


def getSPFInfo(txtDnsResponse):
    if txtDnsResponse is not None:
        for item in txtDnsResponse.rrset.items:
            if "v=spf".lower() in str(item).lower():
                return 1
    return 0


def getDkim(txtDnsReponse):
    if txtDnsReponse is not None:
        for item in txtDnsReponse.rrset.items:
            if "v=dkim".lower() in str(item).lower():
                return 1
    return 0


def getDmarc(dmarcResponse):
    if dmarcResponse is not None:
        for item in dmarcResponse.rrset.items:
            if "v=dmarc".lower() in str(item).lower():
                return 1
    return 0
