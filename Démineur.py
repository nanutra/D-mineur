import random

#matrice qui possède les bombes
matrice= [[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0]]

#la matrice affichée
Afficher = [ ['☐','☐','☐','☐','☐','☐','☐','☐','☐'],
['☐','☐','☐','☐','☐','☐','☐','☐','☐'],
['☐','☐','☐','☐','☐','☐','☐','☐','☐'],
['☐','☐','☐','☐','☐','☐','☐','☐','☐'],
['☐','☐','☐','☐','☐','☐','☐','☐','☐'],
['☐','☐','☐','☐','☐','☐','☐','☐','☐'],
['☐','☐','☐','☐','☐','☐','☐','☐','☐'],
['☐','☐','☐','☐','☐','☐','☐','☐','☐'],
['☐','☐','☐','☐','☐','☐','☐','☐','☐'] ]

#AjoutCase ajoute un +1 autour des cases d'une bombe
#pas de return, pas de print
def AjoutCase(liste, lig, col):

  if(lig-1>=0):
    if(liste[lig-1][col] !='b'):  #marche
      liste[lig-1][col] += 1

  if(lig-1>=0 and col-1>=0):   # marche
    if(liste[lig-1][col-1] !='b'):
      liste[lig-1][col-1] += 1
    
  if(col-1>=0):  
    if(liste[lig][col-1] !='b'): #marche
      liste[lig][col-1] += 1

  if(lig+1 <9 and col-1>=0):   # marche
    if(liste[lig+1][col-1] !='b'):
      liste[lig+1][col-1] += 1

  if(lig+1 < 9):
    if(liste[lig+1][col] !='b'):  #marche
      liste[lig+1][col] += 1

  if(lig+1 <9 and col+1<9):   # marche
    if(liste[lig+1][col+1] !='b'):
      liste[lig+1][col+1] += 1

  if(col+1<9):  
    if(liste[lig][col+1] !='b'): #marche
      liste[lig][col+1] += 1

  if(lig-1 >=0 and col+1<9):   # marche
    if(liste[lig-1][col+1] !='b'):
      liste[lig-1][col+1] += 1


#changer la valeur des cases par 0 autour du 0 choisi
#ne return pas, print pas
def Afficher0(liste2, lig2, col2, correction):

  if(lig2-1 >=0 ):
    if(liste2[lig2-1][col2] == 0):
      correction[lig2-1][col2] = 0



  if(lig2-1>=0 and col2-1>=0):     #marche
    if(liste2[lig2-1][col2-1] == 0):
      correction[lig2-1][col2-1] = 0
      
  if(col2-1>=0):  
    if(liste2[lig2][col2-1] == 0):  #marche
      correction[lig2][col2-1] = 0

  if(lig2+1 <9 and col2-1>=0):     # marche
    if(liste2[lig2+1][col2-1] == 0):
      correction[lig2+1][col2-1] = 0

  if(lig2+1 < 9):
    if(liste2[lig2+1][col2] == 0):  #marche
      correction[lig2+1][col2] = 0

  if(lig2+1 <9 and col2+1<9):      # marche
    if(liste2[lig2+1][col2+1] == 0):
      correction[lig2+1][col2+1] = 0

  if(col2+1<9):  
    if(liste2[lig2][col2+1] == 0):  #marche
      correction[lig2][col2+1] = 0


  if(lig2-1 >=0 and col2+1<9):     # marche
    if(liste2[lig2-1][col2+1] == 0):
      correction[lig2-1][col2+1] = 0


x=0
nbB =0
#Entrer le nombre de bombes que l'on veut dans le jeu
while nbB != 1:
  nbBombe = int(input("entrez le nombre de bombes:"))
  if( nbBombe<1 or nbBombe>80):
    print("Désolé c'est impossible met plutôt entre 1 et 80 !")
    nbBombe = int(input("entrez le nombre de bombes(conseillé entre 10 et 15) :"))
  else:
    nbB = 1

#cette boucle while sert a changer la valeurs des 0 par des bombes
while x < nbBombe:

    ligne = random.randint(0, 8)
    colonne= random.randint(0,8)

    if(matrice[ligne][colonne] != 'b'):
      matrice[ligne][colonne] ='b'
      AjoutCase(matrice, ligne, colonne)
      x = x + 1 


choixAffichageMatrice = False
#le but est d'afficher la grille des bombes pour faciliter le codage
#si un non est rentré la grille ne s'affichera pas
while choixAffichageMatrice != True:
  OuiOuNon = input("ModeTest(Afficher l'emplacement des bombes : oui ou non ?")
  if(OuiOuNon == "oui"):
    print("   1 2 3 4 5 6 7 8 9")
    print("                    ")
    for i in range(0,9):
      print(i+1, end="  ")
      for y in range(0,9):
        print(matrice[i][y], end=" ")
      print("")
    choixAffichageMatrice= True
  if(OuiOuNon == "non"):
    choixAffichageMatrice= True


print("")

#Afficher la matrice a afficher avant de jouer
for i in range(0,9):
  print(i+1, end="  ")
  for y in range(0,9):
    print(Afficher[i][y], end=" ")
  print("")

gameOver = False   #initialisation du game over

u = 0 
nbDeCoupsVictoires= 81 - x  #nbDeCoupsVictoires définit le nombre de coups pour gagner
print(nbDeCoupsVictoires)


# définition des regles du jeu
#mise en place du gameover
while gameOver == False:
  while u != nbDeCoupsVictoires:
    colonne1 = int(input("choisissez votre colonne :"))-1
    ligne1 = int(input("choisissez votre ligne :"))-1

    if( ligne1>8 or ligne1 <0): #si valeur de ligne incorecte = réécrire ligne
      print("met une valeur etre 1 et 9!")
      ligne1 = int(input("choisissez votre ligne :"))-1

    if(colonne1>8 or colonne1 <0):  #si valeur de colonne incorrecte = réécrire colonne
      print("met une valeur etre 1 et 9!")
      colonne1 = int(input("choisissez votre colonne :"))-1
    
    else: #si valeur juste if en fonction de si c'est une bombe ou pas

      if matrice[ligne1][colonne1] == "b": #si bombe= perdu
        print("Perdu !!")
        gameOver = True

      if matrice[ligne1][colonne1] == 0: #si un 0 lancer la fonction Afficher0
          Afficher[ligne1][colonne1]=matrice[ligne1][colonne1]
          Afficher0(matrice, ligne1, colonne1, Afficher)
          
          #print la nouvelle matrice
          print("   1 2 3 4 5 6 7 8 9")
          for i in range(0,9):
            print(i+1, end="  ")

            for y in range(0,9):
              print(Afficher[i][y], end=" ")
            print("")
          u +=1

      else: #Si autre que 0 et b juste afficher la valeur
        Afficher[ligne1][colonne1]=matrice[ligne1][colonne1]
        #print la nouvelle matrice
        print("   1 2 3 4 5 6 7 8 9")
        for i in range(0,9):
          print(i+1, end="  ")
          for y in range(0,9):
            print(Afficher[i][y], end=" ")
          print("")
        u +=1
  if(u == nbDeCoupsVictoires):
    print("let's gooo t'as gagné !!")
    gameOver = True
