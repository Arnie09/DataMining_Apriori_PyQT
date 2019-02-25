import pandas as pd
import os
import sys

dataFrame = pd.read_csv(open(os.path.join(sys.path[0],'data.csv')))

marks = {'O':10,'E':9,'A':8,'B':7,'C':6,'D':5,'F':4}
dataFrame.drop(columns = 'Sl')
dataFrame.set_index(' ROLL NO. ',inplace  = True)

x = 0
for i in dataFrame["HU101"]:
    dataFrame["HU101"][x:x+1]=dataFrame["HU101"][x:x+1].str.replace(i,str(marks[i]))
    x = x+1

x = 0
for i in dataFrame["PH101"]:
    dataFrame["PH101"][x:x+1]=dataFrame["PH101"][x:x+1].str.replace(i,str(marks[i]))
    x = x+1

x = 0
for i in dataFrame["M101"]:
    dataFrame["M101"][x:x+1]=dataFrame["M101"][x:x+1].str.replace(i,str(marks[i]))
    x = x+1

x = 0
for i in dataFrame["ME101"]:
    dataFrame["ME101"][x:x+1]=dataFrame["ME101"][x:x+1].str.replace(i,str(marks[i]))
    x = x+1

x = 0
for i in dataFrame["ES101"]:
    dataFrame["ES101"][x:x+1]=dataFrame["ES101"][x:x+1].str.replace(i,str(marks[i]))
    x = x+1

x = 0
for i in dataFrame["PH191"]:
    dataFrame["PH191"][x:x+1]=dataFrame["PH191"][x:x+1].str.replace(i,str(marks[i]))
    x = x+1

x = 0
for i in dataFrame["ES191"]:
    dataFrame["ES191"][x:x+1]=dataFrame["ES191"][x:x+1].str.replace(i,str(marks[i]))
    x = x+1

x = 0
for i in dataFrame["ME192"]:
    dataFrame["ME192"][x:x+1]=dataFrame["ME192"][x:x+1].str.replace(i,str(marks[i]))
    x = x+1

x = 0
for i in dataFrame["HU181"]:
    dataFrame["HU181"][x:x+1]=dataFrame["HU181"][x:x+1].str.replace(i,str(marks[i]))
    x = x+1

x = 0
for i in dataFrame["XC181"]:
    dataFrame["XC181"][x:x+1]=dataFrame["XC181"][x:x+1].str.replace(i,str(marks[i]))
    x = x+1


# for elements in dataFrame.index:
#     print(dataFrame.loc[10900113021])

dataFrame.to_csv(os.path.join(sys.path[0],'datanew.csv'))
#print(dataFrame.loc[10900113021])
