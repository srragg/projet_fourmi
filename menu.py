import tkinter as tk
from main import lancer_jeu

racine = tk.Tk() # Création de la fenêtre racine
label = tk.Label(racine, text="Jeu de la fourmis",
                  padx=20, pady=20, font = ("helvetica", "30") 
                )
label.grid(row=0, column=0)
bouton = tk.Button(racine, text="play", 
                    command=lancer_jeu, font = ("helvetica", "30") 
                  ) # création du button
bouton.grid(row=1, column=0) # positionnement du button
racine.mainloop() # Lancement de la boucle principale
