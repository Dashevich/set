import pygame
from functions import *
from Button import Button
import windows

display_width = 1200 #размеры дисплея
display_height = 700
display = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()

def score_wind(time_score):
    game_bckgr = pygame.image.load("obj/score.png")
    quit_btn1 = Button(display, 200, 70)
    play_again = Button(display, 300, 70)
    score = True
    while score:  # цикл во время игры
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # для выхода из игры
                pygame.quit()
                quit()
        display.blit(game_bckgr, (0, 0))
        print_text(display, "Your score", display_width / 2 - 175 , 50, font_size=70)
        print_text(display, "Your time: " + time_score, display_width / 2 - 170, 200, font_size=50)
        play_again.draw(display, display_width/2 - 150, display_height / 2, 'Play again', windows.game_win, 50)
        quit_btn1.draw(display, display_width/2 - 100, display_height / 4 * 3, 'Quit', quit, 50)
        pygame.display.update()
        clock.tick(60)