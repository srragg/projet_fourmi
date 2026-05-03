from ant import Ant  # Importe la classe Ant depuis ant.py


from tkinter import *
import tkinter as tk
import random

#creer la fenetre

fenetre = Tk()     
fenetre.geometry('400x400')
fenetre.title('La Fourmi de Langton')
fenetre['bg']= 'white'
fenetre.resizable(height= True, width= True)



# dimensions de la grille (en nombre de cases)
rows = 30  # nombre de lignes
cols = 30 # nombre de colonnes
taille_case = 15

# Variables globales
grille = []
fourmi = None  # Stocke la fourmi (ant)
animation_en_cours = False  # Pour gérer l'animation
vitesse = 100  #Pouvoir modifier la vitesse de passage des étapes.

#Fonction pour créer une grille aléatoire

def creer_grille_aleatoire():
    return [[random.choice(["blanc", "noir"]) for _ in range(cols)] for _ in range(rows)]

# Fonction pour dessiner la grille
def dessiner_grille():
    
    canevas.delete("all")  # Efface tout avant de redessiner
    for i in range(rows):
        for j in range(cols):
            x1, y1 = j * taille_case, i * taille_case
            x2, y2 = x1 + taille_case, y1 + taille_case
            couleur = "black" if grille[i][j] == "noir" else "white"
            canevas.create_rectangle(x1, y1, x2, y2, fill=couleur, outline="black")
    # Dessiner la fourmi (si elle existe)
    if fourmi:
        fourmi.draw()


