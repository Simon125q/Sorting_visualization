import pygame, sys

WIDTH = 1500
HEIGHT = 800
WINDOW_SIZE = (WIDTH, HEIGHT)
SNOOZE = 400
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)

class VisualCell:

    def __init__(self, value, x, y, cell_size, color = (255, 204, 0)):
        self.value = value
        self.x = x
        self.y = y
        self.cell_size = cell_size
        self.color = color

    def update(self, new_value):
        "Update value of the cell"
        self.value = new_value

    def move(self, dx, dy):
        "Move the cell by dx and dy"
        self.x += dx
        self.y += dy
    
    def set_position(self, x, y):
        "Set position of the cell to x and y"
        self.x = x
        self.y = y

    def draw(self, color = 0):
        "Draw the cell at its coordinates and with provided color"
        if color == 0:
            color = self.color
        cell_rect = pygame.Rect(self.x, self.y, self.cell_size, self.cell_size)
        pygame.draw.rect(screen, color, cell_rect)
        myfont = pygame.font.Font('C:/Users/szomi/Dropbox/Komputer/Desktop/Algorithms&DS/traveling-salesman-main/font/Roboto-Light.ttf', 50)
        num = myfont.render(str(self.value), True, (255, 255, 255))
        num_box = num.get_rect()
        num_box.center = (self.x + self.cell_size/2, self.y + self.cell_size/2)
        screen.blit(num, num_box)

class VisualTable:

    def __init__(self, data):
        self.data = []
        self.length = len(data)
        self.cell_size = (WIDTH - 10 * self.length) / self.length
        y = HEIGHT/2 - self.cell_size
        screen.fill("Grey")
        "Append the Visual table with Visual cells"
        for elem in range(self.length):
            x = elem*self.cell_size + (elem+1) * 5
            cell = VisualCell(data[elem], x, y, self.cell_size)
            self.data.append(cell)
        self.visualize()
        
    def swap(self, index1, index2):
        "Swap 2 cells with provided indexes"
        if index1 == index2:
            return
        elif index1 >= self.length or index2 >= self.length:
            return
        self.animate(index1, index2)
        temp = self.data[index1]
        self.data[index1] = self.data[index2]
        self.data[index2] = temp
        self.visualize()
        pygame.time.wait(SNOOZE)

    def look(self, index):
        "Check value of given cell"
        if index >= self.length:
            return False
        self.visualize()
        self.data[index].draw("Green")
        pygame.display.flip()
        pygame.time.wait(SNOOZE)
        return self.data[index].value
        
    def compare(self, index1, index2):
        "Compare 2 cells with given indexes"
        if index1 >= self.length or index2 >= self.length:
            return False
        self.visualize()
        self.data[index1].draw("Red")
        self.data[index2].draw("Red")
        pygame.display.flip()
        pygame.time.wait(SNOOZE)
        if self.data[index1].value > self.data[index2].value:
            return True
        else:
            return False
    
    def animate(self, index1, index2):
        "Animate swaping of cells"
        if index1 > index2:
            temp = index1
            index1 = index2
            index2 = temp
        diff = 2
        old_cord1 = [self.data[index1].x, self.data[index1].y]
        old_cord2 = [self.data[index2].x, self.data[index2].y]
        
        while self.data[index1].y < old_cord1[1] + self.cell_size + 10:
            self.data[index1].move(0, diff)
            self.data[index2].move(0, -diff)
            self.visualize()
        while self.data[index1].x < old_cord2[0]:
            self.data[index1].move(diff, 0)
            self.data[index2].move(-diff, 0)
            self.visualize()
        while self.data[index1].y > old_cord2[1]:
            self.data[index1].move(0, -diff)
            self.data[index2].move(0, diff)
            self.visualize()
        self.data[index1].set_position(old_cord2[0], old_cord2[1])
        self.data[index2].set_position(old_cord1[0], old_cord1[1])
            
    def visualize(self):
        "Draw all cells in the table"
        screen.fill("Grey")
        for element in range(self.length):
            self.data[element].draw()
        pygame.display.flip()


if __name__ == "__main__":
    nums = [12, 24, 23, 1, 56, 2, 32, 5, 10]
    table = VisualTable(nums)
    pygame.time.wait(1000)
    for index in range(table.length):
        table.look(index)


    table.compare(1, 3)
    table.swap(1, 3)
    table.compare(6, 1)
    table.swap(0, 7)
    table.compare(5, 6)
    table.swap(1, 2)
    table.compare(1, 12)
    table.swap(1, 25)
    table.compare(0, table.length-1)
    table.swap(0, table.length-1)
