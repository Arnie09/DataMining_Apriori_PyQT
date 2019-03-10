import math
import pandas as pd
import xlrd

class treeNode:
    def __init__(self,name,count,parent,label):
        self.name=str(name)
        self.count=count
        self.parent=parent
        self.children={}
        self.nodeLink=None #to store the link to the next similar node in the fp tree
        self.label=str(label) #this is important for creating two different nodes of same name in the fptree display. If tree is not being displayed, this is useless
    #Adding Children to the current node
    def addChildren(self,child):
        self.children[child.name]=child
    #A display function just for debugging purpose
    def disp(self, ind=1):
        print ('  '*ind, self.name, ':', self.count)
        for child in self.children.values():
            child.disp(ind+1)


class FP_Tree:
    def __init__(self,**kwargs):
        self.minSup=kwargs.get('min')
        self.labelcount=0
        self.freqItems=[]
        self.dataSet={}
        self.conf=0.8

        if(kwargs.get('address') is not None):
            self.initialiseData(kwargs.get('address'),kwargs.get('TransID'),kwargs.get('ProductCode'))

        elif(kwargs.get('transactions') is not None):

            self.dataSet=kwargs.get('transactions')
            self.formatdata()


        self.mainTree,self.mainHeadertable=self.createTree(self.dataSet,self.minSup)# main FP tree and HeaderTable are formed


        self.mineTree(self.mainTree,self.mainHeadertable,[],math.inf) #Mining the main tree


    def formatdata(self):

        self.dataSet=list(self.dataSet.values())
        for i in self.dataSet:
            i.append(1)


    def initialiseData(self,path,TransID,ProductCode):#This function converts the dataset to the format in which our algorithm will work.
        dataset=pd.read_excel(path)
        invNo=dataset[TransID]
        productcode=dataset[ProductCode]

        for i in range(len(invNo)):
            self.dataSet[invNo[i]]=self.dataSet.get(invNo[i],[])+[str(productcode[i])]

        self.formatdata()


    def createTree(self,data,sup):#This function creates the FP tree for the data passed and returns the tree along with the corrosponding HeaderTable. This function was created keeping in mind that it will be used recursively
        headerTable={}

        for trans in data:
            for item in trans[:-1]:
                headerTable[item]=headerTable.get(item,0)+trans[-1]
        for k in set(headerTable):
            if headerTable[k]<sup:
                del(headerTable[k])
        for k in headerTable:
            headerTable[k]=[headerTable[k],None]

        retTree=treeNode('Null',0,None,'Null'+str(self.labelcount)) #The root node is created here with name null
        self.labelcount+=1 #Ignore label count as it is for tree visualisation only and useless here
        freqitems=list(headerTable.keys())

        for trans in data:
            local={}
            for item in trans[:-1]:
                if item in freqitems:
                    local[item]=headerTable[item][0]
            if(len(local)>0):
                ordereditems=[v[0] for v in sorted(local.items(),key=lambda p:p[1],reverse=True)] #sorted w.r.t support count in descending order
                self.updateTree(ordereditems,retTree,headerTable,trans[-1])




        return retTree,headerTable


    def updateTree(self,items,inTree,headerTable,count): #This function is used by create tree function to add each transaction as a subtree to the root node
        if items[0] in inTree.children:
            inTree.children[items[0]].count+=count
        else:
            newNode=treeNode(items[0],count,inTree,str(items[0])+str(self.labelcount))
            self.labelcount+=1
            inTree.addChildren(newNode)
            if headerTable[items[0]][1]==None:
                headerTable[items[0]][1]=newNode
            else:
                self.updateHeader(headerTable[items[0]][1],newNode)
        if len(items)>1:
            self.updateTree(items[1:],inTree.children[items[0]],headerTable,count)

    def updateHeader(self,nodeToTest,targetNode): #This function is used by updateTree function to keep the Header updated as pasr the tree
        while (nodeToTest.nodeLink != None):
            nodeToTest = nodeToTest.nodeLink
        nodeToTest.nodeLink = targetNode


    def ascendTree(self,node,path): #A small function used by findPrefixPath function to climb the tree while recording the path till it reaches root node

        if node.parent!=None:
            path.append(node.name)
            self.ascendTree(node.parent,path)

    def findPrefixPath(self,basePat,node): #This function returns the conditional pattern bases for a give node
        condPat=[]

        while node!=None:
            prefixpath=[]
            self.ascendTree(node,prefixpath)
            if len(prefixpath)>1:
                condPat.append(prefixpath[1:]+[node.count])
            node=node.nodeLink
        return condPat


    def mineTree(self,inTree,headerTable,preFix,count):#This function is for mining the main tree as well as the conditional trees

        #bigL = [v[0] for v in sorted(headerTable.items(), key=lambda p: p[1][0])]
        bigL=headerTable

        for basePat in bigL:
            k=min(headerTable[basePat][0],count)
            newFreqItem=preFix.copy()
            newFreqItem.append(basePat)
            #if len(newFreqItem)>1:
            self.freqItems.append(newFreqItem+[k])
            condPattbases=self.findPrefixPath(basePat,headerTable[basePat][1])
            myCondTree,myHead=self.createTree(condPattbases,self.minSup)
            if myHead!=None:
                self.mineTree(myCondTree,myHead,newFreqItem,k)

    def display(self):
        ordereditems=[v for v in sorted(self.freqItems,key=len)]
        for i in ordereditems:
            print(i)

    def loop(self,L,k,rules,supL):
        for i in L:
            l=[x for x in L if x != i]
            r=[x for x in k if x not in l]
            if not(l==[] or r==[]):
                confidence=supL/self.suppdata[tuple(l)]
                rule=tuple([tuple(l),tuple(r),confidence*100])
                if rule not in rules and confidence>=self.conf:
                    rules.append(rule)
                    self.loop(l,k,rules,supL)
    def displayRules1(self):
        self.suppdata={}
        k=list(self.mainHeadertable.keys())
        for i in range(len(self.freqItems)):
            t=self.freqItems[i][-1]
            self.freqItems[i]=[v for v in sorted(self.freqItems[i][:-1],key=k.index)]+[t]
        for i in self.freqItems:
            self.suppdata[tuple(i[:-1])]=i[-1]
        for key in self.suppdata:
            supL=self.suppdata[key]
            Freqset=list(key)
            rules=[]
            self.loop(Freqset,Freqset,rules,supL)
            for rule in rules:
                count+=1
                print(rule[0],'=>',rule[1],str(round(rule[2]))+"%")
                print(count)








