# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 14:16:18 2020

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

Ancestor = "Benny"

AncestorPerson = family.find_person(Ancestor)
AncestorsOffspring = [AncestorPerson]
OldGen = [AncestorPerson]
Spouses = []

while OldGen:
    NewGen = []
    for p in OldGen:
        print(p.name)
        CurrentSpouses = []
        for h in p.households:
            NewGen.extend(h.kids)
            CurrentSpouses.extend(h.parents)
            CurrentSpouses.remove(p)
        Spouses.extend(CurrentSpouses)
        for i in CurrentSpouses:
            print(i.name)
    AncestorsOffspring.extend(NewGen)
    OldGen = NewGen
