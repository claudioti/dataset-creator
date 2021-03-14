# Copyright (C) 2020 Claudio Marques - All Rights Reserved
class Features:
    def __init__(self, domain, DNSRecordType, MXDnsResponse, TXTDnsResponse, hasSPFInfo, hasDkimInfo, hasDmarcInfo, ip,
                 domainInAlexaDB, commonPorts, countryCode, registeredCountry, creationDate, expirationDate,
                 lastUpdateDate, ASN, httpResponseCode, registeredOrg,
                 subdomainNumber, entropy, entropyOfSubDomains, strangeCharacters,
                 TLD, ipReputation, domainReputation, consoantRatio, numericRatio,
                 specialCharRatio, vowelRatio, consoantSequence, vowelSequence, numericSequence,
                 specialCharSequence, domainLength, classExample):
        self.domain = domain
        self.DNSRecordType = DNSRecordType
        self.MXDnsResponse = MXDnsResponse
        self.TXTDnsResponse = TXTDnsResponse
        self.hasSPFInfo = hasSPFInfo
        self.hasDkimInfo = hasDkimInfo
        self.hasDmarcInfo = hasDmarcInfo
        self.ip = ip
        self.domainInAlexaDB = domainInAlexaDB
        self.commonPorts = commonPorts
        self.countryCode = countryCode
        self.registeredCountry = registeredCountry
        self.creationDate = creationDate
        self.expirationDate = expirationDate
        self.lastUpdateDate = lastUpdateDate
        self.ASN = ASN
        self.httpResponseCode = httpResponseCode
        self.registeredOrg = registeredOrg
        self.subdomainNumber = subdomainNumber
        self.entropy = entropy
        self.entropyOfSubDomains = entropyOfSubDomains
        self.strangeCharacters = strangeCharacters
        self.TLD = TLD
        self.ipReputation = ipReputation
        self.domainReputation = domainReputation
        self.consoantRatio = consoantRatio
        self.numericRatio = numericRatio
        self.specialCharRatio = specialCharRatio
        self.vowelRatio = vowelRatio
        self.consoantSequence = consoantSequence
        self.vowelSequence = vowelSequence
        self.numericSequence = numericSequence
        self.specialCharSequence = specialCharSequence
        self.domainLength = domainLength
        self.classExample = classExample
