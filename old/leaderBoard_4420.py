# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 20:17:17 2020

Curtis Easton

This is a program that takes a .csv file from schoology, and imports it into a Course object. Student info is 
stored in a list of Student Objects within a Course, including individual quiz scores. 

Within the Course class are some functions for calculating and printing high scores. 
"""
import bisect
import random

chemQuizzes=['The Number of Neutrons (CO Pages 4-6)','Valence Electrons / Energy Levels (CO Pages 8-11)',
                  'Dot Diagrams and Charge (CO Pages 13-16)','Chemical Formulas (CO Page 18)',
                  'Ionic and Covalent Bonding (CO Pages 20-24)','Reactions1 Quiz','Reactions2 Quiz',
                  'Elephant Toothpaste Quiz','Protons Neutrons Electrons (CO Page 2)']
astrQuizzes=['1 - The Fusing of Elements Quiz','2 - Solar Nuclear Fusion Quiz']


class Student:
    def __init__(self,ID,firstName,lastName):
        self.name = firstName + " " + lastName
        self.ID = ID
        self.score = 0
        self.weekScore = 0
        self.quizzes = []
        self.quizNames =[]
        self.nickName =[]
        self.astronomy = 0
        self.chemistry = 0
        self.numHundos = 0

class scoreSheet:
    def __init__(self,filename):
        self.nickNames=[]
        self.studentIDs=[]
        self.studentNames=[]
        self.studentList=[]
        self.quizIDs=[]
        self.quizList=[]
        self.idsWithNickNames=[]
        self.chosenNames=[]
        self.numHundos = []
        self.nameHundos = []
        self.highScores = []
        self.highScorers =[]
        self.toPrint = []
        self.astScores=[]
        self.astronomers=[]

        #import data
        with  open(filename, 'r') as fin:
            text=(fin.readlines()) #read schoology .csv into python
            text.pop(0).split(",") #pop the categories line
        for x in range(len(text)): #iterate through all the quiz scores to be added
            text[x]=text[x].split(",") #change current data into list
            quizAttempt=text[x]
            #create and update Student objects
            if quizAttempt[0] in self.studentIDs:  #if student is already added to studentList
                self.createPlayerList(quizAttempt[0],quizAttempt[13],quizAttempt[10])
            else : #if student is not there, create student and add result
                self.addScore(quizAttempt[1],quizAttempt[2],quizAttempt[0],quizAttempt[13],quizAttempt[10])
                
    """ __init__ methods """                 
    def createPlayerList(self,ID,quizScore,quizName):
                idx=self.studentIDs.index(ID) #get student index 
                if (quizScore != ''): #if there is a quiz score
                    self.studentList[idx].quizzes.append(float(quizScore)) #add score to list
                    self.studentList[idx].quizNames.append(quizName)
                    self.studentList[idx].score+=float(quizScore) #update total score
                    if quizName in chemQuizzes:
                        self.studentList[idx].chemistry += float(quizScore)
                    if quizName in astrQuizzes:
                        self.studentList[idx].astronomy += float(quizScore)
                   
    def addScore(self,firstName,lastName,ID,quizScore,quizName):
        self.studentNames.append(firstName + " " + lastName) #add student name to master list
        self.studentIDs.append(ID) # add student number to master list
        self.studentList.append(Student(ID,firstName,lastName)) #initialize and store student object
        if (quizScore != ''):
            self.studentList[-1].quizzes.append(float(quizScore))
            self.studentList[-1].quizNames.append(quizName)
            self.studentList[-1].score+=float(quizScore) 
            if quizName in chemQuizzes:
                self.studentList[-1].chemistry += float(quizScore)
            if quizName in astrQuizzes:
                self.studentList[-1].astronomy += float(quizScore)

    """ user tools """
    def getStudent(self,firstname): #add new student nickname
        for element in self.studentList:
            if firstname in element.name:
                print ('get student: ' + element.name + '?')
                print("type y/n")
                result=input() #use user input to decide if correct student found
                if result == 'y': #if correct student found, edit student. else move to next student w/ same first name
                    return element
                    break

    """ calculate stuff """                 
    def getHighScores(self): 
        for item in self.studentList:
            if (item.score>0):
                self.insertScoreUser(item,item.score,item.ID,self.highScores,self.highScorers)
        self.toPrint=[self.highScorers,self.highScores]
    
    def mostHundos(self):
        for item in self.studentList:
            item.numHundos=item.quizzes.count(100)
            if (item.numHundos>0):
                self.insertScoreUser(item,item.numHundos,item.ID,self.numHundos,self.nameHundos)
        self.toPrint=[self.nameHundos,self.numHundos]
        
    def topAstronomer(self):
        for item in self.studentList:
            if (item.astronomy>0):
                self.insertScoreUser(item,item.astronomy,item.ID,self.astronomy,self.astronomers)
        self.toPrint=[self.nameHundos,self.numHundos]
        
    """ used by 'calculate stuff' above """    
    def insertScoreUser (self,student,score,user,scoreList,userList):
        i=bisect.bisect_right(scoreList,float(score))
        scoreList.insert(i,score)
        ID=student.ID         
        ID=self.insertNickname(ID)
        userList.insert(i,ID) 
        
    """ print stuff """           
    def printLeaders(self,namesScores,numScores):
        if numScores=='all':
            numScores=len(namesScores[1])
        for x in range(1,numScores+1):
            str1=namesScores[0][-x]
            str_length=len(str1)+(13-len(namesScores[0][-x]))
            str1=str1.ljust(str_length)
            print(str1 + "  -  " + str(int(namesScores[1][-x])) + " pts")
        print("\n")

    def printHighScores(self,numScores):
        print("The top scores are:")
        self.getHighScores()
        self.printLeaders(self.toPrint,numScores)
        
    def printNumHundos(self,numScores):
        print("The top scores are:")
        self.mostHundos()
        self.printLeaders(self.toPrint,numScores)
                
    """ Nickname insert/import/edit/save """
    def insertNickname(self,initID):
        if initID in self.idsWithNickNames:
            idx=self.idsWithNickNames.index(initID)
            return self.chosenNames[idx]
        else:
            return initID
    
    def importNicknames(self):
        with  open('nickNamesList.txt', 'r') as fin:
            text=(fin.readlines()) #read schoology .csv into python
        for x in range(len(text)): #iterate through all the quiz scores to be added
            self.nickNames.append(text[x].rstrip('\n').split(",")) #change current data into list
        for item in self.nickNames:
            if item[0] != 'N/A':
                self.idsWithNickNames.append(item[3])
                self.chosenNames.append(item[0])
    
    def addNickname(self,firstname,nickName): #add new student nickname
        for element in self.nickNames:
            if element[1] == firstname: #use firstname to find student
                print("edit student: "+ firstname + " "+element[2]+"?") #display student last name
                print("type y/n")
                result=input() #use user input to decide if correct student found
                if result == 'y': #if correct student found, edit student. else move to next student w/ same first name
                    element[0]=nickName
                    self.writeNicknames()
                    break
    
    def writeNicknames(self):
        writeStr=[]
        with open("nickNamesList.txt","w") as fout:
            for element in (self.nickNames):
                writeStr=element[0]
                for x in range(1,len(element)):
                    writeStr=writeStr+","+element[x]
                fout.write(writeStr)
                fout.write('\n')

# Import Data and Load into Course object     
intSci=scoreSheet('March30.csv')
     
#Output 
intSci.importNicknames()
intSci.printHighScores(5)
intSci.printNumHundos('all')
#intSci.mostHundos()
