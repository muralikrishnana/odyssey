import random
import pygame
from pygame.locals import *
from sys import exit
import numpy
exit1 = [0,0,0,0,0,0]
screen_width, screen_height= 800, 600
bg = (0,0,0)
screen = pygame.display.set_mode((screen_width, screen_height), FULLSCREEN, 32)
pygame.display.set_caption("ODYSSEY")
pygame.init()
title_width, title_height = 350, 70
Green = (34,139,34)
blink = False

Team_name = "MARSHMALLOW"
a = "509868"
password = int(a)

blink_index = 0
validating_text = "Validating"
validating_dot = []
validating_index = 0
accept_input = False
final_clue = False

pw = ""
pswrd = 0
pa = ""
validate = False
pass1 = False

home_font = pygame.font.SysFont("UBUNTU", 15)
sudoku_font = pygame.font.SysFont("UBUNTU", 30)
prompt = home_font.render("ENTER PASSWORD : ", True, Green)
enter = home_font.render("PRESS ENTER TO ENTER THE SYSTEM", True, Green)
prompt_width = prompt.get_width()
prompt_height = prompt.get_height()
first_text_height = 300
enter_prompt = False

pwd = home_font.render("_", True, Green)

intro = True

home = False

num1_x = []
num2_x = []
corsor_pos = 0
loc = 0

Red = (255,0,0)

bruteforce = []
number = 0
print_num = False
print_count = 0
num1_x = []
num1_y = []
item_x = 0
item_y = 0
page1 = False
access = home_font.render("Access Granted...", True, Green)

Front_screen = False

s7 = []
perfect_entry = False
valid_click = False
sudoku = False
sudoku_complete = False
total_view = 0
s1 = [  [4,6,1,9,2,7,5,3,8],
        [8,5,2,3,1,6,4,7,9],
        [7,9,3,8,4,5,2,6,1],
        [2,7,8,4,9,1,6,5,3],
        [1,4,6,2,5,3,9,8,7],
        [5,3,9,6,7,8,1,4,2],
        [6,2,7,1,3,4,8,9,5],
        [3,1,4,5,8,9,7,2,6],
        [9,8,5,7,6,2,3,1,4] ]
cross = [   ['A','P','Q','W','T','G','H','Z','C','P','T','R','E','W','T'],
            ['T','A','L','U','M','N','I','P','S','Y','Q','L','A','P','Z'],
            ['O','I','S','W','B','L','S','R','Q','L','D','S','R','H','J'],
            ['Q','J','P','S','C','V','E','O','W','L','X','S','T','Y','L'],
            ['Y','D','S','R','H','J','W','C','M','S','W','E','L','W','J'],
            ['U','E','M','N','C','S','B','T','Z','N','P','K','U','E','G'],
            ['P','B','L','L','A','P','T','Y','Y','H','B','L','E','R','Y'],
            ['S','P','I','M','A','S','G','Q','P','W','S','P','O','T','O'],
            ['Y','P','K','U','E','G','S','Z','Q','L','L','P','D','N','P'],
            ['L','I','N','E','W','B','L','O','C','K','L','S','R','Q','L'],
            ['Q','J','P','S','C','V','E','O','W','L','X','S','T','Y','L'],
            ['T','A','K','Z','R','V','C','P','S','Y','Q','L','A','P','Z'],
            ['S','P','O','T','L','E','L','Q','P','W','S','P','O','T','O'] ]

s2 = [] #display matrix
s3 = [] #remaining matrix
for i in range (9):
    s2.append([])
    s3.append([])
    for j in range (9):
        s2[i].append('')
        s3[i].append('')
s4 = [] # for user input
for i in range (9):
    s4.append([])
    s7.append([])
    for j in range (9):
        s4[i].append('')
        s7[i].append('')
s5 = s4 # backup
for i in range (0,9):
    for j in range (0,8): #fill random
        sel = random.randint(0,8)
        for k in range (0,8):
            if k != sel:
                s3[i][k] = s1[i][k]
                s3[i][sel] = ''
        s2[i][sel] = s1[i][sel]
