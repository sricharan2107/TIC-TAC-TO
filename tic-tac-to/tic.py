#welcome to GOOGLE TIC -TAC -TO CLONE
import pygame , sys
import numpy as np

pygame.init()
WIDTH = 600
HEIGHT = 600
RED = (255,0,0)
LINE_COLOR =(23,145,135)
BG_COLOR =(28,170,156)
CIRCLE_COLOR = (239,231,200)
CROSS_COLOR=(66,66,66 )
BOARD_ROWS =3
BOARD_COLS =3
CIRCLE_RADIUS =60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
LINE_WIDTH = 15
SPACE = 55

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("TIC-TAC-TO")
screen.fill(BG_COLOR)
board = np.zeros((BOARD_ROWS,BOARD_COLS))
player =1
game_over = False
def draw_lines():
    pygame.draw.line(screen,LINE_COLOR,(0,200),(600,200),5)
    pygame.draw.line(screen,LINE_COLOR,(0,400),(600,400),5)
    pygame.draw.line(screen,LINE_COLOR,(200,0),(200,600),5)
    pygame.draw.line(screen,LINE_COLOR,(400,0),(400,600),5)
draw_lines()

def mark_square(row ,coloum,player):
    board[row][coloum] =player
#mark_square(0,0,1)
def available_square(row,coloum):
    return board[row][coloum] == 0
def is_board_full():
    for row in range(BOARD_ROWS):
        for cols in range(BOARD_COLS):
            if(board[row][cols]==0):
                return False
    return True
def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen,CIRCLE_COLOR,(int(col*200 +100),int(row*200+100)),CIRCLE_RADIUS,CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen,CROSS_COLOR,(col*200+SPACE,row*200+200-SPACE),(col *200+200-SPACE,row*200+SPACE) ,CROSS_WIDTH)
                pygame.draw.line(screen,CROSS_COLOR,(col*200+SPACE,row*200+SPACE),(col *200+200-SPACE,row*200+200-SPACE) ,CROSS_WIDTH)
#print(board)
def cheack_win(player):
    #vertical cheack
    for col in range(BOARD_COLS):
        if board[0][col]==player and board[1][col]==player and board[2][col]== player:
            draw_vertical_winning_line(col,player)
            return True
    # horizontal cheack
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1]==player and board[row][2]==player:
            draw_horizontal_winning_line(row,player)
            return True
    # original daigonal check
    if board[0][0] == player and board[1][1] == player and board[2][2] ==player:
        draw_asc_daigonal(player)
        return True
    #backword daigonal check
    if board[2][1] ==player and board[1][1]==player and board[1][2]==player:
        draw_dec_daigonal(player)
        return True 
    return False


def draw_vertical_winning_line(col,player):
    posx = col *200 +100
    if player ==1:
        color=CIRCLE_COLOR
    elif player == 2:
        color= CROSS_COLOR
    pygame.draw.line(screen,color,(posx,15),(posx,HEIGHT-15),15)
def draw_horizontal_winning_line(row,player):
    posy = row * 200 +100
    if player ==1:
        color=CIRCLE_COLOR
    elif player == 2:
        color= CROSS_COLOR
    pygame.draw.line(screen,color,(15,posy),(WIDTH-15,posy),15)

def draw_asc_daigonal(player):
    if player ==1:
        color=CIRCLE_COLOR
    elif player == 2:
        color= CROSS_COLOR
    pygame.draw.line(screen,color,(15,HEIGHT-15),(WIDTH-15,15),15)

def draw_dec_daigonal(player):
    if player ==1:
        color=CIRCLE_COLOR
    elif player == 2:
        color= CROSS_COLOR
    pygame.draw.line(screen,color,(15,15),(WIDTH-15,HEIGHT -15),15)

def restart():
    screen.fill(BG_COLOR)
    draw_lines()
    player = 1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] =0
while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mousex = event.pos[0] # x-axis position
            mousey =event.pos[1] #y-axis position
            clicked_row = int( mousey//200)
            clicked_col = int( mousex//200)
            if available_square(clicked_row,clicked_col) :
                if player ==1: 
                    mark_square(clicked_row,clicked_col,player)
                    if cheack_win(player):
                        game_over=True
                    player =2
                elif player==2:
                    mark_square(clicked_row,clicked_col,player)
                    if cheack_win(player):
                        game_over=True
                    player =1
                draw_figures()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restart()
                
    pygame.display.update()  