# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 20:17:17 2020

@author: curti
"""
"""
class Student(object):
    __init__() functions
    def __init__(self, firstName, lastName, )


studentList=[]
student
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
    def addID(self,newID):
        self.studentIDs.append(newID)
    def addName(self,newName):
        self.studentNames.append(newName)             
    def addStudent(self,newStudent):
        self.studentList.append(newStudent)
    def addQuizID(self,newQuizID):
        self.quizIDs.append(newQuizID)       
    def addQuiz(self,newQuiz,idx):
        self.studentList[idx].quizzes.append(newQuiz)
    def getStudentIdx(self,ID):
        return self.studentIDs.index(ID)
    def existStudent(self,student):
        if student in self.studentIDs:
            return True
        else:
            return False
    def addScore(self,score,idx):
        self.studentList[idx].addScore(score)
    def getStudentList(self):
        return self.studentList
        
        
intSci=Course()

with  open('March29.csv', 'r') as fin:
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
    if intSci.existStudent(quizAttempt[0]):  #if student is already added to Course
        idx=intSci.getStudentIdx(quizAttempt[0]) #get student index 
        if (quizAttempt[13] != ''): #if there is a quiz score
            intSci.addQuiz(float(quizAttempt[13]),idx) #add score to list
            intSci.addScore(float(quizAttempt[13]),idx) #update total score
    else : #if student is not there, create student and add result
        intSci.addName(quizAttempt[1] + " " + quizAttempt[2]) #add student name to master list
        intSci.addID(quizAttempt[0]) # add student number to master list
        intSci.addStudent(Student(quizAttempt[0],quizAttempt[1],quizAttempt[2])) #initialize and store student object
        if (quizAttempt[13] != ''):
            intSci.addQuiz(float(quizAttempt[13]),-1)
            intSci.addScore(float(quizAttempt[13]),-1)
        
        
        
"""
#create and update Quiz objects        
if quizAttempt[10] in intSci.quizIDs: #if the quiz has already been created
    if (quizAttempt[13] != ''): #if entry has data to add
        idx=intSci.quizIDs.index(quizAttempt[10]) # get quiz index
        i=bisect.bisect_right(intSci.quizList[idx].scores,float(quizAttempt[13])) #rank attempt
        intSci.quizList[idx].scores.insert(i,float(quizAttempt[13])) #add score in appropriate position
        intSci.quizList[idx].students.insert(i,quizAttempt[1]) #add name in appropriate position
else: #create the quiz and add data
    if (quizAttempt[13] != ''): # if entry has data to add
        intSci.quizIDs.append(quizAttempt[10]) # add Quiz ID to quizID
        intSci.quizList.append(Quiz(quizAttempt[10])) # create new Quiz object in quizList
        intSci.quizList[-1].scores.append(float(quizAttempt[13])) # add score to Quiz
        intSci.quizList[-1].students.append(quizAttempt[1]) # add student to Quiz
        
"""
"""

studentss=intSci.studentIDs
#add nickNames
idsWithNickNames=[]
chosenNames=[]
for item in intSci.nickNames:
    if item[0] != 'N/A':
        idsWithNickNames.append(item[3])
        chosenNames.append(item[0])
        
highScores = []
highScorers = []
numHundos = []
hundoStudents =[]








#Output section
for item in intSci.studentList:
    if (item.score>0):
        i=bisect.bisect_right(highScores,float(item.score))
        highScores.insert(i,item.score)
        ID=item.ID
        if ID in idsWithNickNames:
            idx=idsWithNickNames.index(ID)
            ID=chosenNames[idx]
        highScorers.insert(i,ID)
        
    
#print high scores
print("This week's top 8 competitors are: \n")
for x in range(1,8):
    str1=highScorers[-x]
    str_length=len(str1)+(13-len(highScorers[-x]))
    str1=str1.ljust(str_length)
    print(str1 + "  -  "+ str(int(highScores[-x])) + " pts")  
    
    
print("\nOther winners this week:\n")
randomNames=highScorers[0:len(highScorers)-1-8]
randomNames=random.sample(randomNames,len(randomNames))
for x in range(len(randomNames)):
    print(randomNames[x])
    
print("\nBonus Award: Most Hundos! (Most 100% quizzes)\n")
for item in intSci.studentList:
    hundos=item.quizzes.count(100)
    if (hundos>0):
        i=bisect.bisect_right(numHundos,hundos)
        numHundos.insert(i,hundos)
        ID=item.ID
        if ID in idsWithNickNames:
            idx=idsWithNickNames.index(ID)
            ID=chosenNames[idx]
        hundoStudents.insert(i,ID)
        
for x in range(1,len(hundoStudents)):
    str1=hundoStudents[-x]
    str_length=len(str1)+(13-len(hundoStudents[-x]))
    str1=str1.ljust(str_length)
    print(str1 + "  -  "+ str(int(numHundos[-x])) + " hundos")
    
"""
   