import pygame
import random
from functions import *
from Card import Card
from Button import Button
import windows
import copy
import functions

display_width = 1200 #размеры дисплея
display_height = 700
display = pygame.display.set_mode((display_width, display_height))
Set = []
screen = 0
jey = 0
stop = 0

print(Set)

person_set = []
right_sets = []

clock = pygame.time.Clock() # для кадров в сек

def params():
    global Set
    global stop
    global jey
    stop = 0
    jey = 0
    #Set = [[1, 0, 1, 1], [2, 1, 2, 2], [1, 0, 2, 1], [1, 2, 0, 2], [2, 0, 2, 2], [0, 2, 1, 0], [1, 2, 0, 1], [2, 1, 1, 1], [0, 2, 0, 2], [2, 2, 1, 1], [0, 2, 2, 0], [1, 0, 1, 2], [1, 0, 1, 0], [2, 2, 2, 1], [0, 2, 1, 1], [2, 0, 0, 0], [2, 2, 1, 0], [1, 1, 0, 1]]
    #Set = [[0,0,0,0], [0,0,1,1], [0,0,1,0], [0,1,0,0], [0,2,0,1], [0,1,1,1], [0,1,1,0], [0,2,0,2], [0,2,2,1], [1,0,0,0], [1,0,0,2], [1,0,1,0], [1,1,0,2], [1,2,0,2], [0,1, 2, 0], [0,2,1,0], [1,1,1,1], [2,2,2,2]]
    #Set = [[0,0,0,0], [0,0,1,1], [0,0,1,0], [0,1,0,0], [0,2,0,1], [0,1,1,1], [0,1,1,0], [0,2,0,2], [0,2,2,1], [1,0,0,0], [1,0,0,2], [1,0,1,0], [1,1,0,2], [1,2,1,2], [1,1,0,0], [1,2,1,1], [0,0,2,2], [2,2,2,2]]
    #Set = [[0,0,0,0], [0,0,1,1], [0,0,1,0], [0,1,0,0], [0,2,0,1], [0,1,1,1], [0,1,1,0], [0,2,0,2], [0,2,2,1], [1,0,0,0], [1,0,0,2], [1,0,1,0], [1,1,0,2], [1,1,1,0], [1,2,1,2], [1,1,0,0], [1,2,1,1], [1,2,2,2], [2,2,1,1], [2,2,0,2], [0,0,2,2]]
    #Set = [[0, 0, 0, 0], [0, 0, 1, 1], [0, 0, 1, 0], [0, 1, 0, 0], [0, 2, 0, 1], [0, 1, 1, 1], [0, 1, 1, 0], [0, 2, 0, 2], [0, 2, 2, 1], [1, 0, 0, 0], [1, 0, 0, 2], [1, 0, 1, 0], [1, 1, 0, 2], [1, 1, 1, 0], [1, 2, 1, 2], [1, 1, 0, 0], [1, 2, 1, 1], [1, 2, 2, 2], [2, 2, 1, 1], [2, 2, 0, 2], [0, 0, 2, 2]]
    #Set = [[0,0,0,0],[1,1,1,1],[2,2,2,2],[0,0,2,2],[0,0,1,1],[1,1,0,0]]
    for c in range(3):
       for f in range(3):
           for n in range(3):
               for s in range(3):
                   Set.append([c,f,n,s])
    print(Set, "go")
    random.shuffle(Set)

