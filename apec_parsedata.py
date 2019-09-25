# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 23:18:29 2019

@author: CHANG
"""

import requests
import pandas as pd
from bs4 import BeautifulSoup

#Read the URL 
html_tables = {}
text_file = open("link.txt", "r")

lines = text_file.read().split('\n')

for i,element in enumerate(lines):
    try:
        r = requests.get(lines[i])
        x = r.json()
        html_tables[element] = x

    except ValueError:  # includes simplejson.decoder.JSONDecodeError
        pass   # do nothing!

#Parser the URL and collect data in list parsed_news[]
parsed_news = []
for name, item in html_tables.items():
        try:
            html_ref = item["numeroOffre"]
        except KeyError:
            pass

        try:
            html_title = item["intitule"]
        except KeyError:
            pass        
        
        try:
            html_company = item["nomCompteEtablissement"]
        except KeyError:
            pass

        try:
            html_location = item["lieux"][0]['libelleLieu'] # slicing prefecture
        except KeyError:
            pass
        
        try:
            html_date_raw = item["datePublication"]
            html_date = html_date_raw[:10] # slicing date
        except KeyError:
            pass        
        
        try:
            html_salaire = item["salaireTexte"]
        except KeyError:
            pass
        
        try:
            html_experience = item["idNomNiveauExperience"]
        except KeyError:
            pass
        
        try:
            html_secteur = item["idNomSecteurActivite"]
        except KeyError:
            pass
        
        try:
            html_desription_raw = item["texteHtml"]
            html_desription = BeautifulSoup(html_desription_raw, "lxml").text.replace('\r\n',' ').replace('\n',' ') # remove HTML tag from string and remove '\n' or  '\r\n'
        except KeyError:
            pass
        
        try:
            html_profil_raw = item["texteHtmlProfil"]
            html_profil = BeautifulSoup(html_profil_raw,'lxml').text.replace('\r\n',' ').replace('\n',' ')  # remove HTML tag from string and remove \n
        except KeyError:
            pass
        
        try:
            html_entreprise_raw = item["texteHtmlEntreprise"]
            html_entreprise = BeautifulSoup(html_entreprise_raw, "lxml").text.replace('\r\n',' ').replace('\n',' ')  # remove HTML tag from string and remove \n
        except KeyError:
            pass
        parsed_news.append([name,html_ref,html_title,html_company,html_location,html_date,html_salaire,html_experience,html_secteur,html_desription,html_profil,html_entreprise])


#convert the list into dataframe and save as .csv
columns = ['filename','reference', 'title', 'company name', 'location', 'publication date', 'salaire','experience','domaine','job description','profil expected','presentation entreprise']

df = pd.DataFrame(parsed_news, columns=columns)
df.to_csv('test2.csv', index=False, sep='*', encoding='utf-8-sig') # utf-8-sig' worked for french accent, also 'utf-16'




 