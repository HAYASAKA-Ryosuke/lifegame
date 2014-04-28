import turtle
import time
import copy


class lifegame(object):

    def __init__(self, cell):
        self.cell = cell

    def __left(self, x, y):
        if x > 0:
            if self.cell[y][x-1] == 1:  # left
                return 1
            else:
                return 0
        else:
            return 0

    def __leftup(self, x, y):
        if x > 0 and y > 0:
            if self.cell[y-1][x-1] == 1:  # leftup
                return 1
            else:
                return 0
        else:
            return 0

    def __up(self, x, y):
        if y > 0:
            if self.cell[y-1][x] == 1:  # up
                return 1
            else:
                return 0
        else:
            return 0

    def __rightup(self, x, y):
        if x < len(self.cell)-1 and y > 0:
            if self.cell[y-1][x+1] == 1:  # rightup
                return 1
            else:
                return 0
        else:
            return 0

    def __right(self, x, y):
        if x < len(self.cell)-1:
            if self.cell[y][x+1] == 1:  # right
                return 1
            else:
                return 0
        else:
            return 0

    def __rightdown(self, x, y):
        if x < len(self.cell)-1 and y < len(self.cell)-1:
            if self.cell[y+1][x+1] == 1:  # rightdown
                return 1
            else:
                return 0
        else:
            return 0

    def __down(self, x, y):
        if y < len(self.cell)-1:
            if self.cell[y+1][x] == 1:  # down
                return 1
            else:
                return 0
        else:
            return 0

    def __leftdown(self, x, y):
        if y < len(self.cell)-1 and x > 0:
            if self.cell[y+1][x-1] == 1:  # leftdown
                return 1
            else:
                return 0
        else:
            return 0

    def cellcount(self, x, y):
        count = 0
        count += self.__left(x, y)
        count += self.__leftup(x, y)
        count += self.__up(x, y)
        count += self.__rightup(x, y)
        count += self.__right(x, y)
        count += self.__rightdown(x, y)
        count += self.__down(x, y)
        count += self.__leftdown(x, y)
        return count

    def lifeupdate(self):
        buffcell = copy.deepcopy(self.cell)
        for i in range(len(self.cell)):
            for j in range(len(self.cell)):
                cellstate = self.cell[j][i]
                count = self.cellcount(i, j)
                if cellstate == 0 and count == 3:
                    print("x")
                    print(i)
                    print("y")
                    print(j)
                    buffcell[j][i] = 1
                elif cellstate == 1 and (count == 2 or count ==3):
                    pass
                elif cellstate == 1 and count <= 1:
                    buffcell[j][i] = 0
                elif cellstate == 1 and count >= 4:
                    buffcell[j][i] = 0

        self.cell = buffcell
                        
        print("lifeupdate")


class graphics(object):
    def __init__(self, lifegame):
        turtle.tracer(0)
        turtle.color(0, 0.5, 0)
        self.cell = lifegame.cell

    def __drawsquare(self):
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(10)
            turtle.right(90)
        turtle.end_fill()

    def __drawstate(self, x, y, state):
        turtle.penup()
        turtle.home()
        turtle.setpos(x*10, y*10)
        if state == 1:
            turtle.pen(fillcolor="black")
        if state == 0:
            turtle.pen(fillcolor="white")
        turtle.pendown()
        self.__drawsquare()

    def drawcell(self):
        for i in range(len(self.cell)):
            for j in range(len(self.cell)):
                self.__drawstate(j, i, self.cell[i][j])
        print(self.cell)
        turtle.update()

cell = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] 
life = lifegame(cell)
for i in range(100):
    print(i)
    life.lifeupdate()
    g = graphics(life)
    g.drawcell()
    time.sleep(0.5)
    

turtle.mainloop()
