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
        self.hundoStudents = []
        self.highScores = []
        self.highScorers =[]
        self.toPrint = []

        #import data
        with  open(filename, 'r') as fin:
            text=(fin.readlines()) #read schoology .csv into python
            text.pop(0).split(",") #pop the categories line
        for x in range(len(text)): #iterate through all the quiz scores to be added
            text[x]=text[x].split(",") #change current data into list
            quizAttempt=text[x]       
            #create and update Student objects
            if quizAttempt[0] in self.studentIDs:  #if student is already added to studentList
                idx=self.studentIDs.index(quizAttempt[0]) #get student index 
                if (quizAttempt[13] != ''): #if there is a quiz score
                    self.studentList[idx].quizzes.append(float(quizAttempt[13])) #add score to list
                    self.studentList[idx].quizNames.append(quizAttempt[10])
                    self.studentList[idx].score+=float(quizAttempt[13]) #update total score
                    if quizAttempt[10] in chemQuizzes:
                        self.studentList[idx].chemistry += float(quizAttempt[13])
                    if quizAttempt[10] in astrQuizzes:
                        self.studentList[idx].astronomy += float(quizAttempt[13])
            else : #if student is not there, create student and add result
                self.studentNames.append(quizAttempt[1] + " " + quizAttempt[2]) #add student name to master list
                self.studentIDs.append(quizAttempt[0]) # add student number to master list
                self.studentList.append(Student(quizAttempt[0],quizAttempt[1],quizAttempt[2])) #initialize and store student object
                if (quizAttempt[13] != ''):
                    self.studentList[-1].quizzes.append(float(quizAttempt[13]))
                    self.studentList[-1].quizNames.append(quizAttempt[10])
                    self.studentList[-1].score+=float(quizAttempt[13]) 
                    if quizAttempt[10] in chemQuizzes:
                        self.studentList[-1].chemistry += float(quizAttempt[13])
                    if quizAttempt[10] in astrQuizzes:
                        self.studentList[-1].astronomy += float(quizAttempt[13])
                        
    def createCompeteList
        for x in range(len(text)): #iterate through all the quiz scores to be added
            text[x]=text[x].split(",") #change current data into list
            quizAttempt=text[x]       
            #create and update Student objects
            if quizAttempt[0] in self.studentIDs:  #if student is already added to studentList
                idx=self.studentIDs.index(quizAttempt[0]) #get student index 
                if (quizAttempt[13] != ''): #if there is a quiz score
                    self.studentList[idx].quizzes.append(float(quizAttempt[13])) #add score to list
                    self.studentList[idx].quizNames.append(quizAttempt[10])
                    self.studentList[idx].score+=float(quizAttempt[13]) #update total score
                    if quizAttempt[10] in chemQuizzes:
                        self.studentList[idx].chemistry += float(quizAttempt[13])
                    if quizAttempt[10] in astrQuizzes:
                        self.studentList[idx].astronomy += float(quizAttempt[13])

    def getNickname(self,initID):
        if initID in self.idsWithNickNames:
            idx=self.idsWithNickNames.index(initID)
            return self.chosenNames[idx]
        else:
            return initID
        
    def insertScoreUser (self,student,score,user,scoreList,userList):
        i=bisect.bisect_right(scoreList,float(score))
        scoreList.insert(i,score)
        ID=student.ID         
        ID=self.getNickname(ID)
        userList.insert(i,ID)  
        
    def getHighScores(self,numScores): 
        self.highScores = []
        self.highScorers = []
        for item in self.studentList:
            if (item.score>0):
                self.insertScoreUser(item,item.score,item.ID,self.highScores,self.highScorers)
        self.toPrint=[self.highScorers,self.highScores]
        return self.toPrint
    
    def printLeaders(self,namesScores):
        numScores=len(namesScores[1])
        for x in range(1,numScores):
            str1=namesScores[0][-x]
            str_length=len(str1)+(13-len(namesScores[0][-x]))
            str1=str1.ljust(str_length)
            print(str1 + "  -  " + str(int(namesScores[1][-x])) + " pts")

    def printHighScores(self,numScores):
        print("The top scores are:")
        self.toPrint=self.getHighScores(numScores)
        self.printLeaders(self.toPrint)
        
    def writeNicknames(self):
        writeStr=[]
        with open("nickNamesList.txt","w") as fout:
            for element in (self.nickNames):
                writeStr=element[0]
                for x in range(1,len(element)):
                    writeStr=writeStr+","+element[x]
                fout.write(writeStr)
                fout.write('\n')
                
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
                
    def getStudent(self,firstname): #add new student nickname
        for element in self.studentList:
            if firstname in element.name:
                print ('get student: ' + element.name + '?')
                print("type y/n")
                result=input() #use user input to decide if correct student found
                if result == 'y': #if correct student found, edit student. else move to next student w/ same first name
                    return element
                    break
                
# Import Data and Load into Course object     
intSci=scoreSheet('March30.csv')
     
#Output 
intSci.importNicknames()
intSci.printHighScores(24)
#intSci.mostHundos()
