import pandas as pd
import os
import sys

dataFrame = pd.read_csv(open(os.path.join(sys.path[0],'data.csv')))

marks = {'O':10,'E':9,'A':8,'B':7,'C':6,'D':5,'F':4}
dataFrame.drop(columns = 'Sl')
dataFrame.set_index(' ROLL NO. ',inplace  = True)

subjectList = ['HU101','PH101','M101','ME101','ES101','PH191','ES191','ME192','HU181','XC181']
for subjects in subjectList:
    x = 0
    for i in dataFrame[subjects]:
        dataFrame[subjects][x:x+1]=dataFrame[subjects][x:x+1].str.replace(i,str(marks[i]))
        x = x+1

dataFrame.to_csv(os.path.join(sys.path[0],'data_new.csv'))
#print(dataFrame.loc[10900113021])
