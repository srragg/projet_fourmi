import random as r

# Couleurs utilisées pour les cases de la grille
blanc = "white"
noir = "black"

# Dimensions de la fenêtre de jeu en pixels
height = 640
width = 640

# Taille d'une case en pixels
size = 20

def create_matrice():
    """
    retourne une matrice
    Chaque case vaut soit "b" (blanc) soit "w" (noir).
    """
    return [["b" if r.randint(1, 2) == 1 else "w" for _ in range(width // size)] for _ in range(height // size)]

def create_cell_ids():
    """
    Crée une matrice de même taille que la matrice de jeu,
    initialisée à None. Elle stockes les ids des rectangles du canvas
    pour pouvoir les mettre à jour sans tout redessiner.
    """
    return [[None for _ in range(width // size)] for _ in range(height // size)]

def display(matrice, cell_ids, canvas, height, width, size):
    """
    Dessine la grille entière sur le canvas pour la première fois.
    Chaque case est un rectangle coloré selon la valeur de la matrice :
    - "b" → blanc
    - "w" → noir
    Les identifiants canvas de chaque rectangle sont stockés dans cell_ids
    pour permettre des mises à jour rapides.
    """
    for row in range(len(matrice)):
        for col in range(len(matrice[0])):
            color = blanc if matrice[row][col] == "b" else noir
            x1, y1 = col * size, row * size
            cell_id = canvas.create_rectangle(x1, y1, x1 + size, y1 + size,
                                              fill=color, outline="gray")
            cell_ids[row][col] = cell_id  # Sauvegarde de l'id pour update_cell

def update_cell(matrice, cell_ids, canvas, row, col):
    """
    Met à jour la couleur d'une seule case.
    Utilisée après chaque déplacement de la fourmi pour redessiner la case quitter par la fourmi.
    """
    color = blanc if matrice[row][col] == "b" else noir
    canvas.itemconfig(cell_ids[row][col], fill=color)
