import pygame, sys

WIDTH = 1500
HEIGHT = 800
WINDOW_SIZE = (WIDTH, HEIGHT)
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
        self.value = new_value

    def draw(self, color = 0):
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
        for elem in range(self.length):
            x = elem*self.cell_size + (elem+1) * 5
            cell = VisualCell(data[elem], x, y, self.cell_size)
            self.data.append(cell)
        self.visualize()

    def swap(self, index1, index2):
        print(f"num 1: {self.data[index1].value}, num 2: {self.data[index2].value}")
        temp = self.data[index1].value
        self.data[index1].update(self.data[index2].value)
        self.data[index1].update(temp)
        print(f"num 1: {self.data[index1].value}, num 2: {self.data[index2].value}, temp: {temp}")
        self.visualize()

    def look(self, index):
        self.visualize()
        self.data[index].draw("Green")
        pygame.display.flip()
        return self.data[index].value
    def compare(self, index1, index2):
        self.visualize()
        self.data[index1].draw("Red")
        self.data[index2].draw("Red")
        pygame.display.flip()
        return max(self.data[index1].value, self.data[index2].value)
    def visualize(self):
        for element in range(self.length):
            #center = (2 * element + 1) * (self.cell_size / 2) + (element + 1) * 5
            self.data[element].draw()
        pygame.display.flip()


if __name__ == "__main__":
    nums = [12, 24, 23, 1, 56, 2, 32, 5, 10]
    table = VisualTable(nums)
    pygame.time.wait(1000)
    for index in range(table.length):
        table.look(index)
        pygame.time.wait(500)

    table.swap(2, 5)
    pygame.time.wait(500)
    table.compare(1, 3)
    pygame.time.wait(10000)