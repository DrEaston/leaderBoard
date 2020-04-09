# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 19:05:53 2020

@author: curti
"""

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

class Gradebook:
    def __init(self,gradebookName):
        self.name = gradebookName