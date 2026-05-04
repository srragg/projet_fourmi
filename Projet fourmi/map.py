import tkinter as tk
import json
import os

SAVE_FILE = "save.json"

def lancer_menu():
    """
    ouverture du menu pour permettre soit de remettre l'ancienne position
    soit lancer une nouvelle partie
    """
    root = tk.Tk()
    root.title("Fourmi de Langton")
    root.geometry("400x350")
    root.configure(bg="black")

    label = tk.Label(root, text="🐜 Jeu de la Fourmi", bg="black", fg="cyan",
                     font=("Helvetica", 28, "bold"), pady=30)
    label.pack()

    def on_jouer():
        """
        on crée le nv dossier
        """
        root.destroy()
        from main import lancer_jeu
        lancer_jeu()

    def on_charger():
        """
        on charge l'ancien dosser
        """
        root.destroy()
        from main import lancer_jeu
        with open(SAVE_FILE, "r") as f:
            state = json.load(f)
        lancer_jeu(state=state)
    """
    on retrouve les boutons du menu
    """
    bouton_jouer = tk.Button(root, text="▶  Jouer", bg="cyan", fg="black",
                             font=("Helvetica", 20, "bold"), padx=20, pady=10,
                             command=on_jouer, relief="flat", cursor="hand2")
    bouton_jouer.pack(pady=5)

    # Bouton charger uniquement si une sauvegarde existe
    if os.path.exists(SAVE_FILE):
        bouton_charger = tk.Button(root, text="📂  Charger la partie", bg="#005599", fg="white",
                                   font=("Helvetica", 16, "bold"), padx=20, pady=8,
                                   command=on_charger, relief="flat", cursor="hand2")
        bouton_charger.pack(pady=5)

    bouton_quitter = tk.Button(root, text="✕  Quitter", bg="red", fg="white",
                               font=("Helvetica", 14), padx=10, pady=5,
                               command=root.quit, relief="flat", cursor="hand2")
    bouton_quitter.pack(pady=10)

    root.mainloop()
