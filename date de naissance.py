#créez un programme demandant à un utilisateur d'entrer sa date de fête 
# et retournez-lui sa saison de naissance s'il est né dans l'hémisphère Nord. 
# (Vous pouvez assumer que les équinoxes et solstices ont lieu le 21 du mois.)


def saison():
    jour_naissance=int(input("Entrer votre jour de naissnace en chiffre :"))
    mois_naissance=int(input("Entrer votre mois de naissnace en chiffre :"))
    
    if mois_naissance==1 or mois_naissance==2 or (mois_naissance==12 and jour_naissance>=21) or (mois_naissance==3 and jour_naissance<21):
        print("vous etes né en hiver")
    if mois_naissance==4 or mois_naissance==5 or (mois_naissance==3 and jour_naissance>=21) or (mois_naissance==6 and jour_naissance<21):
        print("vous etes né au printemps")
    if mois_naissance==7 or mois_naissance==8 or (mois_naissance==6 and jour_naissance>=21) or (mois_naissance==9 and jour_naissance<21): 
        print("vous etes né été")
    if mois_naissance==10 or mois_naissance==11 or (mois_naissance==9 and jour_naissance>=21) or (mois_naissance==12 and jour_naissance<21):
        print("vous etes né em automne")
    return None

saison()