trans={10900113001: ['ME101', 'ES101', 'XC181'], 10900113005: ['HU101', 'PH101', 'M101', 'ME101', 'ES101', 'ME192'], 10900113006: ['HU101'], 10900113008: ['HU101', 'PH101', 'M101', 'ES101', 'XC181'], 10900113010: ['HU101', 'PH101', 'M101', 'ME101', 'ES101'], 10900113011: ['ME101'], 10900113012: ['HU101', 'PH101', 'M101', 'ME101', 'ES101', 'ME192', 'XC181'], 10900113013: ['ME101'], 10900113014: ['HU101', 'ME101'], 10900113015: ['ME101', 'XC181'], 10900113016: ['HU101', 'M101', 'ME101'], 10900113018: ['ME101'], 10900113020: ['HU101', 'PH101', 'ME101', 'ME192', 'XC181'], 10900113021: ['HU101', 'PH101', 'ME101', 'ES101'], 10900113022: ['PH101', 'ES101'], 10900113023: ['ME101'], 10900113024: ['HU101', 'PH101', 'M101', 'ME101', 'ES101'], 10900113025: ['HU101', 'PH101', 'M101', 'ME101', 'ES101'], 10900113027: ['XC181'], 10900113028: ['HU101', 'ME101', 'XC181'], 10900113029: ['HU101', 'PH101', 'ME101', 'ES101', 'XC181'], 10900113030: ['HU101', 'PH101', 'ES101'], 10900113031: ['M101', 'ME101', 'ES101'], 10900113032: ['PH101', 'M101', 'ME101', 'ES101'], 10900113034: ['PH101', 'ME101', 'ES101', 'XC181'], 10900113035: ['HU101', 'PH101', 'ES101'], 10900113037: ['ME101', 'ES101'], 10900113038: ['HU101'], 10900113039: ['HU101'], 10900113041: ['PH101', 'ME101', 'ES101'], 10900113042: ['HU101', 'PH101', 'M101', 'ME101', 'ES101'], 10900113043: ['XC181'], 10900113044: ['HU101', 'PH101', 'ME101', 'ES101'], 10900113045: ['HU101', 'ME101', 'ES101'], 10900113047: ['HU101'], 10900113049: ['HU101', 'PH101', 'ES101'], 10900113050: ['HU101', 'PH101', 'M101', 'ME101', 'ES101', 'ME192', 'XC181'], 10900113052: ['HU101', 'ME101', 'ES101'], 10900113053: ['HU101', 'PH101', 'M101', 'ME101', 'ES101'], 10900113054: ['HU101', 'PH101', 'ME101', 'ES101'], 10900113055: ['ME101', 'ES101'], 10900113056: ['HU101', 'ME101', 'ES101', 'XC181'], 10900113057: ['HU101', 'PH101', 'ME101', 'ES101', 'PH191', 'XC181'], 10900113059: ['HU101'], 10900113060: ['HU101', 'PH101', 'M101', 'ES101'], 10900113061: ['HU101', 'PH101', 'M101', 'ME101', 'ES101', 'XC181'], 10900113062: ['PH101', 'ES101'], 10900113063: ['ES101', 'ES191'], 10900113064: ['HU101', 'ES101'], 10900113065: ['HU101', 'ES101'], 10900113066: ['PH101', 'M101', 'ES101'], 10900113067: ['PH101', 'ME101', 'ES101', 'XC181'], 10900113068: ['PH101', 'ME101', 'ES101'], 10900113071: ['M101', 'ME101'], 10900113072: ['ME101'], 10900113073: ['PH101', 'ME101', 'XC181'], 10900113074: ['PH101', 'M101', 'ME101', 'ES101'], 10900113075: ['PH101', 'M101', 'ME101', 'ES101'], 10900113076: ['HU101', 'ES101'], 10900113077: ['ME101'], 10900113078: ['HU101', 'PH101', 'M101', 'ME101', 'ES101'], 10900113081: ['PH101', 'M101', 'ME101', 'ES101', 'XC181'], 10900113082: ['PH101', 'ME101', 'ES101'], 10900113084: ['ES101'], 10900113085: ['ME101', 'XC181'], 10900113086: ['ES101'], 10900113087: ['ES101'], 10900113088: ['ES101'], 10900113090: ['M101', 'ME101'], 10900113091: ['ES101'], 10900113092: ['M101', 'ME101'], 10900113094: ['ME101', 'ES101'], 10900113095: ['PH101', 'M101', 'ME101', 'ES101'], 10900113096: ['M101', 'ME101', 'ES101'], 10900113097: ['PH101', 'M101', 'ME101', 'ES101'], 10900113098: ['M101', 'ME101', 'ES101'], 10900113099: ['PH101', 'M101', 'ES101'], 10900113103: ['PH101', 'M101', 'ME101', 'ES101'], 10900113104: ['PH101', 'ME101', 'ES101', 'ME192'], 10900113105: ['ME101', 'ES101'], 10900113106: ['PH101', 'ME101', 'ES101', 'XC181'], 10900113107: ['HU101', 'PH101', 'M101', 'ME101', 'ES101', 'ME192', 'XC181'], 10900113109: ['HU101', 'PH101', 'ME101', 'ES101'], 10900113112: ['ES101'], 10900113113: ['HU101', 'ME101', 'XC181'], 10900113114: ['HU101', 'PH101', 'ME101', 'ES101', 'XC181'], 10900113115: ['HU101', 'PH101', 'M101', 'ME101', 'ES101', 'ME192', 'XC181'], 10900113116: ['HU101', 'PH101', 'ES101'], 10900113117: ['HU101', 'PH101', 'ES101', 'XC181']}


obj=FP_Tree(address=r"F:\LetsCode\Machine learning\Book1.xlsx",TransID="InvoiceNo",ProductCode="StockCode",min=4)#address,TransID,ProductCode,minSup):
#obj.display()
obj.displayRules1()
