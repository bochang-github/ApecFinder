# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 11:33:05 2019

@author: CHANG
"""


import pandas as pd

apecdata = pd.read_csv("test2.csv",sep="*")
print(apecdata.head())
exp = pd.read_csv("nomenclature_experience.csv",sep="*")
dom = pd.read_csv("nomenclature_domaine.csv",sep="*")

#apecdata['nom_experience'] = apecdata['experience'].map(exp.set_index('id')['experience']) #https://stackoverflow.com/questions/46211967/pandas-add-column-from-one-dataframe-to-another-based-on-a-join
#apecdata['nom_domaine'] = apecdata['domaine'].map(dom.set_index('id')['domaine'])

apecdata.insert(loc = 8,column = 'nom_experience' , value = apecdata['experience'].map(exp.set_index('id')['experience']))
apecdata.insert(loc=9,column = 'nom_domaine', value = apecdata['domaine'].map(dom.set_index('id')['domaine']))

def number(n):
#    m = re.findall(r'\d+', n)
    m = [int(s) for s in n.split() if s.isdigit()] #https://stackoverflow.com/questions/4289331/how-to-extract-numbers-from-a-string-in-python
    try:
        return(m[0])
    except IndexError:
        return(0)
    

#apecdata['nom_salaire'] = apecdata['salaire'].apply(number)
apecdata.insert(loc=10,column = 'nom_salaire',value = apecdata['salaire'].apply(number))
apecdata.to_csv('test3.csv', index=False, sep='*', encoding='utf-8-sig')
