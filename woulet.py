from random import randrange



  
nbre_ordi = randrange(1,500)#nbre_ordi
    
        
print("vous devez entrer un nombre compris entre 1 et 500.\n ")     
chance=5  
while  chance >=1 :
    nbre_utilisateur = int(input("Entrez un nombre: "))
    if nbre_utilisateur == nbre_ordi  :
        print("vous avez gagne")
        break
        
    else  :
        if nbre_utilisateur<nbre_ordi :
            print("Le nombre choisi est inferieur au nombre secret.")
            print("Entrez un nombre a nouveau.")
        
        else : 
            print("le nombre choisi est superieur au nombre secret.")
            print("Entrez un nombre a nouveau.")
            
    chance -= 1
    print("Nombre de chances restants: ",chance)
        
     
print("Le nombre de l'ordinateur etait:", nbre_ordi )   
 
 

    
    

        