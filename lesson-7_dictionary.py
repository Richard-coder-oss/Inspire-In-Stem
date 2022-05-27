#python is a scripting language/ loosely type language/ strongly typed language
#in python; interpreter understands line by line: Goes through the code line by line
#variables are used to store your data e.g  f num = 4
#!usr/bin/python

####################
#      Dictionaries
#      Name : Richard Miruka
#      Date : 24/5/2022

################
#Key value pairs are a set of value associated with each other
#Initializing Dictionaries
student = {"Name": "Bob", "age": "24", "gender":"male"}
#print (student["Name"])
#print (student["age"])
#print (student["gender"])

#adding key value pairs to your dictionary
student["id-no"]= "33469730"
student ["Hobby"]= "reading"
student ["club"]= "Man-united"
student ["school"]= "Jkuat"
#print(student)
student= {} # Initializing an empty dictionary
student ["fav_food"]="chapati"
student ["home_city"]= "Nairobi"
#print(student)
#modifying values
student["Name"]="Richard"
#print(student)
#removing key pair values
del student["home_city"]
print(student)