# Copyright (C) 2020 Claudio Marques - All Rights Reserved
dataset_path = "data/output/dataset{toReplace}.csv"
dataset_path_final = "data/output/final/datasetFinal.csv"
log_path = "data/logs/output_append.log"
numberOfThreads = 45

inputFileMalign = "data/input/malign/all.log"
outputFileMalign = "data/output/fileMalign.csv"
sampleMalign = 300

inputFileBenignAAAA = "data/input/benign/aaaa/all.log"
outputFileBenignAAA = "data/output/fileBenignAAAA.csv"
sampleAAAA = 100

inputFileBenignCNAME = "data/input/benign/cname/all.log"
outputFileBenignCNAME = "data/output/fileBenignCNAME.csv"
sampleCNAME = 100

inputFileBenignMX = "data/input/benign/mx/all.log"
outputFileBenignMX = "data/output/fileBenignMX.csv"
sampleMX = 100

alexaDbPath = "utils/Database/AlexaDB/top-1m.csv"

ports = [80, 443, 21, 22, 23, 25, 53, 110, 143, 161, 445, 465, 587, 993, 995, 3306, 3389, 7547, 8080, 8888]

fileHeader = "Domain,DNSRecordType,MXDnsResponse,TXTDnsResponse,HasSPFInfo,HasDkimInfo,HasDmarcInfo,Ip,DomainInAlexaDB,CommonPorts,CountryCode,RegisteredCountry,CreationDate," \
             "LastUpdateDate,ASN,HttpResponseCode,RegisteredOrg,SubdomainNumber,Entropy,EntropyOfSubDomains,StrangeCharacters," \
             "TLD,IpReputation,DomainReputation," \
             "ConsoantRatio,NumericRatio,SpecialCharRatio,VowelRatio,ConsoantSequence,VowelSequence,NumericSequence,SpecialCharSequence,DomainLength,Class"

headerRegex = "%s,%s,%d,%d,%d,%d,%d,%s,%d,%d,%s,%s,%d," \
              "%d,%d,%d,%s,%d,%d,%d,%d," \
              "%s,%d,%d," \
              "%0.1f,%0.1f,%0.1f,%0.1f,%d,%d,%d,%d,%d,%d\n"

sublist3rEngines = "bing,passivedns"
