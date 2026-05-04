import tkinter as tk
import json
import os

# Fichier de sauvegarde de la partie
SAVE_FILE = "save.json"

def lancer_menu():
    """
    Affiche le menu principal du jeu.
    avc trois options :
    - Jouer
    - Charger la partie : reprend depuis la dernière sauvegarde
    - Quitter
    """
    root = tk.Tk()
    root.title("Fourmi de Langton")
    root.geometry("400x350")
    root.configure(bg="black")

    # Titre du menu
    label = tk.Label(root, text="🐜 Jeu de la Fourmi", bg="black", fg="cyan",
                     font=("Helvetica", 28, "bold"), pady=30)
    label.pack()

    def on_jouer():
        """
        Ferme le menu et lance une nouvelle partie sans sauvegarde.
        """
        root.destroy()
        from main import lancer_jeu
        lancer_jeu()

    def on_charger():
        """
        Ferme le menu, lit le fichier de sauvegarde
        et lance le jeu en restaurant l'état sauvegardé.
        """
        root.destroy()
        from main import lancer_jeu
        with open(SAVE_FILE, "r") as f:
            state = json.load(f)
        lancer_jeu(state=state)

    # Bouton pour démarrer une nouvelle partie
    bouton_jouer = tk.Button(root, text="Jouer", bg="cyan", fg="black",
                             font=("Helvetica", 20, "bold"), padx=20, pady=10,
                             command=on_jouer, relief="flat", cursor="hand2")
    bouton_jouer.pack(pady=5)

    # Bouton charger uniquement si un fichier de sauvegarde existe
    if os.path.exists(SAVE_FILE):
        bouton_charger = tk.Button(root, text="Charger la partie", bg="#005599", fg="white",
                                   font=("Helvetica", 16, "bold"), padx=20, pady=8,
                                   command=on_charger, relief="flat", cursor="hand2")
        bouton_charger.pack(pady=5)

    # Bouton pour quitter l'application
    bouton_quitter = tk.Button(root, text="✕  Quitter", bg="red", fg="white",
                               font=("Helvetica", 14), padx=10, pady=5,
                               command=root.quit, relief="flat", cursor="hand2")
    bouton_quitter.pack(pady=10)

    root.mainloop()
