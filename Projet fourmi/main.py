import tkinter as tk
import random as r
import json
import os
from map import *
from ant import Ant
from menu import lancer_menu

SAVE_FILE = "save.json"

var_vitesse = 1000

def lancer_jeu(state=None):
    root = tk.Tk()
    root.title("Langton's Ant")
    root.resizable(True, True)
    root.configure(bg="white")

    # --- Canvas qui remplit toute la fenêtre ---
    canvas = tk.Canvas(root, width=width, height=height, bg=blanc, highlightthickness=0)
    canvas.pack()

    # --- Boutons en dessous ---
    frame = tk.Frame(root, bg="white")
    frame.pack(fill=tk.X)

    # Initialise la matrice
    if state:
        for row in range(len(matrice)):
            for col in range(len(matrice[0])):
                matrice[row][col] = state["matrice"][row][col]
    else:
        for row in range(len(matrice)):
            for col in range(len(matrice[0])):
                matrice[row][col] = "b" if r.randint(1, 2) == 1 else "w"

    display(matrice, canvas, height, width, size)

    if state:
        pos_ant = (state["ant_pos"][0], state["ant_pos"][1])
        direction = state["ant_dir"]
    else:
        pos_ant = (r.randint(0, height // size - 1), r.randint(0, width // size - 1))
        direction = "N"

    ant = Ant(pos_ant, canvas, size, height, width, matrice)
    ant.direction = direction
    ant.draw()

    animation_en_cours = [False]

    def game_loop():
        if animation_en_cours[0]:
            old_pos = (ant.p[0], ant.p[1])
            ant.move()
            update_cell(canvas, old_pos[0], old_pos[1])
            ant.draw()
            root.after(var_vitesse, game_loop)

    def nouvelle_grille():
        animation_en_cours[0] = False
        bouton_animation.config(text="▶ Démarrer", bg="green")
        bouton_save.config(state=tk.DISABLED)
        for row in range(len(matrice)):
            for col in range(len(matrice[0])):
                matrice[row][col] = "b" if r.randint(1, 2) == 1 else "w"
                update_cell(canvas, row, col)
        ant.p = [r.randint(0, height // size - 1), r.randint(0, width // size - 1)]
        ant.direction = "N"
        ant.draw()

    def basculer_animation():
        animation_en_cours[0] = not animation_en_cours[0]
        if animation_en_cours[0]:
            bouton_animation.config(text="⏸ Pause", bg="orange")
            bouton_save.config(state=tk.DISABLED)
            game_loop()
        else:
            bouton_animation.config(text="▶ Démarrer", bg="green")
            bouton_save.config(state=tk.NORMAL)

    def sauvegarder():
        save_data = {
            "matrice": [row[:] for row in matrice],
            "ant_pos": [ant.p[0], ant.p[1]],
            "ant_dir": ant.direction
        }
        with open(SAVE_FILE, "w") as f:
            json.dump(save_data, f)
        bouton_save.config(text="✅ Sauvegardé !", bg="#005500")
        root.after(2000, lambda: bouton_save.config(text="💾 Sauvegarder", bg="#333333"))

    bouton_grille = tk.Button(frame, text="🔄 Nouvelle grille", command=nouvelle_grille,
                              bg="cyan", fg="black", font=("Helvetica", 12, "bold"),
                              padx=10, pady=5)
    bouton_grille.pack(side=tk.BOTTOM, padx=10, pady=5)

    bouton_animation = tk.Button(frame, text="▶ Démarrer", command=basculer_animation,
                                 bg="green", fg="white", font=("Helvetica", 12, "bold"),
                                 padx=10, pady=5, relief="flat", cursor="hand2")
    bouton_animation.pack(side=tk.BOTTOM, padx=10, pady=5)

    bouton_save = tk.Button(frame, text="💾 Sauvegarder", command=sauvegarder,
                            bg="#333333", fg="white", font=("Helvetica", 12, "bold"),
                            padx=10, pady=5, relief="flat", cursor="hand2",
                            state=tk.DISABLED)
    bouton_save.pack(side=tk.BOTTOM, padx=10, pady=5)

    root.mainloop()

if __name__ == "__main__":
    lancer_menu()
