import random as r
import tkinter as tk

color1 = "white"
color2 = "black"
height = 512
width = 512 
size = 16 

matrice = [["b" if r.randint(1, 2) == 1 else "w" for _ in range(width // size)] for _ in range(height // size)]

# On stocke les labels dans un tableau
labels = [[None for _ in range(width // size)] for _ in range(height // size)]


def display(matrice, screen, height, width, size):
    """"
        affichage première de chaque case blanche ou noir 
    """
    for row in range(len(matrice)):
        for col in range(len(matrice[0])):
            color = color1 if matrice[row][col] == "b" else color2
            label = tk.Label(screen, bg=color, width=size, height=size)
            label.place(x=col * size, y=row * size, width=size, height=size)
            labels[row][col] = label  # on sauvegarde le label


def update_cell(row, col):
    """
    réecriture de la couleur de la case
    """
    color = color1 if matrice[row][col] == "b" else color2
    labels[row][col].config(bg=color)  # on met juste à jour la couleur

    
