# Copyright (C) 2020 Claudio Marques - All Rights Reserved
import logging

from utils import Constants


from utils.Features import Features

features = Features
outputFileNameOpened = None
domains = []

logging.basicConfig(level=logging.INFO, filename=Constants.log_path, filemode="a+",
                    format="%(asctime)-15s %(levelname)-8s %(message)s")


def createSamples(outputFileName, inputFileName, size, skipRows, sampleClass):
    outputFileNameOpened = openOutputFile(outputFileName)
    dataframe = open(inputFileName, "r")
    idCounter = 0
    indexToReturn = 0
    if size == 0:
        return outputFileName, idCounter, indexToReturn
    lines = dataframe.readlines()[skipRows:]
    for index, line in enumerate(lines):
        line = line.split(" ")
        indexOfDomain = getIndexOf(line, "query:")
        features.domain = getDomain(line, indexOfDomain)
        indexOfDNSRecordType = getIndexOf(line, "IN")
        features.DNSRecordType = getDnsType(line, indexOfDNSRecordType)
        features.MXDnsResponse = 0
        features.TXTDnsResponse = 0
        features.hasSPFInfo = 0
        features.hasDkimInfo = 0
        features.hasDmarcInfo = 0
        features.ip = 'null'
        features.domainInAlexaDB = 0
        features.commonPorts = 0
        features.countryCode = 'null'
        features.registeredCountry = 'null'
        features.creationDate = 0
        features.lastUpdateDate = 0
        features.ASN = 0
        features.httpResponseCode = 0
        features.registeredOrg = 'null'
        features.subdomainNumber = 0
        features.entropy = 0
        features.entropyOfSubDomains = 0
        features.strangeCharacters = 0
        features.TLD = 'null'
        features.ipReputation = 0
        features.domainReputation = 0
        features.consoantRatio = 0
        features.numericRatio = 0
        features.specialCharRatio = 0
        features.vowelRatio = 0
        features.consoantSequence = 0
        features.vowelSequence = 0
        features.numericSequence = 0
        features.specialCharSequence = 0
        features.domainLength = 0
        features.classExample = sampleClass

        if features.domain != 'null' and features.domain not in domains and not features.domain.startswith("*"):
            idCounter += 1
            indexToReturn = index
            domains.append(features.domain)
            writeToFile(outputFileNameOpened)
            if idCounter == size:
                break

    outputFileNameOpened.close()
    return outputFileName, idCounter, indexToReturn


def getIndexOf(row, query):
    try:
        return row.index(query) + 1
    except Exception as e:
        logging.error("Error in getIndexOf(): " + str(e))
        return 0


def getDomain(row, indexOfDomain):
    if indexOfDomain != 0:
        return row.__getitem__(indexOfDomain)
    else:
        return 'null'


def getDnsType(row, indexOfDnsType):
    if indexOfDnsType != 0:
        return row.__getitem__(indexOfDnsType)
    else:
        return 'null'


def writeToFile(outputFileNameOpened):
    outputFileNameOpened.write(
        Constants.headerRegex %
        (features.domain, features.MXDnsResponse, features.TXTDnsResponse, features.hasSPFInfo,
         features.hasDkimInfo, features.hasDmarcInfo, features.ip, features.domainInAlexaDB,
         features.commonPorts, features.countryCode, features.registeredCountry,
         features.creationDate,
         features.lastUpdateDate, features.ASN, features.httpResponseCode,
         features.registeredOrg, features.subdomainNumber, features.entropy,
         features.entropyOfSubDomains, features.strangeCharacters, features.TLD, features.ipReputation,
         features.domainReputation, features.consoantRatio, features.numericRatio, features.specialCharRatio,
         features.vowelRatio, features.consoantSequence, features.vowelSequence, features.numericSequence,
         features.specialCharSequence, features.domainLength, features.classExample))


def openOutputFile(outputFileName):
    with open(outputFileName, 'w+') as f:
        f.write(Constants.fileHeader + "\n")
        f.close()
    return open(outputFileName, "a")
