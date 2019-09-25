# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 15:50:19 2019

@author: BC40966N
"""

import pandas as pd

nomenclature_exp = []

r = [{"codePresentation":"OFFRE_NIVEAU_EXPERIENCE","idNomenclature":200269,"idOrganisation":689179,"libelle":"Tous niveaux d'expérience acceptés","niveau":1,"ordre":1},{"codePresentation":"OFFRE_NIVEAU_EXPERIENCE","idNomenclature":597150,"idOrganisation":689180,"libelle":"Aucune expérience exigée","niveau":1,"ordre":2},{"codePresentation":"OFFRE_NIVEAU_EXPERIENCE","idNomenclature":597151,"idOrganisation":689181,"libelle":"Minimum 1 an","niveau":1,"ordre":3},{"codePresentation":"OFFRE_NIVEAU_EXPERIENCE","idNomenclature":597152,"idOrganisation":689182,"libelle":"Minimum 2 ans","niveau":1,"ordre":4},{"codePresentation":"OFFRE_NIVEAU_EXPERIENCE","idNomenclature":597153,"idOrganisation":689183,"libelle":"Minimum 3 ans","niveau":1,"ordre":5},{"codePresentation":"OFFRE_NIVEAU_EXPERIENCE","idNomenclature":597154,"idOrganisation":689184,"libelle":"Minimum 4 ans","niveau":1,"ordre":6},{"codePresentation":"OFFRE_NIVEAU_EXPERIENCE","idNomenclature":597155,"idOrganisation":689185,"libelle":"Minimum 5 ans","niveau":1,"ordre":7},{"codePresentation":"OFFRE_NIVEAU_EXPERIENCE","idNomenclature":597156,"idOrganisation":689186,"libelle":"Minimum 6 ans","niveau":1,"ordre":8},{"codePresentation":"OFFRE_NIVEAU_EXPERIENCE","idNomenclature":597157,"idOrganisation":689187,"libelle":"Minimum 7 ans","niveau":1,"ordre":9},{"codePresentation":"OFFRE_NIVEAU_EXPERIENCE","idNomenclature":597158,"idOrganisation":689188,"libelle":"Minimum 8 ans","niveau":1,"ordre":10},{"codePresentation":"OFFRE_NIVEAU_EXPERIENCE","idNomenclature":597159,"idOrganisation":689189,"libelle":"Minimum 9 ans","niveau":1,"ordre":11},{"codePresentation":"OFFRE_NIVEAU_EXPERIENCE","idNomenclature":597160,"idOrganisation":689190,"libelle":"Minimum 10 ans","niveau":1,"ordre":12}]

for item in r:
    ref = item["idNomenclature"]
    metier = item["libelle"]
    nomenclature_exp.append([ref, metier])
    
columns = ['id','experience']
df = pd.DataFrame(nomenclature_exp, columns=columns)
df.to_csv('nomenclature_experience', index=False, sep='*', encoding='utf-8-sig') 