for i in range (0,9):
    for j in range(0,9):
        if s2[i][j] == s3[i][j]:
            s3[i][j] = ''
soln_array = []
soln = []
for i in range (0,9):
    for j in range (0,9):
        soln_array.append(s3[i][j])
clicked = False
filled_nos = []
num_detail = []
crossword = False
#img load
stacs_width, stacs_height = 80, 90
nss_width, nss_height = 130, 140
od_width, od_height = 250, 300
od = pygame.transform.scale(pygame.image.load('odyssey.png'), (od_width, od_height))
nss = pygame.transform.scale(pygame.image.load('nss.png'), (nss_width, nss_height))
title = pygame.transform.scale(pygame.image.load('ody.png'), (title_width, title_height))
stacs = pygame.transform.scale(pygame.image.load('stacs.png'), (stacs_width, stacs_height))
invalid_entry = False

while True:
    #General
    board_error = 0
    flag = 0
    screen.fill(bg)
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == MOUSEBUTTONDOWN:
            if accept_input:
                click_x, click_y = pygame.mouse.get_pos()
                clicked = True
        elif event.type == KEYDOWN :
            if event.key == K_c :
                exit1[0] = 1
            if exit1[0] and event.key == K_h :
                    exit1[1] = 1
            if exit1[0] and exit1[1] and event.key == K_i :
                    exit1[2] = 1
            if exit1[0] and exit1[1] and exit1[2] and event.key == K_k :
                    exit1[3] = 1
            if exit1[0] and exit1[1] and exit1[2] and exit1[3] and event.key == K_k :
                    exit1[4] = 1
            if exit1[0] and exit1[1] and exit1[2] and exit1[3] and exit1[4] and event.key == K_u :
                    exit1[5] = 1
            if (event.key != K_c and event.key != K_h and event.key !=K_i and event.key !=K_k and event.key !=K_u):
                exit1 = [0,0,0,0,0,0]
            if intro:
                if event.key == K_RETURN:
                    intro = False
                    home = True
            if Front_screen:
                if event.key == K_RETURN:
                    Front_screen = False
                    home = True
            if home:
                if (K_0 <= event.key <= K_9) and len(pa)<12:
                    num = chr(event.key)
                    pa += str(num+" ")
                    loc += 11
                if pa != "":
                    if event.key == K_BACKSPACE and validate == False:
                        pa = pa[:-2]
                        loc -= 11
                if len(pa) == 12:
                    enter_prompt = True
                    if event.key == K_RETURN:
                        validate = True
                        conv_pwd = 1
                if event.key == K_c:
                    home = False
                    Front_screen = True
                if len(pa) < 12:
                    enter_prompt = False
            if page1 and not pass1:
                if event.key == K_RETURN:
                    page1 = False
                    home = True
            if page1 and pass1:
                if event.key == K_RETURN:
                    page1 = False
                    sudoku = True
                    accept_input = True
            if sudoku:
                if event.key == K_c:
                    for i in range(0,9):
                        for j in range(0,9):
                            s7[i][j] = s2[i][j]
                    for i in range (0,9):
                        for j in range (0,9):
                            if (s4[i][j] != ''):
                                s7[i][j] = s4[i][j]
                    if numpy.array_equal(s7,s1):
                                perfect_entry = True
                                sudoku = False
                                sudoku_complete = False
                                accept_input = False
                    else:
                                invalid_entry = True
                                sudoku = False
                                sudoku_complete = False
                if event.key == K_r:
                    for i in range (9):
                        for j in range (9):
                            s4[i][j] = ''

            if sudoku and valid_click:
                if (K_0 < event.key <= K_9):
                    num1 = chr(event.key) #num1 -> iserted by user
                    s4[u][v] = int(num1)
                if event.key == K_BACKSPACE:
                    s4[u][v] = ''

            if invalid_entry:
                    if event.key == K_RETURN:
                        invalid_entry = False
                        sudoku = True
                        sudoku_complete = True
            if perfect_entry:
                    if event.key == K_RETURN:
                        perfect_entry = False
                        final_clue = True
                        invalid_entry = False
            if final_clue:
                    if event.key == K_n:
                        final_clue = False
                        crossword = True
            if crossword:
                if event.key == K_c:
                    final_clue = True
                    crossword = False
    if (exit1[0] and exit1[1] and exit1[2] and exit1[3] and exit1[4] and exit1[5]):
        exit()

    #intro
    if intro:
        screen.blit(stacs, (3*(screen_width/4),60))
        screen.blit(nss, (screen_width/4-80, 30))
        screen.blit(od, (screen_width/2 - od_width/2, 150))

        od_ar = home_font.render('Welcome Team {}'.format(Team_name),True,Green)
        screen.blit(od_ar, (screen_width/2 - od_ar.get_width()/2,screen_height-100))
        od_ar = home_font.render('Hit Enter to begin the run!',True,Green)
        screen.blit(od_ar, (screen_width/2 - od_ar.get_width()/2,screen_height-60))


    #Front_screen
    if not home and Front_screen:
        clue1 = "In the building you are, somewhere in the dark, lies a name that connect you with this game."
        clue2 = home_font.render("Keep your brain running, they have a secret your eyes can't see.", True, Green)
        first_clue = home_font.render(clue1, True, Green)
        screen.blit(first_clue, ((screen_width/2)-(first_clue.get_width()/2),(screen_height/2-10)))
        screen.blit(clue2, ((screen_width/2)-(clue2.get_width()/2),(screen_height/2)+10))
        clue1 = "Press Enter to go back"
        first_clue = home_font.render(clue1, True, Green)
        screen.blit(first_clue, ((screen_width/2)-(first_clue.get_width()/2),(screen_height/2+50)))

    #Home
    if home:
        screen.blit(title, ((screen_width/2)-(title_width/2),(screen_height/4)-(title_height/2)))
        screen.blit(prompt, ((screen_width/2)-(prompt_width/2),first_text_height))
        cursor_pos = (screen_width/2)-(pwd.get_width()+25) + loc
        if blink_index > 100 and blink_index < 400:
            screen.blit(pwd, (cursor_pos, first_text_height + 30))
        if blink_index > 500:
            blink_index = 0
        blink_index += 1
        screen.blit(home_font.render(pa, True, Green), ((screen_width/2)-(pwd.get_width()+25), first_text_height + 30))
        clue1_prompt = home_font.render("Don't know the passcode? Press C, somebody has left you a clue.", True, Green)
        screen.blit(clue1_prompt, ((screen_width/2)-(clue1_prompt.get_width()/2), screen_height-100))

        if enter_prompt:
            screen.blit(enter, ((screen_width/2)-(enter.get_width()/2), first_text_height + 80))
        if validate:
            if conv_pwd:
                pw = pa
                conv_pwd = 0
            pswrd = int(pw.replace(" ",""))
            if (pswrd == password):
                home = False
                page1 = True
                pass1 = True
            if pswrd != password:
                pa = ""
                validate = False
                enter_prompt = False
                pass1 = False
                home = False
                loc = 0
                page1 = True
    #page1
    if page1 and pass1:
        access = home_font.render("ACCESS GRANTED...", True, Green)
        screen.blit(access, ((screen_width/2)-(access.get_width()/2), first_text_height - 20))
        access = home_font.render("Press Enter To Continue", True, Green)
        screen.blit(access, ((screen_width/2)-(access.get_width()/2), first_text_height+20))
    elif page1 and not pass1:
        access = home_font.render("ACCESS DENIED...", True, Green)
        screen.blit(access, ((screen_width/2)-(access.get_width()/2), first_text_height - 20))
        access = home_font.render("Press Enter To Retry...", True, Green)
        screen.blit(access, ((screen_width/2)-(access.get_width()/2), first_text_height+20))

    #sudoku
    if sudoku:
        x,y = screen_width/2 - 180, 80
        pygame.draw.rect(screen, Green,(x, y,360,360), 5)
        for i in range (0, 3):
            for j in range(3):
                pygame.draw.rect(screen, Green, (x+i*120, y+j*120, 120, 120), 5)
        for i in range(0, 9):
            for j in range (0, 9):
                num = sudoku_font.render(str(s2[i][j]), True, Green)
                pygame.draw.rect(screen, Green,(x+i*40, y+j*40 ,40,40), 2 )
                if (s2[i][j]==''):
                    num = sudoku_font.render(str(s4[i][j]), True, Red)
                    screen.blit(num,(x+i*40+10, y+j*40+3))
                else:
                    screen.blit(num,(x+i*40+10, y+j*40+3))


        if accept_input:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if ((0<= mouse_x - x <= screen_width) and (0 <= mouse_y-y <= screen_height)):
                    i = int((mouse_x-x)/40)
                    j = int((mouse_y-y)/40)
                    if(i>=0 and i<=8 and j>=0 and j<=8):
                        if s2[i][j] == '':
                            pygame.draw.rect(screen, (255,0,0), (x+i*40+2, y+j*40+2, 36, 36), 2)
                if clicked:
                    if ((0<= click_x - x <= screen_width) and (0 <= click_y-y <= screen_height)):
                        u = int((click_x-x)/40)
                        v = int((click_y-y)/40)
                        if(u>=0 and u<=8 and v>=0 and v<=8):
                            if s2[u][v] == '':
                                pygame.draw.rect(screen, (255,0,0), (x+u*40+2, y+v*40+2, 36, 36), 2)
                                valid_click = True
                            else: valid_click = False
                    else: valid_click = False
        access = home_font.render("Press C to SUBMIT SUDOKU", True, Green)
        clear = home_font.render("Press R to RESET", True, Green)
        screen.blit(clear, ((screen_width/2)-(clear.get_width()/2), first_text_height + 220))
        screen.blit(access, ((screen_width/2)-(access.get_width()/2), first_text_height + 170))
    if invalid_entry:
        access = home_font.render("INCORRECT SOLUTION!", True, Green)
        screen.blit(access, ((screen_width/2)-(access.get_width()/2), first_text_height - 20))
        access = home_font.render("Press Enter To Edit", True, Green)
        screen.blit(access, ((screen_width/2)-(access.get_width()/2), first_text_height+20))
    if perfect_entry:
        access = home_font.render("YOU HAVE UNLOCKED THE SECRET!", True, Green)
        screen.blit(access, ((screen_width/2)-(access.get_width()/2), first_text_height - 20))
        access = home_font.render("Press Enter To Reveal", True, Green)
        screen.blit(access, ((screen_width/2)-(access.get_width()/2), first_text_height+20))
    if final_clue:
        access1 = home_font.render("Dear Team {} you did a great work :-)".format(Team_name), True, Green)
        screen.blit(access1, ((screen_width/2)-(access1.get_width()/2), screen_height/2 - 80))
        access1 = home_font.render("Now read this carefully. If you press N, you will see a crossword puzzle.", True, Green)
        screen.blit(access1, ((screen_width/2)-(access1.get_width()/2), screen_height/2 - 40))
        access1 = home_font.render("The name of your next destination is hidden in the puzzle.", True, Green)
        screen.blit(access1, ((screen_width/2)-(access1.get_width()/2), screen_height/2))
        access1 = home_font.render("Crack the puzzle and rush to the destination in the puzzle.", True, Green)
        screen.blit(access1, ((screen_width/2)-(access1.get_width()/2), screen_height/2+30))
        access1 = home_font.render("For your great effort we have a hint for you.", True, Green)
        screen.blit(access1, ((screen_width/2)-(access1.get_width()/2), screen_height/2+60))
        access1 = home_font.render("HINT: The destination is a building in our campus.", True, Green)
        screen.blit(access1, ((screen_width/2)-(access1.get_width()/2), screen_height/2+150))
    if crossword:
        let = sudoku_font.render('A', True, Green)
        pos = screen_width/2 - ((let.get_width()/2)*6 + 180),20
        for i in range (12):
            for j in range (12):
                let = sudoku_font.render(cross[i][j], True, Green)
                screen.blit(let, (pos[0]+i*45, pos[1]+j*45))
        access1 = home_font.render("Press C to see hint.", True, Green)
        screen.blit(access1, ((screen_width/2)-(access1.get_width()/2), screen_height-30))
    pygame.display.update()
