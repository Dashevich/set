import pygame
from functions import *

class Card:
    def __init__(self, display, x, y, width, height, color, form, num, shade, inactive_clr=(0, 212, 255), active_clr=(255, 154, 0), clicked = 0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color  # цвет
        self.form = form  # форма
        self.num = num  # количество
        self.shade = shade  # заполнение
        self.inactive_clr = inactive_clr
        self.active_clr = active_clr
        self.display = display
        self.clicked = clicked
        # self.image = image

    def draw(self, display):
        name = ""
        # display.blit(self.image, (self.x, self.y))
        pygame.draw.rect(display, (255,255,255), (self.x, self.y, self.width, self.height))
        if self.form == 0:
            name += "diamond_"
        if self.form == 1:
            name += "oval_"
        if self.form == 2:
            name += "squiggle_"

        if self.shade == 0:
            name += "open_"
        if self.shade == 1:
            name += "striped_"
        if self.shade == 2:
            name += "solid_"

        if self.color == 0:
            name += "red"
        if self.color == 1:
            name += "blue"
        if self.color == 2:
            name += "green"
        c = pygame.image.load(f"cards/{name}.png")
        c = pygame.transform.rotate(c, 90)
        if self.num == 0:
            display.blit(c, (self.x + self.width/2 - self.width/10, self.y + 2))
        if self.num == 1:
            display.blit(c, (self.x + self.width/3 - self.width/10, self.y + 2))
            display.blit(c, (self.x + 2 * self.width / 3 - self.width/10, self.y + 2))
        if self.num == 2:
            display.blit(c, (self.x + self.width / 4 - self.width/10, self.y + 2))
            display.blit(c, (self.x + self.width/2 - self.width/10, self.y + 2))
            display.blit(c, (self.x + 3 * self.width / 4 - self.width/10, self.y + 2))



        #print_text(display, f"{self.color} {self.form} {self.num} {self.shade}", self.x, self.y)
        #print(f"{self.color} {self.form} {self.num} {self.shade}")

    def clicks(self, display):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if self.x - 5 < mouse[0] < self.x + 10 + self.width and self.y - 5 < mouse[1] < self.y + 10 + self.height:
            pygame.draw.rect(display, self.active_clr, (self.x - 5, self.y - 5, self.width + 10, self.height + 10))

            if click[0] == 1:
                pygame.time.delay(150)

                if self.clicked == 0:
                    self.inactive_clr = (255, 154, 0)
                    #self.active_clr = (0, 212, 255)
                    self.clicked = 1

                else:
                    self.inactive_clr = (0, 212, 255)
                    #self.active_clr = (255, 154, 0)
                    self.clicked = 0

                return [self.color, self.form, self.num, self.shade]

        else:
            pygame.draw.rect(display, self.inactive_clr, (self.x - 5, self.y - 5, self.width + 10, self.height + 10))

    def show_info(self):
        return [self.color, self.form, self.num, self.shade]
