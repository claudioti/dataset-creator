# Copyright (C) 2020 Claudio Marques - All Rights Reserved
import logging

import numpy as np
from collections import Counter
from lib.tldtool import extractDomainWithoutTld
from utils import Constants

logging.basicConfig(level=logging.INFO, filename=Constants.log_path, filemode="a+",
                    format="%(asctime)-15s %(levelname)-8s %(message)s")


def entropyCalc(domain, isSubdomain):
    try:
        if not isSubdomain:
            domain = extractDomainWithoutTld(domain)
        p, lens = Counter(domain), np.float(len(domain))
        return int(-np.sum(count / lens * np.log2(count / lens) for count in p.values()))
    except Exception as e:
        logging.error("Error in entropyCalc(): " + str(e))
        return 0



def getSubdomainsEntropy(subdomains, domain):
    if subdomains is not None and len(subdomains) > 0:
        totalEntropyOfSubdomains = 0
        for subdomain in subdomains:
            subdomain = subdomain.replace(domain, '')
            totalEntropyOfSubdomains += entropyCalc(subdomain, True)
        return int(totalEntropyOfSubdomains / len(subdomains))
    else:
        return 0
