import pygame
from functions import *


class Button:
    def __init__(self, display, width, height):
        self.width = width
        self.height = height
        self.inactive_clr = (13, 162, 58)
        self.active_clr = (23, 204, 58)
        self.display = display

    def draw(self, display, x, y, message, action=None, font_size=30):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
                pygame.draw.rect(display, self.active_clr, (x, y, self.width, self.height))

                if click[0] == 1:
                    pygame.time.delay(300)
                    if action is not None:
                        if action == quit:
                            pygame.quit()
                            quit()
                        else:
                            action()
        else:
            pygame.draw.rect(display, self.inactive_clr, (x, y, self.width, self.height))

        print_text(display, message=message, x=x + 10, y=y + 10, font_size=font_size)
