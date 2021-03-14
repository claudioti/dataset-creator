# Copyright (C) 2020 Claudio Marques - All Rights Reserved
import logging

from tld import get_tld

from utils import Constants

# logging.basicConfig(level=logging.INFO, filename=Constants.log_path, filemode="a+",
#                     format="%(asctime)-15s %(levelname)-8s %(message)s")


def getTldFromUrl(url):
    try:
        site_url = 'http://{}'.format(url)
        return get_tld(site_url)
    except Exception as e:
        logging.error("Error in getTldFromUrl(): " + str(e))
        print(str(e))
        return 'null'


def extractDomainWithoutTld(domain):
    return domain.replace(getTldFromUrl(domain), '')
