import pandas as pd
from Apriori_core import apriori
import os
import sys
''' This function returns the minimum 4 marks that has been sent by the for loop'''
def minimum(arr):
    #print(arr)
    sortedList = []
    arr = sorted(arr)
    for min in range(0,4):
        sortedList.append(arr[min])
    return sortedList

dataFrame = pd.read_csv(open(os.path.join(sys.path[0],'data_new.csv')))
dataFrame= dataFrame.drop(columns = 'Sl')
dataFrame.set_index(' ROLL NO. ',inplace  = True) #sets the index

subjectList = ['HU101','PH101','M101','ME101','ES101','PH191','ES191','ME192','HU181','XC181']

MAIN_LIST = {}

'''dataFrame.index gives the list of the roll ids'''
'''we iterate through each student id'''
'''we send the marks of the students in a list to minimum which returns least marks of the student'''
'''we then create a list that stores the subject name of the lowest marks corresponfing to each student'''
'''we create a dictionary that contains student id and all the subjects in which he has the lowest marks'''

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

#min = int(input("Enter minimum confidence : "))
min = 2

'''calling the Apriori function'''
AprioriInstance = apriori(min = min , transactions = MAIN_LIST , productlist = subjectList)

'''displaying the rules and associations geerated by apriori'''
for elements in AprioriInstance.allLs:
    print(AprioriInstance.allLs[elements])

print()

for elements in AprioriInstance.finalRules:
    print(AprioriInstance.finalRules[elements])
