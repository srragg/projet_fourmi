import tkinter as tk
import random as r
from map import *
from ant import Ant

root = tk.Tk()
root.title("Langten's ant")

root.geometry(f"{width}x{height}")
root.resizable(False, False)    #rend les dimensions fixes et fidèles au cases         

display(matrice, root, height, width, size)                                   #affichage de la fourmi

pos_ant = (r.randint(0, height // size - 1), r.randint(0, width // size - 1)) #position aléatorire de la fourmi
ant = Ant(pos_ant, root, size, height, width, matrice)                        #création de la fourmi

#boucle de tour de jeu
def game_loop():    
    old_pos = (ant.p[0], ant.p[1])  #ancienne position de la fourmi pour redessiner la case après le mouvement de la fourmi
    ant.move()                          # move() déplace la fourmi
    update_cell(old_pos[0], old_pos[1]) # met à jour l'affichage de la case précédente
    ant.draw()                          #on redessine la fourmi
    root.after(50, game_loop)           #recommence la tour de boucle (par récursivité)
    
    
game_loop()
root.mainloop()
