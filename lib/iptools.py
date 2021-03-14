# Copyright (C) 2020 Claudio Marques - All Rights Reserved
import logging
import socket
import pydnsbl

from utils import Constants

logging.basicConfig(level=logging.INFO, filename=Constants.log_path, filemode="a+",
                    format="%(asctime)-15s %(levelname)-8s %(message)s")


def getIp(domain):
    if not domain.startswith("*"):
        try:
            socket.setdefaulttimeout(0.05)
            return socket.gethostbyname(domain)
        except:
            try:
                socket.setdefaulttimeout(0.05)
                return socket.gethostbyname("www." + domain)
            except Exception as e:
                logging.error("Exception in getIp: {}" + str(e))
                pass
            pass
    return 'null'


def getIpReputation(ip):
    ip_checker = pydnsbl.DNSBLIpChecker()
    try:
        result = ip_checker.check(ip)
        return result.blacklisted
    except Exception as e:
        print("Exception in getIpReputation: {}" + str(e))
        logging.error("Exception in getIpReputation: {}" + str(e))
        return False


def getDomainReputation(domain):
    domain_checker = pydnsbl.DNSBLDomainChecker()
    try:
        result = domain_checker.check(domain)
        return result.blacklisted
    except Exception as e:
        print("Exception in getDomainReputation: {}" + str(e))
        logging.error("Exception in getDomainReputation: {}" + str(e))
        return False

