import tkinter as tk
import random as r
import json
import os
from map import *
from ant import Ant
from menu import lancer_menu

# Fichier de sauvegarde de la partie
SAVE_FILE = "save.json"

# Vitesse d'animation en millisecondes
var_vitesse = 1000

def lancer_jeu(state=None):
    """
    Lance la fenêtre du jeu.
    Si 'state' est fourni (chargement d'une sauvegarde), restaure la matrice,
    la position et la direction de la fourmi. Sinon, génère une nouvelle partie aléatoire.
    """
    root = tk.Tk()
    root.title("Langton's Ant")
    root.resizable(True, True)
    root.configure(bg=blanc)

    # Création de la matrice pour le placement des cases et des identifiants des cases du canvas
    matrice = create_matrice()
    cell_ids = create_cell_ids()

    # Canvas sur lequel la grille et la fourmi sont dessinées
    canvas = tk.Canvas(root, width=width, height=height, bg=blanc)
    canvas.pack()

    # Barre du bas contenant les boutons
    frame = tk.Frame(root, bg=blanc)
    frame.pack(fill=tk.X)

    # --- Initialisation de la matrice ---
    if state:
        # Chargement depuis la sauvegarde
        for row in range(len(matrice)):
            for col in range(len(matrice[0])):
                matrice[row][col] = state["matrice"][row][col]
    else:
        # Génération aléatoire : "b" = blanc, "w" = noir
        for row in range(len(matrice)):
            for col in range(len(matrice[0])):
                matrice[row][col] = "b" if r.randint(1, 2) == 1 else "w"

    # Affichage initial de la grille sur le canvas
    display(matrice, cell_ids, canvas, height, width, size)

    # --- Initialisation de la fourmi ---
    if state:
        # Position et direction restaurées depuis la sauvegarde
        pos_ant = (state["ant_pos"][0], state["ant_pos"][1])
        direction = state["ant_dir"]
    else:
        # Position et direction aléatoires pour une nouvelle partie
        pos_ant = (r.randint(0, height // size - 1), r.randint(0, width // size - 1))
        direction = "N"

    ant = Ant(pos_ant, canvas, size, height, width, matrice)
    ant.direction = direction
    ant.draw()

    # Variable partagée pour savoir si l'animation est active
    # On utilise une liste pour pouvoir la modifier depuis les fonctions internes
    animation_en_cours = [False]

    def game_loop():
        """
        Boucle principale du jeu.
        À chaque appel, déplace la fourmi d'un pas, met à jour la case qu'elle vient
        de quitter, puis se rappelle elle-même après 'var_vitesse' millisecondes.
        """
        if animation_en_cours[0]:
            old_pos = (ant.p[0], ant.p[1])  # On mémorise la position avant le déplacement
            ant.move()                        # La fourmi se déplace et retourne la case
            update_cell(matrice, cell_ids, canvas, old_pos[0], old_pos[1])  # Met à jour l'ancienne case
            ant.draw()                        # Redessine la fourmi à sa nouvelle position
            root.after(var_vitesse, game_loop)  # Rappel après le délai défini

    

    def nouvelle_grille():
        """
        Réinitialise la partie :
        - Stoppe l'animation
        - la matrice est recrée avec les canvas
        - Replace la fourmi aléatoirement
        """
        # Stoppe l'animation sans toucher aux boutons
        animation_en_cours[0] = False

        # recréation de la matrice
        for row in range(len(matrice)):
            for col in range(len(matrice[0])):
                if r.randint(1, 2) == 1:
                    matrice[row][col] = "b"
                else:
                    matrice[row][col] = "w"

        # Efface toutes les canvas
        canvas.delete("all")

        # Réinitialise les identifiants de cases
        cell_ids_new = create_cell_ids()
        for row in range(len(cell_ids)):
            for col in range(len(cell_ids[0])):
                cell_ids[row][col] = cell_ids_new[row][col]

        # Redessine la grille selon la nvelle matrice
        display(matrice, cell_ids, canvas, height, width, size)

        # Replace la fourmi à une position aléatoire, face au Nord
        ant.p = [r.randint(0, height // size - 1), r.randint(0, width // size - 1)]
        ant.direction = "N"
        ant.ant_id = None  # Reset l'id canvas pour éviter une erreur de suppression
        ant.draw()

    def basculer_animation():
        """
        Démarre ou met en pause l'animation selon l'état actuel.
        - Si on démarre : désactive le bouton sauvegarder et lance la boucle
        - Si on met en pause : active le bouton sauvegarder
        """
        animation_en_cours[0] = not animation_en_cours[0]
        if animation_en_cours[0]:
            bouton_save.config(state=tk.DISABLED) 
            game_loop()
        else:
            bouton_save.config(state=tk.NORMAL)    # Sauvegarde disponible uniquement en pause

    def sauvegarder():
        """
        Sauvegarde l'état actuel de la partie dans un fichier JSON :
        - La matrice complète
        - La position de la fourmi et sa direction
        Affiche un retour visuel de confirmation pendant 2 secondes.
        """
        save_data = {
            "matrice": [row[:] for row in matrice],  # Copie ligne par ligne pour éviter les références
            "ant_pos": [ant.p[0], ant.p[1]],
            "ant_dir": ant.direction
        }
        with open(SAVE_FILE, "w") as f:
            json.dump(save_data, f)

        #visuel temporaire sur le bouton
        bouton_save.config(text="Sauvegardé !", bg="#005500")
        root.after(2000, lambda: bouton_save.config(text="Sauvegarder", bg="#333333"))

    def step_once():
        """
        Avance la fourmi d'un seul pas, uniquement si l'animation est en pause.
        on l'utilse pour avancer étape par étape.
        """
        if animation_en_cours[0]:  # ← si l'animation tourne, on ne fait rien
            return
        old_pos = (ant.p[0], ant.p[1])
        ant.move()
        update_cell(matrice, cell_ids, canvas, old_pos[0], old_pos[1])  # ← arguments manquants ajoutés
        ant.draw()




    #    Création des boutons 

    # Bouton pour générer une nouvelle grille aléatoire
    bouton_grille = tk.Button(root, text="Nouvelle grille", command=nouvelle_grille)
    bouton_grille.pack(side=tk.BOTTOM, padx=10, pady=5)

    # Bouton pour démarrer ou mettre en pause la fourmi
    bouton_animation = tk.Button(frame, text="Démarrer", command=basculer_animation,
                                 bg="green", fg="white",
                                 padx=10, pady=5)
    bouton_animation.pack(side=tk.BOTTOM, padx=10, pady=5)

    # Bouton pour sauvegarder la partie (désactivé pendant l'animation)
    bouton_save = tk.Button(frame, text="Sauvegarder", command=sauvegarder,
                            bg="#333333", fg="white",
                            padx=10, pady=5, state=tk.DISABLED)

    bouton_save.pack(side=tk.BOTTOM, padx=10, pady=5)

    #Bouton next pour l'instance d'après
    next_button = tk.Button(root, text="Next", command=step_once, bg="red", fg="black", padx = 10, pady = 5)
    next_button.pack(side = tk.BOTTOM, padx = 10, pady = 5)



    root.mainloop()

if __name__ == "__main__":
    lancer_menu()
