

class Ant:
    def __init__(self, pos, screen, size, height, width, matrice):
        self.p = list(pos)
        self.sc = screen
        self.s = size
        self.h = height
        self.w = width
        self.m = matrice
        self.direction = "N"
        self.ant_id = None

    def draw(self):
        """
        Dessine la fourmi (case rouge) directement sur le canvas.
        """
        if self.ant_id is not None:
            self.sc.delete(self.ant_id)
        x1 = self.p[1] * self.s
        y1 = self.p[0] * self.s
        self.ant_id = self.sc.create_rectangle(
            x1, y1, x1 + self.s, y1 + self.s,
            fill="red", outline="gray"  # ← outline ajouté
        )

    def turn_right(self):
        turns = {"N": "E", "E": "S", "S": "O", "O": "N"}
        self.direction = turns[self.direction]

    def turn_left(self):
        turns = {"N": "O", "O": "S", "S": "E", "E": "N"}
        self.direction = turns[self.direction]

    def move(self):
        if self.m[self.p[0]][self.p[1]] == 'w':
            self.turn_left()
            self.m[self.p[0]][self.p[1]] = 'b'
        else:
            self.turn_right()
            self.m[self.p[0]][self.p[1]] = 'w'

        if self.direction == "N":
            self.p[0] = (self.p[0] - 1) % (self.h // self.s)
        elif self.direction == "S":
            self.p[0] = (self.p[0] + 1) % (self.h // self.s)
        elif self.direction == "E":
            self.p[1] = (self.p[1] + 1) % (self.w // self.s)
        elif self.direction == "O":
            self.p[1] = (self.p[1] - 1) % (self.w // self.s)
