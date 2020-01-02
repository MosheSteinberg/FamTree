# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 18:47:27 2019

@author: MS13
"""
import os
import familytreemaker as ftm

os.chdir(r'C:\Users\MS13\Desktop\Personal\familytreemaker-master')

family = ftm.Family()

# Populate the family
f = open('SteinbergFamily.txt', 'r', encoding='utf-8')
family.populate(f)
f.close()

List = []
SubList = []
DictOfEveryone = family.everybody
ListOfEveryone = [v for v in DictOfEveryone.values()]
# this goes up the list of fathers for everyone
for i in ListOfEveryone:
    j=i
    while len(j.parents)>0:
        SubList.append(j)
        j=j.parents[0]
    List.append(SubList)
    SubList=[]
    
List2 = []
SubList2 = []

for i in ListOfEveryone:
    j=[i]
    SubList2 = []
    while len(j)>0:
        jparents=[]
        for k in j:
            jparents.extend(k.parents)
        j=jparents
        SubList2.append(j)
    List2.append(SubList2)
    
ListNames = []
Sub1 = []
Sub2 = []
for i in List2:
    for j in i:
        for k in j:
            Sub2.append(k.name)
        Sub1.append(Sub2)
        Sub2 = []
    ListNames.append(Sub1)
    Sub1=[]
    
NoRents = []
for i in List2:
    NoRents.append(len(i))

MaxNoRents = max(NoRents)

Generations = {}
Generations[str(MaxNoRents)] = [ListOfEveryone[i] for i,x in enumerate(NoRents) if x==MaxNoRents]
GenerationNames = {}
GenerationNames[str(MaxNoRents)] = [ListOfEveryone[i].name for i,x in enumerate(NoRents) if x==MaxNoRents]
    
for i in range(MaxNoRents - 1, 0, -1):
    ListOfPeople = []
    for j in Generations[str(i+1)]:
        ListOfPeople.extend(j.parents)
    uniqueList = []
    for x in ListOfPeople:
        if x not in uniqueList:
            uniqueList.append(x)
    Generations[str(i)] = uniqueList
    GenerationNames[str(i)] = [i.name for i in uniqueList]

FirstPerson = ListOfEveryone[0]
FirstPerson.attr["gen"] = 0
ToDo = [FirstPerson] # consider setting to list of everyone, problem as no gen set yet
Done = []
Gens ={0:[FirstPerson]}
#BE AWARE COULD GO DOWN RABBIT HOLE AND TODO ENDS EARLY
while ToDo:
    #pick out current person
    CurrentPerson = ToDo[0]
    #get their generation, should already be filled out
    CurrentGen = CurrentPerson.attr["gen"]
    #remove current person from to do
    ToDo.remove(CurrentPerson)
    #add person to done
    Done.append(CurrentPerson)
    #get parents
    CurrentParents = CurrentPerson.parents
    #get kids
    CurrentKids = []
    CurrentSpouses = []
    for househ in CurrentPerson.households:
        CurrentKids.extend(househ.kids)
        CurrentSpouses.extend(househ.parents)
        CurrentSpouses.remove(CurrentPerson)
    #for all parents, add to to do if not done
    for pers in CurrentParents:
        if pers not in Done:
            ToDo.append(pers)
            pers.attr["gen"] = CurrentGen + 1
            if Gens.get(pers.attr["gen"]):
                Gens[pers.attr["gen"]].append(pers)
            else:
                Gens[pers.attr["gen"]] = [pers]
    for pers in CurrentKids:
        if pers not in Done:
            ToDo.append(pers)
            pers.attr["gen"] = CurrentGen - 1
            if Gens.get(pers.attr["gen"]):
                Gens[pers.attr["gen"]].append(pers)
            else:
                Gens[pers.attr["gen"]] = [pers]
    for pers in CurrentSpouses:
        if pers not in Done:
            ToDo.append(pers)
            pers.attr["gen"] = CurrentGen
            if Gens.get(pers.attr["gen"]):
                Gens[pers.attr["gen"]].append(pers)
            else:
                Gens[pers.attr["gen"]] = [pers]    
GensNames ={}
for i in Gens.keys():
    uniqueList2 = []
    for j in Gens[i]:
        if j not in uniqueList2:
            uniqueList2.append(j)
    Gens[i] = uniqueList2
    GensNames[i] = [pers.name for pers in uniqueList2]
    
#checks
print('In tree: ' + str(sum([len(i) for i in Gens.values()])))
print('Input people: ' + str(len(ListOfEveryone)))
#for z in [i for i,x in enumerate(NoRents) if x==max(NoRents)]: #loop through people in bottom gen
#    ListOfEveryone[z].attr["gen"] = max(NoRents) + 1

#so now we have number of rents
#need to build bottom up
#take everyone with max number of rents and look at their parents 
#that way, form generations
#use preexisting functions to do the rest
#might need to understand the main code in greater detail:
#objects:
#person - name, parents