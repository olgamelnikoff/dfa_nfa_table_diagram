from graphviz import Digraph
from texttable import Texttable
import json
import graphviz
import pydot
import re
import os

def inputToRawTable ():
    #Creating a class for a diagram
    dot = Digraph()
    
    print('Are you going to enter a table for DFA or NFA? Please type DFA or NFA.')
    typeOfFA = input()
    
    if (typeOfFA != 'DFA' and typeOfFA != 'NFA'):
        print('Incorrect input. Exiting program.')
        exit()

    table = []
    
    print('Please enter the alphabet symbols in your alphabet separated by white spaces.')
    alphabetInput = input()
    alphabetInput = alphabetInput.split()

    #Creating an array of alphabet symbols
    alphabetArray = []

    numOfAlphSymb = len(alphabetInput)
    for i in range(numOfAlphSymb):
        alphabetArray.append(alphabetInput[i])
    
    #Creating the first row of the table consisting of one white space and all the alphabet symbols.
    firstRow = []
    firstRow.append(' ')
    for i in range (numOfAlphSymb):
        firstRow.append(alphabetInput[i])

    table.append(firstRow)
    
    #Prompting the user to enter all the states
    print('Please enter the states separated by white spaces. They are your table row names.')
    statesInput = input()
    statesInput = statesInput.split()
    numOfInputStates = len(statesInput)

    #Prompting the user to enter the start state
    print('Please enter the start state out of the list you entered.')
    startState = input()

    #Prompting the user to enter the accepting state / states
    print('Please enter the accepting state or states out of the list you entered.')
    print('If there are several accepting states, separate them by white spaces.')
    acceptingStates = input()

    #For each state, creating a node in the diagram and a row in the table
    updatedStatesInput = []
    for i in range(numOfInputStates):
        if ((startState == statesInput[i]) and (startState in acceptingStates)):
            dot.node('Fake', 'q', style = 'invisible')
            dot.edge('Fake', startState, style = 'bold')
            dot.node(startState, startState, root = 'true', shape = 'doublecircle')
            updatedStatesInput.append('->*' + statesInput[i])
        elif (startState == statesInput[i]):
            dot.node('Fake', 'q', style = 'invisible')
            dot.edge('Fake', startState, style = 'bold')
            dot.node(startState, startState, root = 'true')
            updatedStatesInput.append('->' + statesInput[i])
        elif (statesInput[i] in acceptingStates):
            dot.node(statesInput[i], statesInput[i], shape = 'doublecircle')
            updatedStatesInput.append('*' + statesInput[i])
        else:
            dot.node(statesInput[i], statesInput[i])
            updatedStatesInput.append(statesInput[i])

    #Prompting the user to fill out the table.
    #The user is asked to fill out one cell at a time.
    # In parallel, the edges of the graph and their labels are created on the diagram. 
    for i in range (numOfInputStates):
        print('Entering input for row '+ str(updatedStatesInput[i]) + '.')
        localList = []
        localList.append(updatedStatesInput[i])
        for j in range(numOfAlphSymb):
            print('Please enter an input for alphabetical symbol '+ str(alphabetArray[j]) + '.')
            print('If there are several states for one cell, separate them by commas.')
            print('If there are no states in the cell, indicate it by 0')
            localInput = input()
            if (typeOfFA == 'DFA'):
                localList.append(localInput)
            else:
                localList.append('{' + localInput + '}')
            if (',' in localInput):
                state_list = []
                state_list = localInput.split(',')
                for k in range(len(state_list)):
                    dot.edge(str(statesInput[i]), state_list[k], label = str(alphabetArray[j]))
            elif (localInput != '0'):
                dot.edge(str(statesInput[i]), localInput, label = str(alphabetArray[j]))
        table.append(localList) 

    #Showing the entered information to the user in a tabular form. 
    #The user is prompted to answer "Yes" if the table is correct.
    t = Texttable()
    t.add_rows(table)
    print(t.draw())
    
    print('Here is the table constructed based on your input. Is it correct? Type Yes or No.')
    answer = input()

    if (answer == 'Yes'):
        print("The diagram has been output as a PDF file.")
    else:
        print('Table incorrect. Exiting program.')
        exit()

    #Outputting the FA diagram using the render() method
    return dot.render('FA_diagram.gv', view=True)  # doctest: +SKIP
    

 #main
var = inputToRawTable()
print(var)    