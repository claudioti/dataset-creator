# Copyright (C) 2020 Claudio Marques - All Rights Reserved
import logging
import sys

import numpy as np
from threading import Thread

from utils import Constants
from utils.DataTools.InformationGathering import getDataFromRow

def process(items_chunk, next_chunk_index):
    logging.basicConfig(level=logging.INFO, filename=Constants.log_path, filemode="a+",
                        format="%(asctime)-15s %(levelname)-8s %(message)s")
    counter = int(next_chunk_index)
    arrayResponse = []
    for index, row in items_chunk.iterrows():
        try:
            counter, responseData = getDataFromRow(row, counter)
            arrayResponse.append(responseData)
        except Exception as e:
            print(str(row['Domain']) + ' - error with chunk item' + str(e))
            logging.error(str(row['Domain']) + ' - error with chunk item' + str(e))

    return arrayResponse


def multiThreads(array, threads, file_out):
    array_chunk = np.array_split(array, threads)
    thread_list = []
    result = []
    for thr in range(threads):
        nextIndex = 1
        if thr > 0:
            nextIndex = ((len(array) / threads) * thr) + 1
        thread = ThreadWithReturn(target=process, args=(array_chunk[thr], nextIndex))
        thread.start()
        thread_list.append(thread)

    for thread in thread_list:
        for itemThread in thread.join():
            result.append(itemThread)
            file_out.write(
                Constants.headerRegex %
                (itemThread[0], itemThread[1], itemThread[2],
                 itemThread[3], itemThread[4], itemThread[5], itemThread[6],
                 itemThread[7], itemThread[8], itemThread[9],
                 itemThread[10], itemThread[11], itemThread[12], itemThread[13],
                 itemThread[14], itemThread[15], itemThread[16], itemThread[17],
                 itemThread[18], itemThread[19], itemThread[20], itemThread[21],
                 itemThread[22], itemThread[23], itemThread[24], itemThread[25],
                 itemThread[26], itemThread[27], itemThread[28], itemThread[29],
                 itemThread[30], itemThread[31], itemThread[32]))

    return result


if sys.version_info >= (3, 0):
    _thread_target_key = '_target'
    _thread_args_key = '_args'
    _thread_kwargs_key = '_kwargs'
else:
    _thread_target_key = '_Thread__target'
    _thread_args_key = '_Thread__args'
    _thread_kwargs_key = '_Thread__kwargs'


class ThreadWithReturn(Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._return = None

    def run(self):
        target = getattr(self, _thread_target_key)
        if not target is None:
            self._return = target(
                *getattr(self, _thread_args_key),
                **getattr(self, _thread_kwargs_key)
            )

    def join(self, *args, **kwargs):
        super().join(*args, **kwargs)
        return self._return
