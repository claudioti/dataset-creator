# Copyright (C) 2020 Claudio Marques - All Rights Reserved
import logging

from utils import Constants

logging.basicConfig(level=logging.INFO, filename=Constants.log_path, filemode="a+",
                    format="%(asctime)-15s %(levelname)-8s %(message)s")

def ratioCalculator(domain, list):
    try:
        return len([char for char in domain if char in list]) / len(domain)
    except Exception as e:
        logging.error("Error in ratioCalculator(): " + str(e))
        return 0


def sequenceCalculator(domain, list):
    try:
        return max(map(len, ''.join(i if i in list else ' ' for i in domain).split()))
    except Exception as e:
        logging.error("Error in sequenceCalculator(): " + str(e))
        return 0
