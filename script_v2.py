import serial
import time
import matplotlib.pyplot as plt
import csv
import os
from datetime import datetime
import numpy as np
import functions
import analysis

boo = True
time1 = time.perf_counter()
path = r"C:\Users\danie\Desktop\Arduino_Python_v2"
now = datetime.now()
folder = now.strftime("%m-%d-%Y_%H-%M-%S")
try:
    os.makedirs(folder)
    ser = serial.Serial('COM3', baudrate=9600 ,stopbits=2 , timeout=4)
except:
    pass
csvlist = ['Photo1.csv', 'Photo2.csv']#, "Photo3.csv", "Photo4.csv", "Photo5.csv", "Photo6.csv"]
plotlist = ['Plot1.png', 'Plot2.png']#, "Plot3.png", "Plot4.png", "Plot5.png", "Plot6.png"]
# ser = serial.Serial('COM3', baudrate=9600 ,stopbits=2 , timeout=4)
masterFile_analysis = 'masterFile.csv'
masterFile = folder + '/' + masterFile_analysis

fieldnames = ['PhotoValue','time']

datafiles = [masterFile_analysis]
processes = []

try:
    with open(masterFile, 'w') as dataFile:
        data_writer = csv.DictWriter(dataFile, fieldnames=fieldnames)
        data_writer.writeheader()
    timeElapsed = time.perf_counter() - time1
    while timeElapsed <= 32.97:
        PhotoByte = ser.readline()
        PhotoList = PhotoByte.decode('utf-8').strip().split(',')
        print(PhotoList)
        timeElapsed = time.perf_counter() - time1

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
except:
    pass
print('finished recording')

print('Starting Analysis')
start = time.perf_counter()
if __name__ == '__main__':
    functions.find_zeros(folder, masterFile_analysis)
    functions.makePlots(folder, masterFile_analysis)

finish = time.perf_counter()
print(f'Analysis Finished in {finish-start}')

#Multiprocessing that repeats entire script???\

# path = r"C:\Users\danie\Desktop\Arduino_Python_v2"
# os.chdir(os.path.join(path, folder))
# if __name__ == '__main__':
#         for file in datafiles:
#             p = multiprocessing.Process(target = functions.makePlots, args = (folder, file))
#             p2 = multiprocessing.Process(target = functions.find_zeros, args = (folder, file))
#             p.start()
#             p2.start()
#             processes.append(p)
#             processes.append(p2)
#         for process in processes:
#             process.join()
#         finish = time.perf_counter()
#         print(f'finished in {finish-start}')
