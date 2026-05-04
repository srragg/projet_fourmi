import random as r

blanc = "white"
noir = "black"
height = 640   # ← 512 → 640
width = 640    # ← 512 → 640
size = 20      # ← 16 → 20


#initialisationd de la matrice
matrice = [["b" if r.randint(1, 2) == 1 else "w" for _ in range(width // size)] for _ in range(height // size)]
cell_ids = [[None for _ in range(width // size)] for _ in range(height // size)]

def display(matrice, canvas, height, width, size):
    """
    Affichage initial de chaque case sur le canvas.
    """
    for row in range(len(matrice)):
        for col in range(len(matrice[0])):
            color = blanc if matrice[row][col] == "b" else noir
            x1, y1 = col * size, row * size
            cell_id = canvas.create_rectangle(x1, y1, x1 + size, y1 + size,
                                              fill=color, outline="gray")  # ← outline ajouté
            cell_ids[row][col] = cell_id

def update_cell(canvas, row, col):
    """
    Mise à jour de la couleur d'une case sur le canvas.
    """
    color = blanc if matrice[row][col] == "b" else noir
    canvas.itemconfig(cell_ids[row][col], fill=color)