def nouvelle_grille():
    global fourmi, grille, animation_en_cours
    
    animation_en_cours = False  # stop animation
    
    grille = creer_grille_aleatoire()

    
    fourmi = Ant(
        pos=[rows // 2, cols // 2],
        screen=canevas,
        size=taille_case,
        height=rows * taille_case,
        width=cols * taille_case,
        matrice=grille)
    dessiner_grille()

    bouton_animation.config(text="Démarrer")
    


def avancer_fourmi():
    if fourmi and animation_en_cours:
        fourmi.move()  # Utilise TA méthode move() de ant.py
        dessiner_grille()  # Redessine la grille et la fourmi
        fenetre.after(vitesse, avancer_fourmi)  # Animation


def basculer_animation():
    global animation_en_cours
    animation_en_cours = not animation_en_cours
    if animation_en_cours:
        avancer_fourmi()
    bouton_animation.config(text="Arrêter" if animation_en_cours else "Démarrer")





# Création du canevas
canevas = tk.Canvas(fenetre, width=cols*taille_case, height=rows*taille_case, bg="white")
canevas.pack()

# Bouton pour regénérer une nouvelle grille aléatoire
bouton = tk.Button(fenetre, text="Nouvelle grille", command=nouvelle_grille)
bouton.pack()


bouton_animation = tk.Button(fenetre, text="Démarrer", command=basculer_animation)
bouton_animation.pack(side=tk.RIGHT, padx=10)

grille = creer_grille_aleatoire()
fourmi = Ant(  # Crée TA fourmi avec TES paramètres
    pos=[rows // 2, cols // 2],  # Position centrale
    screen=canevas,
    size=taille_case,
    height=rows * taille_case,
    width=cols * taille_case,
    matrice=grille)
dessiner_grille()


fenetre.mainloop()










































# # # Parametres du quadrillage

# # nb_lignes = 20
# # nb_colonnes = 20
# # taille_case = 25


# # # Creer le quadrillage : ici on stock la couleur de chaque case (0= blanc) : initialisation du quabrillage en blanc

# # grille = []
# # for ligne in range (nb_lignes):
# #     lignes_etats = []
# #     for colonne in range (nb_colonnes):
# #         lignes_etats.append(0)
# #     grille.append(lignes_etats)

# # # la grille doit maintenant stoker les boutons qui sont actuellement vides

# # boutons = []
# # for ligne in range (nb_lignes):
# #     ligne_boutons = []
# #     for colonne in range (nb_colonnes):
# #         ligne_boutons.append(None)
# #     boutons.append(ligne_boutons)

# # # Fonction click qui va changer la couleur de la case ( 0 = blanc, 1 = noir )

# # def click (ligne, colonne):
# #     if grille[ligne][colonne] == 0 :
# #         grille[ligne][colonne] = 1
# #         boutons[ligne][colonne].config(bg = 'black')
# #     else :
# #         grille[ligne][colonne] == 0
# #         grille[ligne][colonne].config(bg = 'white')

# # # Créer tous les boutons dans la grille

# # for ligne in range (nb_lignes):
# #     for colonne in range(nb_colonnes):
# #         bouton = tk.Button(fenetre, width = 2, height = 1, bg = 'white', command = lambda l=ligne, c=colonne : click(l,c))

# #         bouton.grid(row=ligne, column=colonne)
# #         boutons[ligne][colonne] = bouton





# # # Direction de la fourmi


# # # 0 = haut, 1 = droite, 2 = bas, 3 = gauche

# # fourmi_direction = 0


# # #FONCTION POUR UNE ÉTAPE DE LA FOURMI

# # def etape_fourmi():
# #     global fourmi_ligne, fourmi_col, fourmi_direction
    
# #     # Étape 1 : Tourner
# #     if couleur_actuelle == 0:
# #         # Case blanche : tourner à droite
# #         fourmi_direction = (fourmi_direction + 1) % 4
# #     else:
# #         # Case noire : tourner à gauche
# #         fourmi_direction = (fourmi_direction - 1) % 4
    
# #     # Étape 2 : Inverser la couleur de la case
# #     inverser_case(fourmi_ligne, fourmi_col)
    
# #     # Étape 3 : Avancer d'une case
# #     if fourmi_direction == 0: # Haut
# #         fourmi_ligne = fourmi_ligne - 1
    
# #     elif fourmi_direction == 1: # Droite
# #         fourmi_col = fourmi_col + 1
    
# #     elif fourmi_direction == 2: # Bas
# #         fourmi_ligne = fourmi_ligne + 1
    
# #     elif fourmi_direction == 3: # Gauche
# #         fourmi_col = fourmi_col - 1






# import tkinter as tk
# import random

# # Dimensions de la grille
# rows = 10  # nombre de lignes
# cols = 10  # nombre de colonnes
# taille_case = 30  # taille d'une case en pixels

# # Fonction pour créer une grille aléatoire
# def creer_grille_aleatoire():
#     return [[random.choice(["blanc", "noir"]) for _ in range(cols)] for _ in range(rows)]

# # Fonction pour dessiner la grille
# def dessiner_grille():
#     grille = creer_grille_aleatoire()
#     canevas.delete("all")  # Efface tout avant de redessiner
#     for i in range(rows):
#         for j in range(cols):
#             x1, y1 = j * taille_case, i * taille_case
#             x2, y2 = x1 + taille_case, y1 + taille_case
#             couleur = "black" if grille[i][j] == "noir" else "white"
#             canevas.create_rectangle(x1, y1, x2, y2, fill=couleur, outline="gray")

# # Création de la fenêtre
# fenetre = tk.Tk()
# fenetre.title("Grille aléatoire - Fourmi de Langton")

# # Création du canevas
# canevas = tk.Canvas(fenetre, width=cols*taille_case, height=rows*taille_case, bg="white")
# canevas.pack()

# # Bouton pour regénérer une nouvelle grille aléatoire
# bouton = tk.Button(fenetre, text="Nouvelle grille", command=dessiner_grille)
# bouton.pack()

# # Dessiner la première grille au lancement
# dessiner_grille()

# Lancer la boucle principale de la fenêtre
# fenetre.mainloop()















































# Taille de la grille
# TAILLE_GRILLE = 10
# TAILLE_CASE = 35  # Taille de chaque case en pixels

# # Créer un frame pour contenir la grille
# frame_grille = tk.Frame(fenetre)
# frame_grille.pack()

# # Créer un Canvas de 400x400 pixels
# canvas = tk.Canvas(fenetre, width=400, height=400, bg="white")
# canvas.pack()

# Créer un Canvas de la taille de la grille
# largeur = TAILLE_GRILLE * TAILLE_CASE
# hauteur = TAILLE_GRILLE * TAILLE_CASE
# canvas = tk.Canvas(fenetre, width=largeur, height=hauteur, bg="white")
# canvas.pack()


# Dessiner la grille      
# for i in range(TAILLE_GRILLE + 1):  # +1 pour inclure la dernière ligne/colonne
#     # Dessiner les lignes horizontales
#     canvas.create_line(0, i * TAILLE_CASE, TAILLE_GRILLE * TAILLE_CASE, i * TAILLE_CASE, fill="black")
#     # Dessiner les lignes verticales
#     canvas.create_line(i * TAILLE_CASE, 0, i * TAILLE_CASE, TAILLE_GRILLE * TAILLE_CASE, fill="black")



# # Dessiner la grille     2
# for ligne in range(TAILLE_GRILLE):
#     for colonne in range(TAILLE_GRILLE):
#         # Calculer les coordonnées du rectangle
#         x1 = colonne * TAILLE_CASE
#         y1 = ligne * TAILLE_CASE
#         x2 = x1 + TAILLE_CASE
#         y2 = y1 + TAILLE_CASE
#         # Dessiner le rectangle
#         canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="white")