def game_cycle(): #главное меню
    params()
    global array
    game_bckgr = pygame.image.load("obj/game.jpg")
    game = True
    array = []
    create_card_arr()
    time = pygame.time.get_ticks()
    global screen
    screen = 0
    quit_btn = Button(display, 200, 70)
    while game:         # цикл во время игры
        for event in pygame.event.get(): #  перебор событий
            # check for closing window
            if event.type == pygame.QUIT: # для выхода из игры
                pygame.quit()
                quit()
        if screen == 1:
            Set = []
            time_score = str(((pygame.time.get_ticks() - time)//1000) // 60) + ":" + str(((pygame.time.get_ticks() - time)//1000) % 60)
            windows.score_win(time_score)
        #print(screen)
        display.blit(game_bckgr, (0,0))
        print_text(display, str(((pygame.time.get_ticks() - time)//1000) // 60) + ":" + str(((pygame.time.get_ticks() - time)//1000) % 60), 0, 0, (255, 255, 255))
        draw_array()
        check()
        quit_btn.draw(display, display_width - 200, display_height / 6 - 70, 'Quit', quit, 50)
        pygame.display.update()  # обновление
        clock.tick(60) # 60 кадров в секунду

def create_card_arr(): #создать массив карт на  поле
    global jey, screen, stop
    global array
    print(jey)
    jey1 = 4
    x = display_width/16
    y = display_height/16
    print(array)
    print(stop, 'DASHA', (4+jey)*3, len(Set))
    if len(Set) < (4+jey)*3 and stop == 1:
        print("y")
        screen = 1
    else:
        if len(Set) < 12:
            i1 = len(Set)//4 + 1
            j1 = len(Set)%4
        else:
            i1 = 3+jey
            j1 = jey1
        for i in range(i1):
            if i >= 2 + jey:
                jey1 = 6 - i
            if i == 4 and jey == 3:
                jey1+=1
            if i == i1-1 and len(Set) < 12:
                jey1 = j1
            for j in range(jey1):
                array.append(Card(display, int(x), int(y), int(display_width/8), int(display_height/8), Set[i*4+j][0], Set[i*4+j][1], Set[i*4+j][2], Set[i*4+j][3]))
                x += display_width*3/16
            y += display_height/16*3
            x = display_width/16
            if i == 4 and jey == 3:
                break
        print(Set)
        find_right()

def draw_array(): #отрисовать карты
    global array
    #print(len(array))
    right_sets = []
    num = 0
    for card in array:
        x = card.clicks(display)
        if x != None:
            if x not in person_set:
                person_set.append(x)
            else:
                person_set.remove(x)
            print(person_set)
        card.draw(display)
        num += 1
        #print(num)

        right_sets.append(card.show_info())

    #print(right_sets)

def check():  #проверка на сборку сета
    global Set, array, jey, card_arr
    global a, b, c, lene

    ind = 0
    if len(person_set) == 3:
        for i in range(4):
            if (person_set[0][i] == person_set[1][i] == person_set[2][i]) or (person_set[0][i] != person_set[1][i] != person_set[2][i] != person_set[0][i]):
                ind += 1
        if ind == 4:
            print(person_set[0], person_set[1],  person_set[2])
            print(Set)
            a = Set.index(person_set[0])
            b = Set.index(person_set[1])
            c = Set.index(person_set[2])
            if a > b:
                x = a
                a = b
                b = x
            if b > c:
                x = c
                c = b
                b = x
            if a > b:
                x = a
                a = b
                b = x
            Set.pop(c)
            Set.pop(b)
            Set.pop(a)
            lene = len(array)
            if len(Set) > lene:
                Set.insert(a, Set[lene - 3])
                Set.pop(lene - 2)
                Set.insert(b, Set[lene - 1])
                Set.pop(lene)
                Set.insert(c, Set[lene + 1])
                Set.pop(lene + 2)
            person_set.clear()

            print("yes")
            if jey > 0:
                jey -= 1

            array = []
            create_card_arr()


def find_right():
    global a, b, c, lene
    global stop
    global jey
    global array
    info = []
    info1 = []
    info2 = []
    ind = 0
    ind1 = 0
    if len(Set) < 12:
        jey1 = len(Set)
    else:
        jey1 = (4+jey)*3
    for card in range(0, jey1-2):
        info = array[card].show_info()
        for card1 in range(card+1, jey1-1):
            info1 = array[card1].show_info()
            for card2 in range(card1+1, jey1):
                ind = 0
                info2 = array[card2].show_info()
                #if jey != 0:
                #    print(array[12].show_info())
                #print(info, info1, info2)
                #print('-')
                for i in range(4):
                    if (info[i] == info1[i] == info2[i]) or (info[i] != info1[i] != info2[i] != info[i]):
                        #print(info[i], info1[i], info2[i])
                        ind += 1
                if ind == 4:
                    ind1 = 1
                    print("lets go", info, info1, info2)
    if ind1 != 0:
        stop = 0
    if ind1 == 0:
        jey += 1
        array = []
        stop = 1
        create_card_arr()

