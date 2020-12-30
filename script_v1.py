import multiprocessing
import serial
import time
import matplotlib.pyplot as plt
import csv
import pandas as pd
import os
from datetime import datetime
now = datetime.now()
folder = now.strftime("%m-%d-%Y_%H-%M-%S")
os.makedirs(folder)
csvlist = ['Photo1.csv', 'Photo2.csv']#, "Photo3.csv", "Photo4.csv", "Photo5.csv", "Photo6.csv"]
plotlist = ['Plot1.png', 'Plot2.png']#, "Plot3.png", "Plot4.png", "Plot5.png", "Plot6.png"]
ser = serial.Serial('COM3', baudrate=9600 ,stopbits=2 , timeout=4)
masterFile = folder + '/' + 'masterFile.csv'

fieldnames = ['PhotoValue','time']



datafiles = [masterFile]
processes = []
def makePlots(folder1, masterFile1):
    now = datetime.now()
    PlotName = "plot_" + now.strftime("%m-%d-%Y_%H-%M-%S") + ".png"
    FinalPlotName = folder1 + '/' + PlotName
    master_file1 = folder1 + "/" + masterFile1
    AccDataAnalysis = pd.read_csv(master_file1)
    plt.plot(AccDataAnalysis.time,AccDataAnalysis.PhotoValue)
    plt.ylim(0,2023)
    plt.savefig(FinalPlotName)

def find_zeros(folder2, masterFile2):
    now = datetime.now()
    CrossTimesName = "Crosstimes_" + now.strftime("%m-%d-%Y_%H-%M-%S") + ".csv"
    CrossTimes = folder2 + '/' + CrossTimesName
    master_file2 = folder2 + "/" + masterFile2
    with open(master_file2, "r") as data:
        with open(CrossTimes, "w") as crosstimes:
            for line in data:
                PhotoList = line.strip().split(',')
                if PhotoList[0] in ['PhotoValue', '']:
                    pass
                elif PhotoList[0] in ["0"]:
                    for i in PhotoList:
                        float(i)
                    csv.writer(crosstimes, delimiter = ',').writerow(PhotoList)


with open(masterFile, 'w') as dataFile:
    data_writer = csv.DictWriter(dataFile, fieldnames=fieldnames)
    data_writer.writeheader()
while timeElapsed<=31.97:
    PhotoByte = ser.readline()
    PhotoList = PhotoByte.decode('utf-8').strip().split(',')
    print(PhotoList)

x = 1
while x==1:
    PhotoByte = ser.readline()
    PhotoList = PhotoByte.decode('utf-8').strip().split(',')
    if PhotoList[0] in ['done']:
        break
# VERY IMPORTANT: This is what makes the whole thing work. It changes each number (photovalue and time) into floats
    for i in PhotoList:
        float(i)
    with open(masterFile, 'a') as dataFile:
        data_writer = csv.writer(dataFile, delimiter=',')
        data_writer.writerow(PhotoList)#reading up to here
    print(PhotoList)
print('finished recording')

print('Starting Analysis')

start = time.perf_counter()

if __name__ == '__main__':
        for file in datafiles:
            p = multiprocessing.Process(target = makePlots, args = [folder, file])
            p2 = multiprocessing.Process(target = find_zeros, args = [folder, file])
            p.start()
            p2.start()
            processes.append(p)
            processes.append(p2)
        for process in processes:
            process.join()

        finish = time.perf_counter()
        print(f'finished in {finish-start}')

print('Analysis Done')
