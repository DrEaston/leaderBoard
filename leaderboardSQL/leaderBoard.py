# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 20:17:17 2020

Curtis Easton

This is a program that takes a .csv file from schoology, and imports it into a Course object. Student info is 
stored in a list of Student Objects within a Course, including individual quiz scores. 

Within the Course class are some functions for calculating and printing high scores. 
"""
import bisect

chemQuizzes=['The Number of Neutrons (CO Pages 4-6)','Valence Electrons / Energy Levels (CO Pages 8-11)','Dot Diagrams and Charge (CO Pages 13-16)','Chemical Formulas (CO Page 18)','Ionic and Covalent Bonding (CO Pages 20-24)','Reactions1 Quiz','Reactions2 Quiz','Elephant Toothpaste Quiz','Protons Neutrons Electrons (CO Page 2)']
astrQuizzes=['1 - The Fusing of Elements Quiz','2 - Solar Nuclear Fusion Quiz','Electrons and Light Quiz','Where does light come from? - Quiz','The color of light - Quiz','Light and Scorpions - Quiz']
earthQuizzes=["Plate Tectonics 1 - Quiz","Plate Tectonics 2 - Quiz","Plate Tectonics 3 - Quiz","Convection Quiz","Earth's Crust Quiz","Earth's Mantle and Core Quiz","Earth's Spheres Quiz","Rainbows and Infrared Light","Earth's Atmosphere Quiz","Weather or Climate? - Videos - Quiz","Weather and Climate Reading Quiz","Wind and Solar Radiation Quiz"]
quantQuizzes=['Valence Electrons / Energy Levels (CO Pages 8-11)','Protons Neutrons Electrons (CO Page 2)','Electrons and Light Quiz','Where does light come from? - Quiz','The color of light - Quiz','Light and Scorpions - Quiz','Rainbows and Infrared Light','Invisible Sunlight Quiz']
categories=['score','astronomy','chemistry','noQuizzes','earthSci','hundos','quantPhys'] 

class Student:
    def __init__(self,ID,firstName,lastName):
        self.name = firstName + " " + lastName
        self.ID = ID
        self.score = 0
        self.quizzes = []
        self.quizNames =[]
        self.nickName =[]
        self.astronomy = 0
        self.chemistry = 0
        self.hundos = 0
        self.noQuizzes = 0
        self.earthSci = 0
        self.quantPhys = 0 

class scoreSheet:
    def __init__(self,filename):
        self.nickNames=[]
        self.studentIDs=[]
        self.studentNames=[]
        self.studentList=[]
        self.idsWithNickNames=[]
        self.chosenNames=[]
        self.toPrint = [] 
        
        #lists containing sorted scores, players
        self.hundos = []
        self.score = []
        self.astronomy=[]
        self.chemistry=[]
        self.noQuizzes=[]
        self.earthSci=[]
        self.quantPhys=[]
        #import data
        with  open(filename, 'r') as fin:
            text=(fin.readlines()) #read schoology .csv into python
            text.pop(0).split(",") #pop the categories line
        for x in range(len(text)): #iterate through all the quiz scores to be added
            text[x]=text[x].split(",") #change current data into list
            quizAttempt=text[x]
            for y in range(len(quizAttempt)): 
                quizAttempt[y]=quizAttempt[y].replace("\"","") 
            #create and update Student objects
            if quizAttempt[0] in self.studentIDs:  #if student is already added to studentList
                self.appendList(quizAttempt[0],quizAttempt[13],quizAttempt[10])
            else : #if student is not there, create student and add result
                self.createAppendList(quizAttempt[1],quizAttempt[2],quizAttempt[0],quizAttempt[13],quizAttempt[10])
                
    """ __init__ methods """                 
    def appendList(self,ID,quizScore,quizName): #add scores to existing student
            idx=self.studentIDs.index(ID) #get student index 
            self.addScore(idx,quizScore,quizName)
                   
    def createAppendList(self,firstName,lastName,ID,quizScore,quizName): #create new student and add scores
        self.studentNames.append(firstName + " " + lastName) #add student name to master list
        self.studentIDs.append(ID) # add student number to master list
        self.studentList.append(Student(ID,firstName,lastName)) #initialize and store student object
        self.addScore(-1,quizScore,quizName)
             
    def addScore(self,idx,quizScore,quizName): #called by __init__ methods above
        if (quizScore != ''): #if there is a quiz score
            self.studentList[idx].noQuizzes += 1 #increment number of quizzes taken
            self.studentList[idx].quizzes.append(float(quizScore)) #add score to list
            self.studentList[idx].quizNames.append(quizName) #add name of quiz to list
            self.studentList[idx].score+=float(quizScore) #update total score
            if quizName in chemQuizzes:
                self.studentList[idx].chemistry += float(quizScore)
            if quizName in astrQuizzes:
                self.studentList[idx].astronomy += float(quizScore)
            if quizName in earthQuizzes:
                self.studentList[idx].earthSci += float(quizScore)
            if quizName in quantQuizzes:
                self.studentList[idx].quantPhys += float(quizScore)
            if quizScore == '100':
                self.studentList[idx].hundos += 1
            
    """ user tools """
    def getStudent(self,firstname): #enter student firstname
        for element in self.studentList: #iterate through list of students
            if firstname in element.name:
                print ('get student: ' + element.name + '?')
                print("type y/n")
                result=input() #use user input to decide if correct student found
                if result == 'y': #if correct student found, edit student. else move to next student w/ same first name
                    return element
                    break
                
    def getStudentID(self,ID): #enter student firstname
        for element in self.studentList: #iterate through list of students
            if ID in element.ID:
                print(element.name)

    """ calculate stuff """  
    def getLeaders(self,category): # create list of leaders for attributes in input variables
        getattr(self,category).append([[],[]])
        for item in self.studentList:
            if (getattr(item,category)>0):
                item.ID=self.insertNickname(item.ID)
                self.insertScorePlayer(item.ID,getattr(item,category),getattr(self,category)[0])
    
    def getWeeklyLeaders(self,category):
        getattr(self,category).append([[],[]])
        current=getattr(intSci,category)[0]
        last=getattr(lastWeek,category)[0]
        for item in current[1]:
            idx=current[1].index(item)
            if item in last[1]:
                idx1=last[1].index(item)
                score=current[0][idx]-last[0][idx1]
            else:
                score=current[0][idx]
            self.insertScorePlayer(current[1][idx],score,getattr(self,category)[1])
           
                
    """ used by getLeaders """    #insert username/score into ordered list of leaders
    def insertScorePlayer (self,ID,score,highScores):
        
        i=bisect.bisect_right(highScores[0],float(score))
        highScores[0].insert(i,score)       
        highScores[1].insert(i,ID) 
        
    """ print stuff """           
    def printLeaders(self,category,numScores,weeks): #print leaderboard. "namesScores" is generated by "getLeaders" 
        if numScores=='all':  #numScores indicates how many scores to print. 'all' prints all leaders (those with scores)
            numScores=len(getattr(self,category)[0][0])
        for x in range(1,numScores+1): 
            toString=''
            for i in reversed(range(weeks)): #loop adds overall and weekly leaders into 1 toString
                if getattr(self,category)[i][0][-x]!=0:
                    str1=getattr(self,category)[i][1][-x]
                    str2=str(int(getattr(self,category)[i][0][-x]))
                    toString=f'{toString}{str1:15}  -   {str2:6}  '
                else:
                    toString="-"*23+6*" "
            print(toString)
        print("\n")
                    
    """ Nickname import/insert/edit/save """
    def importNicknames(self): #read in nicknames from file
        with  open('nickNamesList.txt', 'r') as fin:
            text=(fin.readlines()) #read schoology .csv into python
        for x in range(len(text)): #iterate through all the quiz scores to be added
            self.nickNames.append(text[x].rstrip('\n').split(",")) #change current data into list
        for item in self.nickNames:
            if item[0] != 'N/A':
                self.idsWithNickNames.append(item[3])
                self.chosenNames.append(item[0])
    
    def insertNickname(self,initID): #swap studentID for nickname. used by "insertScorePlayer"
        if initID in self.idsWithNickNames:
            idx=self.idsWithNickNames.index(initID)
            return self.chosenNames[idx]
        else:
            return initID

    def addNickname(self,firstname,nickName): #add new student nickname and save to file. called by user
        for element in self.nickNames:
            if element[1] == firstname: #use firstname to find student
                print("edit student: "+ firstname + " "+element[2]+"?") #display student last name
                print("type y/n")
                result=input() #use user input to decide if correct student found
                if result == 'y': #if correct student found, edit student. else move to next student w/ same first name
                    element[0]=nickName
                    self.writeNicknames()
                    break
    
    def writeNicknames(self): #write nicknames to file. used by "addNickname"
        writeStr=[]
        with open("nickNamesList.txt","w") as fout:
            for element in (self.nickNames):
                writeStr=element[0]
                for x in range(1,len(element)):
                    writeStr=writeStr+","+element[x]
                fout.write(writeStr)
                fout.write('\n')



# Import Data and Load into Course object     
intSci=scoreSheet('May4.csv')
intSci.importNicknames() 
lastWeek=scoreSheet('April28.csv')
lastWeek.importNicknames()  
   
for item in categories:
    intSci.getLeaders(item)
    lastWeek.getLeaders(item)
    intSci.getWeeklyLeaders(item)

""" Program Output """ 
print("The total points leaders are:\n")

print("\u0332".join("Week")+" "*25 +"\u0332".join("Overall"))
intSci.printLeaders('score',20,2)

print("The leaders for most Hundos (100% quizzes) are:\n")
print("\u0332".join("Week")+" "*25 +"\u0332".join("Overall"))
intSci.printLeaders('hundos',10,2)


print("The Chemistry points leaders are:\n")
print("\u0332".join("Week")+" "*25 +"\u0332".join("Overall"))
intSci.printLeaders('chemistry',10,2)

print("The Astronomy points leaders are:\n")
print("\u0332".join("Week")+" "*25 +"\u0332".join("Overall"))
intSci.printLeaders('astronomy',10,2)

print("Quiz warriors (Those with most quiz attempts) :\n")
print("\u0332".join("Week")+" "*25 +"\u0332".join("Overall"))
intSci.printLeaders('noQuizzes',10,2)

print("The leading earth scientists are:\n")
print("\u0332".join("Week")+" "*25 +"\u0332".join("Overall"))
intSci.printLeaders('earthSci',10,2)

print("The leading quantum physicists are:\n")
print("\u0332".join("Week")+" "*25 +"\u0332".join("Overall"))
intSci.printLeaders('quantPhys',10,2)



