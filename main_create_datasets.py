# Copyright (C) 2020 Claudio Marques - All Rights Reserved
from datetime import datetime

from utils.Functions import createSamples, createDatasetFile
import pandas as pd
import logging
from utils import Constants
from utils.MultiThread import multiThreads
import os
import glob


def main():
    skipRowsAAAA = 0
    skipRowsCNAME = 0
    skipRowsMX = 0
    skipRowsMalign = 0
    totalDatasets = 100

    for index in range(totalDatasets):
        print("***Starting Dataset*** " + str(index + 1))
        logging.info("***Starting Dataset*** " + str(index + 1))
        # current datetime
        print(datetime.now())
        logging.info("Start Date: " + str(datetime.now()))

        benignFileAAAA, bLastIdAAAA, lastIndexAAAA = createSamples(Constants.outputFileBenignAAA,
                                                                   Constants.inputFileBenignAAAA, Constants.sampleAAAA,
                                                                   skipRowsAAAA, 1)

        benignFileCNAME, bLastIdCNAME, lastIndexCNAME = createSamples(Constants.outputFileBenignCNAME,
                                                                      Constants.inputFileBenignCNAME,
                                                                      Constants.sampleCNAME, skipRowsCNAME,
                                                                      1)
        benignFileMX, bLastIdMX, lastIndexMX = createSamples(Constants.outputFileBenignMX, Constants.inputFileBenignMX,
                                                             Constants.sampleMX, skipRowsMX, 1)

        malignFile, mLastId, lastIndexMalign = createSamples(Constants.outputFileMalign, Constants.inputFileMalign,
                                                             Constants.sampleMalign, skipRowsMalign, 0)

        totalBening = bLastIdMX + bLastIdAAAA + bLastIdCNAME

        print("Total Malign: " + str(mLastId) + "\nTotal Benign: " + str(totalBening))
        logging.info("Total Malign: " + str(mLastId) + "\nTotal Benign: " + str(totalBening))

        print("\nLast row AAAA: " + str(lastIndexAAAA) +
              "\nLast row CNAME: " + str(lastIndexCNAME) +
              "\nLast row MX: " + str(lastIndexMX) +
              "\nLast row Malign: " + str(lastIndexMalign))

        logging.info("\nLast row AAAA: " + str(lastIndexAAAA) +
                     "\nLast row CNAME: " + str(lastIndexCNAME) +
                     "\nLast row MX: " + str(lastIndexMX) +
                     "\nLast row Malign: " + str(lastIndexMalign))

        dataFrameBenignAAAA = pd.read_csv(benignFileAAAA)
        dataFrameBenignCNAME = pd.read_csv(benignFileCNAME)
        dataFrameBenignMX = pd.read_csv(benignFileMX)
        dataFrameMalign = pd.read_csv(malignFile)

        pandaMergedData = pd.concat([dataFrameBenignAAAA, dataFrameBenignCNAME, dataFrameBenignMX, dataFrameMalign])

        file_out = createDatasetFile(index + 1)

        multiThreads(pandaMergedData, Constants.numberOfThreads, file_out)
        file_out.close()

        skipRowsAAAA = skipRowsAAAA + lastIndexAAAA
        skipRowsCNAME = skipRowsCNAME + lastIndexCNAME
        skipRowsMX = skipRowsMX + lastIndexMX
        skipRowsMalign = skipRowsMalign + lastIndexMX
        print("***Ending Dataset*** " + str(index + 1))
        logging.info("***Ending Dataset*** " + str(index + 1))
        # current datetime
        print(datetime.now())
        logging.info("Ending Date: " + str(datetime.now()))

    mergeDatasets(totalDatasets)


def mergeDatasets():
    os.chdir("/data/output")
    extension = 'csv'
    all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
    dataset_final = pd.concat([pd.read_csv(f) for f in all_filenames])
    dataset_final = dataset_final.fillna('null')
    dataset_final.to_csv('/data/output/datasetFinal.csv', index=False)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filename=Constants.log_path, filemode="a+",
                        format="%(asctime)-15s %(levelname)-8s %(message)s")
    main()
