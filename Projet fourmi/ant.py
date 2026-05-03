import tkinter as tk

class Ant:
    def __init__(self, pos, screen, size, height, width, matrice):
        self.p = list(pos)
        self.sc = screen
        self.s = size
        self.h = height
        self.w = width
        self.m = matrice
        self.direction = "N"
        self.label = None  # on sauvegarde le label de la fourmi
    
    def draw(self):
    # 1. Si une fourmi était déjà dessinée, on l'efface
        if hasattr(self, 'label') and self.label:
            self.sc.delete(self.label)

        # 2. On calcule la position de la fourmi sur le canevas
        x = self.p[1] * self.s  # Position en X (colonne * taille d'une case)
        y = self.p[0] * self.s  # Position en Y (ligne * taille d'une case)

        # 3. On dessine un cercle rouge à cette position
        self.label = self.sc.create_oval(x, y, x + self.s, y + self.s, fill="red", outline="black")

    def turn_right(self):
        """
        tourne vers la droite selon son point cardinal et lui attribue son nv point cardinal(direction)
        """
        turns = {"N": "E", "E": "S", "S": "O", "O": "N"}
        self.direction = turns[self.direction]

    def turn_left(self):
        """
        tourne vers la gauche selon son point cardinal et lui attrivue son nv point cardinal(direction)
        """
        turns = {"N": "O", "O": "S", "S": "E", "E": "N"}
        self.direction = turns[self.direction]

    def move(self):
        """
        se déplace selon sa direction (point cardinal)
        """
        #premiere condition vérifie selon sur quel case est la fourmi
        if self.m[self.p[0]][self.p[1]] == 'blanc':   
            self.turn_left()
            self.m[self.p[0]][self.p[1]] = 'noir'
        else:
            self.turn_right()
            self.m[self.p[0]][self.p[1]] = 'blanc'

        #selon la direction de la fourmi elle se déplace
        if self.direction == "N":
            self.p[0] = (self.p[0] - 1) % (self.h // self.s)
        elif self.direction == "S":
            self.p[0] = (self.p[0] + 1) % (self.h // self.s)
        elif self.direction == "E":
            self.p[1] = (self.p[1] + 1) % (self.w // self.s)
        elif self.direction == "O":
            self.p[1] = (self.p[1] - 1) % (self.w // self.s)
        
        
