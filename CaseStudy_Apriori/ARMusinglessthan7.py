import pandas as pd
import os
import sys
from  Apriori_core import apriori

dataFrame = pd.read_csv(open(os.path.join(sys.path[0],'data_new.csv')))
dataFrame= dataFrame.drop(columns = 'Sl')

dataFrame.set_index(' ROLL NO. ',inplace  = True)

subjectList = ['HU101','PH101','M101','ME101','ES101','PH191','ES191','ME192','HU181','XC181']

MAIN_LIST = {}

for rollNo in dataFrame.index:
    arr=[]
    SUBJECTS_WITH_GRADE_D = []
    for subject in subjectList:
        if(dataFrame.loc[rollNo][subject]<7):
            SUBJECTS_WITH_GRADE_D.append(subject)
    if(SUBJECTS_WITH_GRADE_D !=[]):
         MAIN_LIST[rollNo]=SUBJECTS_WITH_GRADE_D

AprioriInstance=apriori(min=18,transactions=MAIN_LIST,productlist = subjectList)
for elements in AprioriInstance.finalRules:
    for i in AprioriInstance.finalRules[elements]:
        print(i)
