# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 13:43:11 2020

@author: curti
"""
studentNNames=[]
studentIDs=[]
studentNames=[]
studentList=[]
quizIDs=[]
quizList=[]


with  open('nicknames.csv', 'r') as fin:
    text=(fin.readlines()) #read schoology .csv into python
    categories=text.pop(0).split(",") #pop the categories line

for x in range(len(text)): #iterate through all the quiz scores to be added
    text[x]=text[x].split(",")
    studentNNames.append(text[x][0:4])
    
    
with  open('nicknames_per4.csv', 'r') as fin:
    text=(fin.readlines()) #read schoology .csv into python
    categories=text.pop(0).split(",") #pop the categories line
    
for x in range(len(text)): #iterate through all the quiz scores to be added
    text[x]=text[x].split(",")
    studentNNames.append(text[x][0:4])

    