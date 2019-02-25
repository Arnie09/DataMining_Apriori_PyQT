import pandas as pd
import os
import sys

def minimum(arr):
    #print(arr)
    sortedList = []
    arr = sorted(arr)
    for min in range(0,4):
        sortedList.append(arr[min])
    return sortedList


dataFrame = pd.read_csv(open(os.path.join(sys.path[0],'datanew.csv')))
dataFrame= dataFrame.drop(columns = 'Sl')
dataFrame.set_index(' ROLL NO. ',inplace  = True)

subjectList = ['HU101','PH101','M101','ME101','ES101','PH191','ES191','ME192','HU181','XC181']

print(dataFrame.loc[10900113001].index)
print(dataFrame.loc[10900113001])

MAIN_LIST = {}


for students in dataFrame.index:
    arr = []
    SUBJECTS_WITH_LOWEST_MARKS = []
    for subjects in subjectList:
        arr.append(dataFrame.loc[students][subjects])

    #print(arr)
    least = minimum(arr)
    for subjects in subjectList:
        if(dataFrame.loc[students][subjects] in least):
            SUBJECTS_WITH_LOWEST_MARKS.append(subjects)
            least.pop(least.index(dataFrame.loc[students][subjects]))

    MAIN_LIST[students] = SUBJECTS_WITH_LOWEST_MARKS

print(MAIN_LIST)
