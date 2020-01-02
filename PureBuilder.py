# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 16:28:36 2019

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


DictOfEveryone = family.everybody
ListOfEveryone = [v for v in DictOfEveryone.values()]


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
#print('In tree: ' + str(sum([len(i) for i in Gens.values()])))
#print('Input people: ' + str(len(ListOfEveryone)))

TopGen = max(Gens.keys())

print('digraph {\n' + \
      '\tnode [shape=box];\n' + \
      '\tedge [dir=none];\n')

for p in ListOfEveryone:
	print('\t' + p.graphviz() + ';')
print('')

for i in range(len(Gens.keys())):
    family.display_generation(Gens[TopGen - i])

print('}')