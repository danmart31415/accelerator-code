import concurrent.futures
import multiprocessing
import serial
import time
import matplotlib.pyplot as plt
import csv
import pandas as pd
import os
from datetime import datetime
import numpy as np

def makePlots(folder1, masterFile1):
    print('make plots')
    path = r"C:\Users\danie\Desktop\Arduino_Python_v2"
    os.chdir(os.path.join(path, folder1))
    PlotName = "plot.png"
    AccDataAnalysis = pd.read_csv(masterFile1)
    plt.plot(AccDataAnalysis.time,AccDataAnalysis.PhotoValue)
    plt.ylim(0,1123)
    plt.xlabel("Time")
    plt.ylabel("Phototransistor Reading")
    plt.savefig(PlotName)


def find_zeros(folder2, masterFile2):
    print('find zeros')
    path = r'C:\Users\danie\Desktop\Arduino_Python_v2'
    os.chdir(os.path.join(path, folder2))
    masterFile2 = os.path.join(path, folder2, masterFile2)
    CrossTimesName = "Crosstimes.csv"
    with open(masterFile2, "r") as data:
        with open(CrossTimesName, "w") as crosstimes:
            for line in data:
                PhotoList = line.strip().split(',')
                if PhotoList[0] in ['PhotoValue', '']:
                    pass
                elif float(PhotoList[0]) <=40:
                    # print('Hello, Maria!!!')
                    for i in PhotoList:
                        float(i)
                    csv.writer(crosstimes, delimiter = ',').writerow(PhotoList)

# def multiprocess(folders, files):
#     # with concurrent.futures.ProcessPoolExecutor() as executor:
#     #     result1 = executor.submit(functions.makePlots, folders, files)
#     #     result2 = executor.submit(functions.find_zeros, folders, files)
#     start = time.perf_counter()
#     processes = []
#     p = multiprocessing.Process(target = makePlots, args = (folders, files))
#     p2 = multiprocessing.Process(target = find_zeros, args = (folders, files))
#     processes.append(p)
#     processes.append(p2)
#     for process in processes:
#         process.start()
#         process.join(timeout = 1)
#     finish = time.perf_counter()
#     print(f'finished in {finish-start}')
