# Copyright (C) 2020 Claudio Marques - All Rights Reserved
import logging

from lib.alexadb import existsInAlexaDb
from lib.dns import getMXDnsResponse, getTXTDnsResponse, getSPFInfo, getTXTDnsDmarcResponse, getDmarc, getDkim
from lib.entropy import entropyCalc, getSubdomainsEntropy
from lib.enumerations import Lists
from lib.online import getCommonPorts, getHttpResponseCode, getCommonPortsMultiThread
from lib.iptools import getIp, getIpReputation, getDomainReputation
from lib.ratio import ratioCalculator, sequenceCalculator
from lib.sublist3rUtil import getSubdomains
from lib.utils import getStrangeCharacters
from lib.whois import whois, getLastUpdateAndCreationDate, getRegisteredOrg, getRegisteredCountry
from lib.geoTools import *
from lib.tldtool import *
import threading

from utils import Constants

features = threading.local()
logging.basicConfig(level=logging.INFO, filename=Constants.log_path, filemode="a+",
                    format="%(asctime)-15s %(levelname)-8s %(message)s")


def getDataFromRow(row, counter):
    print("Processing the domain: " + str(row['Domain']))
    print("\nCounter: " + str(counter))
    logging.info("Processing the domain: " + str(row['Domain']))
    logging.info("Counter: " + str(counter))

    id = counter

    features.domain = row['Domain']
    features.ip = getIp(features.domain)
    features.MXDnsResponse = getMXDnsResponse(features.domain)
    txtDnsReponse = getTXTDnsResponse(features.domain)
    dmarcResponse = getTXTDnsDmarcResponse(features.domain)
    features.TXTDnsResponse = 1 if txtDnsReponse is not None else 0
    features.hasSPFInfo = getSPFInfo(txtDnsReponse)
    features.hasDkimInfo = getDkim(txtDnsReponse)
    features.hasDmarcInfo = getDmarc(dmarcResponse)
    features.domainInAlexaDB = existsInAlexaDb(features.domain)
    features.commonPorts = getCommonPortsMultiThread(features.domain)

    features.httpResponseCode = getHttpResponseCode(features.domain)

    subdomains = getSubdomains(features.domain)
    features.subdomainNumber = len(subdomains) if subdomains is not None else 0

    features.entropy = entropyCalc(features.domain, False)
    features.entropyOfSubDomains = getSubdomainsEntropy(subdomains, features.domain)
    features.strangeCharacters = getStrangeCharacters(features.domain)
    features.TLD = getTldFromUrl(features.domain)

    features.domainReputation = 1 if getDomainReputation(features.domain) else 0
    features.consoantRatio = ratioCalculator(features.domain, Lists.CONSOANT.value)
    features.numericRatio = ratioCalculator(features.domain, Lists.NUMERIC.value)
    features.specialCharRatio = ratioCalculator(features.domain, Lists.SPECIALCHAR.value)
    features.vowelRatio = ratioCalculator(features.domain, Lists.VOWEL.value)
    features.consoantSequence = sequenceCalculator(features.domain, Lists.CONSOANT.value)
    features.vowelSequence = sequenceCalculator(features.domain, Lists.VOWEL.value)
    features.numericSequence = sequenceCalculator(features.domain, Lists.NUMERIC.value)
    features.specialCharSequence = sequenceCalculator(features.domain, Lists.SPECIALCHAR.value)

    features.domainLength = len(features.domain)

    features.classExample = row['Class']


    features.countryCode = getCountryIsoCode(features.ip)
    features.ASN = getAsn(features.ip)
    features.ipReputation = 1 if getIpReputation(features.ip) else 0
    whoIsData = whois(features.ip)
    features.registeredOrg = getRegisteredOrg(whoIsData)
    features.registeredCountry = getRegisteredCountry(whoIsData)
    # return days
    features.lastUpdateDate, features.creationDate = getLastUpdateAndCreationDate(whoIsData)

    return id, [features.domain, features.MXDnsResponse, features.TXTDnsResponse, features.hasSPFInfo,
                features.hasDkimInfo, features.hasDmarcInfo, features.ip, features.domainInAlexaDB,
                features.commonPorts, features.countryCode, features.registeredCountry,
                features.creationDate,
                features.lastUpdateDate, features.ASN, features.httpResponseCode,
                features.registeredOrg, features.subdomainNumber, features.entropy,
                features.entropyOfSubDomains, features.strangeCharacters, features.TLD, features.ipReputation,
                features.domainReputation, features.consoantRatio, features.numericRatio, features.specialCharRatio,
                features.vowelRatio, features.consoantSequence, features.vowelSequence, features.numericSequence,
                features.specialCharSequence, features.domainLength, features.classExample]
