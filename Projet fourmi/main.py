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
    paused = False  # état pause

    def toggle_pause():
        nonlocal paused
        paused = not paused
        pause_bouton.config(text="Reprendre" if paused else "Pause")

    def step_once():
        if not paused:
            return  

        old_pos = (ant.p[0], ant.p[1])
        ant.move()
        update_cell(old_pos[0], old_pos[1])
        ant.draw()


    def game_loop():
        nonlocal paused

        if paused:
            root.after(500, game_loop)
            return 
        old_pos = (ant.p[0], ant.p[1])
        ant.move()
        update_cell(old_pos[0], old_pos[1])
        ant.draw()
        root.after(500, game_loop)

    pause_bouton = tk.Button( root, text="Pause",bg="red", fg="black",
                       font=("Helvetica", 20, "bold"), command=toggle_pause)
    pause_bouton.place(x=10, y=10)

    next_bouton = tk.Button(root, text="Next",bg="red", fg="black",
                       font=("Helvetica", 20, "bold"), command=step_once)
    next_bouton.place(x=10, y=70)

    game_loop()
    root.mainloop()

if __name__ == "__main__": 
    lancer_menu()
