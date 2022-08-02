import pygame
from Button import Button
from game_window import game_cycle
import windows
from functions import *

clock = pygame.time.Clock()
display_width = 1200 #размеры дисплея
display_height = 700
display = pygame.display.set_mode((display_width, display_height))

def show_menu_w():     #игровое меню
    menu_bckgr = pygame.image.load("obj/menu.png")
    start_btn = Button(display, 300, 70)
    quit_btn = Button(display, 200, 70)
    show = True
    while show:         # цикл во время игры
        for event in pygame.event.get(): #  перебор событий
            # check for closing window
            if event.type == pygame.QUIT: # для выхода из игры
                pygame.quit()
                quit()
        display.blit(menu_bckgr, (0,0))
        print_text(display, "SET", display_width/2 - 200, 0, font_size = 300)
        start_btn.draw(display, display_width/2 - 150, display_height / 2, 'Start game', windows.game_win, 50)
        quit_btn.draw(display, display_width/2 - 100, display_height / 4 * 3, 'Quit', quit, 50)
        pygame.display.update()
        clock.tick(60)
