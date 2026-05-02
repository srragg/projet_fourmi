import tkinter as tk

def lancer_menu():
    root = tk.Tk()
    root.title("Fourmi de Langton")
    root.geometry("400x300")
    root.configure(bg="black")

    label = tk.Label(root, text="🐜 Jeu de la Fourmi", bg="black", fg="cyan",
                     font=("Helvetica", 28, "bold"), pady=40)
    label.pack()

    def on_jouer():
        root.destroy()        # ← ferme le menu
        from main import lancer_jeu
        lancer_jeu()          # ← ouvre le jeu

    bouton = tk.Button(root, text="▶  Jouer", bg="cyan", fg="black",
                       font=("Helvetica", 20, "bold"), padx=20, pady=10,
                       command=on_jouer, relief="flat", cursor="hand2")
    bouton.pack()

    bouton_quitter = tk.Button(root, text="✕  Quitter", bg="red", fg="white",
                               font=("Helvetica", 14), padx=10, pady=5,
                               command=root.quit, relief="flat", cursor="hand2")
    bouton_quitter.pack(pady=10)

    root.mainloop()

