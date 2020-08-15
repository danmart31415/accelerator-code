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
csvlist = ['Photo1.csv', 'Photo2.csv', 'Photo3.csv', 'Photo4.csv', 'Photo5.csv', 'Photo6.csv']
plotlist = ['Plot1.png','Plot2.png', 'Plot3.png', 'Plot4.png', 'Plot5.png', 'Plot6.png' ]
ser = serial.Serial('COM3', baudrate = 9600, timeout=1)

for i in csvlist:
    AcceleratorData_file = i
    AcceleratorData = folder + '/'+ AcceleratorData_file
    with open(AcceleratorData, 'w') as dataFile:
        data_writer = csv.writer(dataFile, delimiter=',')
        data_writer.writerow([i, 'time'])

    x = 1
    time.sleep(5)
    while x==1:
        PhotoByte = ser.readline()
        PhotoString = PhotoByte.decode().rstrip().split(',')

        if PhotoString[0] in ['done']:
            i += 1
            break

        elif PhotoString[0] in ['Photo1', 'Photo2', 'Photo3', 'Photo4', 'Photo5', 'Photo6']:
            continue
        else:
            with open(AcceleratorData, 'a') as dataFile:

                data_writer = csv.writer(dataFile, delimiter=',')
                data_writer.writerow(PhotoString)#reading up to here
            print(PhotoString)



print('finished recording')

print('Starting Analysis')
for i in plotlist:
    plotname_file = i
    plotname = folder + '/' + plotname_file
    AccDataAnalysis = pd.read_csv(AcceleratorData)
    x = csvlist[i]
    plt.plot(AccDataAnalysis.time, AccDataAnalysis.x)
    plt.savefig(plotname)
# plt.close()
print('Analysis Done')
