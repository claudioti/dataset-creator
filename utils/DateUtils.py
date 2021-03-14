# Copyright (C) 2020 Claudio Marques - All Rights Reserved
from datetime import datetime

import dateutil

from lib.enumerations import DatesEnum


def dateToEnum(date):
    today = datetime.today().date()
    months = (today.year - date.year) * 12 + today.month - date.month
    if months <= 1:
        return DatesEnum.UmMes.value
    if months <= 6:
        return DatesEnum.SeisMeses.value
    if months <= 12:
        return DatesEnum.UmAno.value
    if months > 12:
        return DatesEnum.MaisDeUmAno.value
    return DatesEnum.SemDados.value


