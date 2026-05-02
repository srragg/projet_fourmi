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
        """
            dessine la fourmi (case rouge) au moment T
        """
        if self.label is not None:
            self.label.destroy()  # on détruit l'ancien label rouge
        self.label = tk.Label(self.sc, bg="red", width=self.s, height=self.s)
        self.label.place(x=self.p[1] * self.s, y=self.p[0] * self.s, width=self.s, height=self.s)

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
        if self.m[self.p[0]][self.p[1]] == 'w':   
            self.turn_left()
            self.m[self.p[0]][self.p[1]] = 'b'
        else:
            self.turn_right()
            self.m[self.p[0]][self.p[1]] = 'w'

        #selon la direction de la fourmi elle se déplace
        if self.direction == "N":
            self.p[0] = (self.p[0] - 1) % (self.h // self.s)
        elif self.direction == "S":
            self.p[0] = (self.p[0] + 1) % (self.h // self.s)
        elif self.direction == "E":
            self.p[1] = (self.p[1] + 1) % (self.w // self.s)
        elif self.direction == "O":
            self.p[1] = (self.p[1] - 1) % (self.w // self.s)
        
        
