#!/usr/bin/python

# this script writes out reversible Michaelis-Menten equations
import sys
import random

# sys.argv[0] is the name of the py file
reactants = sys.argv[1] # should be a string
products = sys.argv[2] # should be a string

reactantsList = reactants.split(" + ")
productsList = products.split(" + ")

def randomConstant():
	return str(round(random.uniform(0,1), 4))

def isEmpty(testList):
	for ele in testList:
		if ele.strip(): # if list is not empty
			return False
	return True # if list is empty

def addMetabolites(listOfMetabolites):
	species = ''

	for m in listOfMetabolites: 
		# split m by space
		addend = m.split(" ")
		addend = [i for i in addend if i]
		
		if len(addend) > 1: # if there is a coefficient
			if addend[0] == '$':
				metabolite = addend[1]
				species += "(" + metabolite + ")"
			else: 
				power = addend[0]
				metabolite = addend[1]
				species += "(pow((" + metabolite + ")," + str(power) + "))"
		else: 
			metabolite = addend[0]
			species += "(" + metabolite + ")"
		
	return species

if isEmpty(reactantsList): # if reactantsList is empty
	print("I am empty")
	parString = None

else: 
	Km1 = randomConstant()
	parString = "e * " + randomConstant() + "/" + Km1 + " * ("
	parString = parString + addMetabolites(reactantsList)

	if not isEmpty(productsList): #
		parString = parString + " - " + addMetabolites(productsList) + " / " + randomConstant()
	

	parString =  parString + ")/(1 + " + addMetabolites(reactantsList) + " / " + Km1

	if not isEmpty(productsList): # if reactantsList is empty
		parString =parString +  " + " + addMetabolites(productsList) + " / " + randomConstant() ###########HERE IS THE WEIRD PART

	parString += ");"
	
# write rateLaw to file
rateLaw_file = open("rateLaws.list", "a") 
if parString:
	rateLaw_file.write(parString + '\n')
	# rateLaw_file.write("\n")
rateLaw_file.close() 