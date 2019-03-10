import math
import pandas as pd
import xlrd
import pydot
import os,sys
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
        self.graphcount=1

        if(kwargs.get('address') is not None):
            self.initialiseData(kwargs.get('address'),kwargs.get('TransID'),kwargs.get('ProductCode'))

        elif(kwargs.get('transactions') is not None):

            self.dataSet=kwargs.get('transactions')
            self.formatdata()

        self.mainTree,self.mainHeadertable=self.createTree(self.dataSet,self.minSup)# main FP tree and HeaderTable are formed

        #self.displaytree(self.mainTree)


    def formatdata(self):

        self.dataSet=list(self.dataSet.values())
        for i in self.dataSet:
            i.append(1)


    def initialiseData(self,path,TransID,ProductCode):#This function converts the dataset to the format in which our algorithm will work.
        dataset=pd.read_csv(path)
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
                self.displaytree(retTree)

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


    def displaytree(self,node):
        self.tree = pydot.Dot(graph_type='digraph')
        self.round(node)
        self.tree.write_png(os.path.join(sys.path[0],'graph'+str(self.graphcount)+'.png'))
        self.graphcount+=1


    def round(self,nod):
        for i in nod.children:
            self.tree.add_node(pydot.Node(str(nod.label),label=(str(nod.name)+' : '+str(nod.count))))
            self.tree.add_node(pydot.Node(str(nod.children[i].label),label=(str(nod.children[i].name+' : '+str(nod.children[i].count)))))
            edge=pydot.Edge(str(nod.label),str(nod.children[i].label))
            self.tree.add_edge(edge)
            self.round(nod.children[i])

obj=FP_Tree(min=2,transactions={101:['A','B','D','E'],
                  102:['B','C','E'],
                  103:['A','B','D','E'],
                  104:['A','B','C','E'],})
