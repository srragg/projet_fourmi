import tkinter as tk
import random as r
from map import *
from ant import Ant
from menu import lancer_menu

def lancer_jeu():
    root = tk.Tk()
    root.title("Langton's Ant")
    root.geometry(f"{width}x{height}")
    root.resizable(False, False)

    display(matrice, root, height, width, size)

    pos_ant = (r.randint(0, height // size - 1), r.randint(0, width // size - 1))
    ant = Ant(pos_ant, root, size, height, width, matrice)

    def game_loop():
        old_pos = (ant.p[0], ant.p[1])
        ant.move()
        update_cell(old_pos[0], old_pos[1])
        ant.draw()
        root.after(500, game_loop)

    game_loop()
    root.mainloop()

if __name__ == "__main__":  # ← cette ligne est la clé
    lancer_menu()