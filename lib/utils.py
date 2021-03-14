# Copyright (C) 2020 Claudio Marques - All Rights Reserved
import logging
import re

from utils import Constants

logging.basicConfig(level=logging.INFO, filename=Constants.log_path, filemode="a+",
                    format="%(asctime)-15s %(levelname)-8s %(message)s")


def getStrangeCharacters(domain):
    try:
        domain = re.sub(r'[a-zA-Z\.]+', '', domain)
        if len(domain) > 0:
            digits = sum(char.isdigit() for char in domain)
            digits = 0 if digits <= 2 else digits - 2
            domain = re.sub(r'[0-9]+', '', domain)
            return len(domain) + digits
        return 0
    except Exception as e:
        logging.error("Error on getStrangeCharacters(): " + str(e))
        return 0
