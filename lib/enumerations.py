# Copyright (C) 2020 Claudio Marques - All Rights Reserved
from enum import Enum


class Lists(Enum):
    VOWEL = 'aeiou'
    CONSOANT = "bcdfghjklmnpqrstvwxyz"
    NUMERIC = "0123456789"
    SPECIALCHAR = "!\"#|\\$%&/()=?«»´`*+ºª^~;,-_@£€{[]}'"


class DatesEnum(Enum):
    SemDados = 0
    UmMes = 1
    SeisMeses = 2
    UmAno = 3
    MaisDeUmAno = 4


class HttpResponseEnum(Enum):
    SemDados = 0
    Codigos100 = 1
    Codigos200 = 2
    Codigos300 = 3
    Codigos400 = 4
    Codigos500 = 5
