# Copyright (C) 2020 Claudio Marques - All Rights Reserved
import logging

import geoip2.database

from utils import Constants

# logging.basicConfig(level=logging.INFO, filename=Constants.log_path, filemode="a+",
#                     format="%(asctime)-15s %(levelname)-8s %(message)s")

def getCountry(ip):
    if ip != 'null':
        try:
            reader = geoip2.database.Reader('./utils/Database/GeoLite2-Country_20200526/GeoLite2-Country.mmdb')
            return reader.country(ip)
        except Exception as e:
            logging.error("Error in getCountry(): " + str(e))
            return 'null'
    else:
        return 'null'


def getCountryIsoCode(ip):
    if ip != 'null':
        try:
            return getCountry(ip).country.iso_code
        except Exception as e:
            logging.error("Error in getCountryIsoCode(): " + str(e))
            return 'null'
    else:
        return 'null'


def getAsn(ip):
    if ip != 'null':
        reader = geoip2.database.Reader('./utils/Database/GeoLite2-ASN_20200526/GeoLite2-ASN.mmdb')
        try:
            return int(reader.asn(ip).autonomous_system_number)
        except Exception as e:
            logging.error("Error in getAsn(): " + str(e))
            return -1
    else:
        return -1
