import pygame

WIDTH = 1500
HEIGHT = 800
WINDOW_SIZE = (WIDTH, HEIGHT)
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)

class VisualCell:

    def __init__(self, value, x, y, cell_size, color = "Green"):
        self.value = value
        self.x = x
        self.y = y
        self.cell_size = cell_size
        self.color = color

    def draw(self):
        cell_rect = pygame.Rect(self.x, self.y, self.cell_size, self.cell_size)
        pygame.draw.rect(screen, self.color, cell_rect)
        myfont = pygame.font.Font('fonts/TimesNewRoman.ttf', 20)
        num = myfont.render(str(self.value), True, (255, 255, 255))
        num_box = num.get_rect()
        num_box.center = (self.x + self.cell_size, self.y + self.cell_size)
        screen.blit(num, num_box)

class VisualTable:

    def __init__(self, data):
        self.data = []
        self.length = len(data)
        self.cell_size = (WIDTH - 10 * self.length) / self.length
        y = HEIGHT/2 - self.cell_size
        for elem in range(self.length):
            x = elem*self.cell_size + (elem+1) * 5
            cell = VisualCell(data[elem], x, y, self.cell_size)
            self.data.append(cell)

    def swap(self, index1, index2):
        temp = self.data[index1].value
        self.data[index1].value = self.data[index2].value
        self.data[index1].value = temp
        self.visualize()

    def look(self, index):
        return self.data[index]
    def compare(self, index1, index2):
        pass
    def visualize(self):
        for element in range(self.length):
            #center = (2 * element + 1) * (self.cell_size / 2) + (element + 1) * 5
            self.data[element].draw()
            