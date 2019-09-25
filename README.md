# projet_apecsearcher 

# Description

Apecsearcher est une application codée en Python qui cherche et parse les offres d'emploi du site APEC, enfin de stocker les données dans une fiche csv. A partir de ces données, l'application peut générer des rapports de visualisation en fonction de salaire proposé, nombre des offres publiés et localisation d'entreprise. Ces rapports peuvent nous aider de trouver les offres d'emploi correspondants à nos attente.

Le seconde but de cette application est de filtrer les mots clés des offre d'emplois respectivement sur le profil cherché, la présentation d'entreprise et la description du poste. Ces mots clés peuvent nous aider à la mise à jour du CV et la préparation de l'entretien. 

# Pourquoi ce projet ?
Je pense à changer mon travail d'après une formation de Python depuis Mai. Chercher du premier travail dans le domaine d'informatique est tout nouveau pour les personnes comme moi. Des Centaines d'offres sont publiés sur site tous les jours  lors que les offres intéressantes sont noyées parmi les offres de SSII. Il faut s'inscrire pour enregistrer ses recherches avancées et les offres préférées.  La premier raison était de pouvoir rechercher du travail à votre place pendant que vous regardez les vidéos sur internet.  Ensuite j'ai commencé à préparer mon CV mais je ne sais pas de quel domaine et quel entreprise à évider. Aussi je me pose des questions sur lesquelles compétences ou expériences attirer les recruteurs. Voilà pourquoi je fais cette base de donnée pour répondre à ces question!

Je voulais changer le travail pour la raison de motivation. Comme je suis débutant dans le domaine de data d'analyse, je ne sais pas sur quoi à m'orienter. j'ai besoin une base de données de ce marché à jour pour me répondre des questions suivantes:
	○ Quelles  entreprises, proche de chez moi, cherchent des ingénieur data niveau débutant avec salaire élevé.
	○ Quels domaines ont la bonne rentabilité et durabilité selon son nombre des candidatures recherchés et le salaire moyen par rapport le   niveau d'expérience demandé (débutant, junior, senior, expérimenté)
	○ Comment entre dans ces domaines et entreprises? Filtrer les mot clé des profil cherché, présentation d'entreprise et description du poste

# Etat du projet
Le développement du ApecSearcher est en cours. Il manques beaucoup de fonctionnalités. Une interface sera nécessaire à créer pour le saisie des recherches avancées. La recherches des liens url des offres devrait plus intelligente. J'aimerais aussi établir une "black liste" pour bloquer les sociétés qu'on veut pas y aller. Un outil de base de données au lieu de csv sera plus stable pour la gestion des données. Dans le moyen terme, j'aimerais que les offres venant des autre plateformes (Monster, Linkedin, Keljob, etc.) pourront être intégrées dans l'application. Le API Openstreetmap pourrait être utilisé pour localiser les offres sur la carte.  

# Pour tester JobSearcher
Package utilisé: python.Requests,  python.BeautifulSoup, python.Json
