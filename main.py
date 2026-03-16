import tkinter as tk
import random as r

root = tk.Tk()
root.title("Fourmi de Langton")

color1 = "white"
color2 = "black"
height = 768
width = 768
size = 16


#règle les dimensions de l'écran
root.geometry(f"{width}x{height}")
root.resizable(False, False)

#crée la matrice aléatoire qui indique si la case est blanche ou noir
matrice = [["b" if r.randint(1, 2) == 1 else "n" for _ in range(width // size)] for _ in range(height // size)]


#fonction qui affiche le grillage
def display(matrice, screen, height, width, size):
    for row in range(len(matrice)):
        for col in range(len(matrice[0])):
            color = color1 if matrice[row][col] == "b" else color2
            label = tk.Label(screen, bg=color, width=size, height=size)
            label.place(x=col * size, y=row * size, width=size, height=size)

display(matrice, root, height, width, size)  

root.mainloop()  
