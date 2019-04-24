import pandas as pd
from itertools import combinations
class apriori:

    def __init__(self,**kwargs):

        self.rulesLength = kwargs.get('rules_len')
        self.min = kwargs.get('min')
        self.minConf=kwargs.get('minConf')
        self.maxConf=kwargs.get('maxConf')
        self.rulesMin = kwargs.get('rulesMin')
        if(kwargs.get('address') is not None):
            self.dataset=pd.read_excel(kwargs.get('address'))
            self.index = kwargs.get('invNo')

            '''index has been set here'''
            self.dataset.set_index(self.index,inplace = True)

            self.columnheader=list(self.dataset.columns)

        if(kwargs.get('transactions') is not None):
            self.transaction = kwargs.get('transactions')
            self.uniqproductcode = kwargs.get('productlist')
        else:
            self.transaction={}  #to store all the transactions w.r.t invNo
            self.uniqproductcode=[] #storing the codes of each product only once

        self.allLs={}
        self.finalL={}
        self.finalRules={}

        if(self.transaction):# boolean on an empty dictionary returns false
            self.createL1()
            self.createLs()
        else:
            self.preprocess()
            self.createL1()
            self.createLs()

    def preprocess(self):
        MAIN_LIST={}
        content = []
        SUBJECTS = self.columnheader

        '''filling up the dictionary with empty lists'''
        for students in self.dataset.index:
            MAIN_LIST[students] = []

        '''grouping of marks into good,average,poor based on the higest and lowest in the subjects is done here'''
        for subjects in SUBJECTS:
            marks = sorted(self.dataset[subjects])
            min,max = marks[0], marks[len(marks)-1]
            diff= (max-min)/3
            for students in self.dataset.index:
                scores = ""
                marks = self.dataset.loc[students][subjects]
                String = ""
                if(marks>=max - diff):
                    String = "Good marks in "
                elif(marks>= min+diff and marks<max-diff):
                    String = "Average marks in "
                else:
                    String = "Poor marks in "
                scores = (String+subjects)
                MAIN_LIST[students].append(scores)
                if(scores not in content):
                    content.append(scores)

        self.transaction = MAIN_LIST
        self.uniqproductcode = content

    def createL1(self):

        l1={}
        temp=[]
        for item in self.uniqproductcode:
            count=0
            for eachlist in self.transaction:
                if item in self.transaction[eachlist]:
                    count+=1
            if count>=self.min:
                temp.append(item)
                l1[tuple(temp)]=count
                temp=[]

        self.allLs[1]=l1

    def createLs(self):
        List=self.allLs[1]
        a=1

        while(len(List)!= 0 and a<=self.rulesLength):
            a+=1
            List=self.createList(List,a)
            self.allLs[a]=List
            self.finalL=self.allLs[a]
            self.displayRules(a)

    def createList(self,List,a):
        lx={}
        combo=[] #We dont want anagrams of a similar combo so we store each uniq combination here and compare the new one with each of its item
        lprevKeys=list(List.keys())
        L=len(lprevKeys)
        for i in range(0,L):
            for j in range(i+1,L):

                pair=self.comb(list(lprevKeys[i]),list(lprevKeys[j]))

                if len(pair)==a:
                    uniqcheck=True

                    for eachcombo in combo:
                        if all(i in eachcombo for i in pair):
                            uniqcheck=False
                    if uniqcheck:
                        count=0
                        for eachlist in self.transaction:
                            if all(elem in self.transaction[eachlist] for elem in pair):
                                count+=1
                        if(count>=self.min):
                            lx[tuple(pair)]=count
                            combo.append(pair)
        return lx

    def displayRules(self,a):
        #print("All the important associations are:  \n")
        rules=[]
        for keys in self.finalL:
            supL=self.finalL[keys] #support of FinalList
            L=list(keys) #items of finallist stored as a list

            subsets=[]


            for i in range(1,len(keys)):
                subsets.append(list(combinations(keys,i))) #all non-empty subsets created and stored as tuples in subsets list

            #we will use S to store each subset. L stores the main set
            minconfi=self.minConf/100
            maxconfi = self.maxConf/100
            for eachlist in subsets:
                for subset in eachlist:
                    S=list(subset)
                    LminusS=[i for i in L if i not in S]
                    supS=self.allLs[len(subset)][subset]
                    confidence = supL/supS

                    if confidence>=minconfi and confidence<=maxconfi:
                        rule=(str(S)+"=>"+str(LminusS)+": "+str(confidence*100)+"%")
                        rules.append(rule)
        self.finalRules[a]=rules

    def comb(self,A,B): #It combines two lists without keeping duplicates while maintaining the order
        c=A+[]
        for i in B:
            if i not in A:
                c.append(i)
        return c
