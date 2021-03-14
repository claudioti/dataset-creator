# Copyright (C) 2020 Claudio Marques - All Rights Reserved
from sklearn.preprocessing import LabelEncoder

from utils import Constants
from utils.DataTools.SamplesGenerator import createSamples as samplesGenerator
from utils.DataTools.InformationGathering import getDataFromRow as dataFromRow


def createSamples(outputFileName, inputFileName, size, skipRows, sampleClass):
    return samplesGenerator(outputFileName, inputFileName, size, skipRows, sampleClass)


def getDataFromRow(row, counter):
    return dataFromRow(row, counter)


def createDatasetFile(index):
    path = Constants.dataset_path.replace("{toReplace}", str(index))
    with open(path, 'w+') as f:
        f.write(Constants.fileHeader + "\n")
        f.close()
    return open(path, "a", encoding="utf-8")