# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 20:17:17 2020

Curtis Easton

This is a program that takes a .csv file from schoology, and imports it into a Course object. Student info is 
stored in a list of Student Objects within a Course, including individual quiz scores. 

Within the Course class are some functions for printing high scores. 
"""
import bisect
import random

class Student:
    def __init__(self,ID,firstName,lastName):
        self.name = firstName + " " + lastName
        self.ID = ID
        self.score = 0
        self.quizzes = []
        self.nickName =[]
    
    def addScore(self,newScore):
        self.score += float(newScore)
        
class Quiz:
    def __init__(self,quizName):
        self.name = quizName
        self.scores = []
        self.students = []

class Course:
    def __init__(self):
        self.nickNames=[['N/A', 'Alyssa', 'Adkins', '23200106'], ['N/A', 'Jose', 'Antunez Adame', '23200249'], ['N/A', 'Desirae', 'Bello', '23200269'], ['N/A', 'Macy', 'Boring', '23200293'], ['Ninja', 'Seanna', 'Bradford', '23200284'], ['N/A', 'Daniel', 'Crawford', '23200587'], ['N/A', 'Jose', 'Delgadillo Angon', '21200340'], ['N/A', 'Colleen', 'Ellsworth', '23200512'], ['N/A', 'Faith', 'Erikson', '23200463'], ['N/A', 'Cortez', 'Flakes', '23200558'], ['N/A', 'Shaeil', 'Grijalva Avila', '23200379'], ['N/A', 'Brayan', 'Lascares Zambrano', '23200095'], ['Speed Racer', 'Darius', 'Maddox', '23200457'], ['N/A', 'Michael', 'Martinez', '23200047'], ['N/A', 'Mya', 'Matus', '23200393'], ['N/A', 'Allison', 'Menger', '23200374'], ['N/A', 'Luis', 'Morales Barcenas', '23200339'], ['N/A', 'Isaac', 'Ramirez', '23200385'], ['Mrcu', 'Marcus', 'Reno', '23200501'], ['N/A', 'Tamara', 'Rogers', '23200461'], ['N/A', 'Natalie', 'Thompson', '23200311'], ['N/A', 'Tydrick', 'Tyler', '23200255'], ['N/A', 'Jesus', 'Uribe', '22200599'], ['N/A', 'Serenity', 'Vasquez Perez', '23200116'], ['N/A', 'Casey-Nyree', 'Belt', '23200525'], ['N/A', 'Chloe', 'Bradley', '23200168'], ['N/A', 'Leticia', 'Careaga', '23200391'], ['N/A', 'Yahir', 'Cebreros Arellano', '23200109'], ['N/A', 'Mike William', 'Espiritu', '23200439'], ['Christopher15', 'Christopher', 'Flor-Aguilar', '23200220'], ['N/A', 'Larissa', 'Fredericks', '23200465'], ['N/A', 'Desirae', 'Hagood', '23200273'], ['N/A', 'Nevaeh', 'Hillman', '23200051'], ['N/A', 'Toni', 'Littleman', '23200039'], ['N/A', 'Yaretzi', 'Lopez Martin', '23200156'], ['Jazz', 'Jazmin', 'Martinez', '23200256'], ['Izzy', 'Isabelle', 'McCabe', '23200187'], ['N/A', 'Cristian', 'Mondragon-Alcaide', '23200250'], ['N/A', 'Alexis', 'Munoz Martinez', '23200473'], ['N/A', 'Timothy', 'Newman', '23200513'], ['Kay', 'Kaylynn', 'Ortega Vazquez', '23200345'], ['N/A', 'Ashton', 'Palma', '23200428'], ['Kimberly3', 'Kimberly', 'Ramos-Morales', '23200494'], ['N/A', 'Alexia', 'Rodriguez', '23200481'], ['N/A', 'Arleth', 'Rodriguez Leyva', '23200137'], ['N/A', 'Ramon', 'Roman Rojo', '23200390'], ['N/A', 'Daryl', 'Schnoor', '23200351'], ['N/A', 'Shelby', 'Shaffer', '23200308'], ['N/A', 'Marisa', 'Smale', '23200314'], ['N/A', 'Brady', 'Staton', '23200538'], ['N/A', 'Jeremiah', 'Stidhum', '23200244'], ['N/A', 'Quentin', 'Swindle', '23200235'], ['N/A', 'Donovan', 'Sylvester', '23200061'], ['N/A', 'Zaira', 'Urioste Herrera', '23200281'], ['N/A', 'Christhian', 'Valenzuela', '23200482'], ['N/A', 'Yahir', 'Vasquez Lopez', '23200372'], ['JRONA06', 'Austin', 'Wenio', '23200470']]
        self.studentIDs=[]
        self.studentNames=[]
        self.studentList=[]
        self.quizIDs=[]
        self.quizList=[]
        self.tests=["cat","dog","mouse","leper"]
        self.idsWithNickNames=[]
        self.chosenNames=[]
        
    def importNicknames(self):
        for item in self.nickNames:
            if item[0] != 'N/A':
                self.idsWithNickNames.append(item[3])
                self.chosenNames.append(item[0])
                
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
        
    def printHighScores(self,numScores):  
        highScores = []
        highScorers = []
        for item in self.studentList:
            if (item.score>0):
                self.insertScoreUser(item,item.score,item.ID,highScores,highScorers)
                
                
                """
                i=bisect.bisect_right(highScores,float(item.score))
                highScores.insert(i,item.score)
                ID=item.ID         
                ID=self.getNickname(ID)
                highScorers.insert(i,ID)     
                """
        #print high scores
        print("This week's top competitors are: \n")
        for x in range(1,numScores):
            str1=highScorers[-x]
            str_length=len(str1)+(13-len(highScorers[-x]))
            str1=str1.ljust(str_length)
            print(str1 + "  -  "+ str(int(highScores[-x])) + " pts") 
            
        print("\nOther winners this week:\n")
        randomNames=highScorers[0:len(highScorers)-1-numScores]
        randomNames=random.sample(randomNames,len(randomNames))
        for x in range(len(randomNames)):
            print(randomNames[x])
            
    def mostHundos(self):
        numHundos = []
        hundoStudents =[]
        for item in self.studentList:
            hundos=item.quizzes.count(100)
            if (hundos>0):
                i=bisect.bisect_right(numHundos,hundos)
                numHundos.insert(i,hundos)
                ID=item.ID
                ID=self.getNickname(ID)
                hundoStudents.insert(i,ID)
        print("\nBonus Award: Most Hundos! (Most 100% quizzes)\n")       
        for x in range(1,len(hundoStudents)):
            str1=hundoStudents[-x]
            str_length=len(str1)+(13-len(hundoStudents[-x]))
            str1=str1.ljust(str_length)
            print(str1 + "  -  "+ str(int(numHundos[-x])) + " hundos")
        print(hundoStudents)
        print("butts")
    
# Import Data and Load into Course object     
intSci=Course()

with  open('March30.csv', 'r') as fin:
    text=(fin.readlines()) #read schoology .csv into python
    categories=text.pop(0).split(",") #pop the categories line
for x in range(len(text)): #iterate through all the quiz scores to be added
    text[x]=text[x].split(",") #change current data into list
    quizAttempt=text[x]
    for y in range(len(quizAttempt)): #remove inexplicable quotations in data file
       quizAttempt[y]=quizAttempt[y].replace("\"","") 
    text[x]=quizAttempt
    
for x in range(len(text)):
    quizAttempt=text[x]       
    
    #create and update Student objects
    if quizAttempt[0] in intSci.studentIDs:  #if student is already added to studentList
        idx=intSci.studentIDs.index(quizAttempt[0]) #get student index 
        if (quizAttempt[13] != ''): #if there is a quiz score
            intSci.studentList[idx].quizzes.append(float(quizAttempt[13])) #add score to list
            intSci.studentList[idx].addScore(float(quizAttempt[13])) #update total score
    else : #if student is not there, create student and add result
        intSci.studentNames.append(quizAttempt[1] + " " + quizAttempt[2]) #add student name to master list
        intSci.studentIDs.append(quizAttempt[0]) # add student number to master list
        intSci.studentList.append(Student(quizAttempt[0],quizAttempt[1],quizAttempt[2])) #initialize and store student object
        if (quizAttempt[13] != ''):
            intSci.studentList[-1].quizzes.append(float(quizAttempt[13]))
            intSci.studentList[-1].addScore(float(quizAttempt[13]))
        




intSci.importNicknames()
intSci.printHighScores(24)
intSci.mostHundos()
