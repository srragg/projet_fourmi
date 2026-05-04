import tkinter as tk

class Ant:
    """
    Représente la fourmi de Langton
    La fourmi réapparait de l'autre côté de la grille si elle sort du bord.
    """

    def __init__(self, pos, screen, size, height, width, matrice):
        """
        Initialise la fourmi.
        """
        self.p = list(pos)     # Position actuelle [ligne, colonne]
        self.sc = screen       # Canvas tkinter
        self.s = size          # Taille d'une case en pixels
        self.h = height        # Hauteur totale en pixels
        self.w = width         # Largeur totale en pixels
        self.m = matrice       # Référence à la matrice de jeu
        self.direction = "N"   # Direction initiale : Nord
        self.ant_id = None     # Identifiant du rectangle canvas représentant la fourmi

    def draw(self):
        """
        Dessine la fourmi sur le canvas sous forme d'un carré rouge.
        Elle supprimel'ancien dessin si il existe,
        puis crée un nveau rectangle à sa position actuelle.
        """
        if self.ant_id is not None:
            self.sc.delete(self.ant_id)  # Efface l'ancien carré rouge
        x1 = self.p[1] * self.s
        y1 = self.p[0] * self.s
        self.ant_id = self.sc.create_rectangle(
            x1, y1, x1 + self.s, y1 + self.s,
            fill="red", outline="gray"
        )

    def turn_right(self):
        """
        Fait tourner la fourmi de 90° vers la droite
        en mettant à jour son point cardinal.
        """
        turns = {"N": "E", "E": "S", "S": "O", "O": "N"}
        self.direction = turns[self.direction]

    def turn_left(self):
        """
        Fait tourner la fourmi de 90° vers la gauche
        en mettant à jour son point cardinal.
        """
        turns = {"N": "O", "O": "S", "S": "E", "E": "N"}
        self.direction = turns[self.direction]

    def move(self):
        """
        Applique les règles de la fourmi de Langton pour un pas :
        - Regarde la couleur de la case actuelle
        - Tourne à gauche si blanche, à droite si noire
        - Inverse la couleur de la case
        - Avance d'une case dans la nvlle direction
        """
        # Règle 1 & 2 : tourner selon la couleur de la case
        if self.m[self.p[0]][self.p[1]] == 'w':
            self.turn_left()
            self.m[self.p[0]][self.p[1]] = 'b'  # La case devient noire
        else:
            self.turn_right()
            self.m[self.p[0]][self.p[1]] = 'w'  # La case devient blanche

        # Règle 3 : avancer d'une case selon la direction (avec rebord toroïdal)
        if self.direction == "N":
            self.p[0] = (self.p[0] - 1) % (self.h // self.s)
        elif self.direction == "S":
            self.p[0] = (self.p[0] + 1) % (self.h // self.s)
        elif self.direction == "E":
            self.p[1] = (self.p[1] + 1) % (self.w // self.s)
        elif self.direction == "O":
            self.p[1] = (self.p[1] - 1) % (self.w // self.s)
