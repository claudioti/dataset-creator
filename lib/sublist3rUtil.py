# Copyright (C) 2020 Claudio Marques - All Rights Reserved
import logging

import sublist3r

from lib.tldtool import getTldFromUrl
from utils import Constants

# logging.basicConfig(level=logging.INFO, filename=Constants.log_path, filemode="a+",
#                     format="%(asctime)-15s %(levelname)-8s %(message)s")


def getSubdomains(domain):
    try:
        tld = getTldFromUrl(domain)
        tldSplitted = tld.split(".")[0]
        domain = domain.split(".")[domain.split(".").index(tldSplitted) - 1] + "." + tld
        return sublist3r.main(domain, 5, savefile=None, ports=None, silent=False, verbose=False,
                              enable_bruteforce=False, engines=Constants.sublist3rEngines)
    except Exception as e:
        logging.error("Error in getSubdomains(): " + str(e))
        pass
    return None
