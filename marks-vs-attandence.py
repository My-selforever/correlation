import csv
import os
import numpy as np

os.system('cls')

def convert():
    f = open('Student Marks vs Days Present.csv')
    rf = csv.reader(f)

    fileList= list(rf)
    fileList.pop(0)
    dayspresent = []
    marksinpercentage = []

    for i in range(len(fileList)):
        present = float(fileList[i][1])
        dayspresent.append(present)
        marks = float(fileList[i][2])
        marksinpercentage.append(marks)

    return{
        'x':dayspresent,
        'y':marksinpercentage
    }

def correlate(dictionary):
     relate=np.corrcoef(dictionary['x'],dictionary['y'])
     print(relate[1][0])

def main():
    dictionary = convert()
    correlate(dictionary)

main()