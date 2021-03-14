# Copyright (C) 2020 Claudio Marques - All Rights Reserved
from lib.tldtool import getTldFromUrl
from utils import Constants


def existsInAlexaDb(domain):
    tld = getTldFromUrl(domain)
    tldSplitted = tld.split(".")[0]
    domain = domain.split(".")[domain.split(".").index(tldSplitted) - 1] + "." + tld
    with open(Constants.alexaDbPath) as f:
        if domain in f.read():
            return 1
    return 0

