import pygame, random, time
from pygame.locals import *

#Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BORDA = (22, 50, 76)

#Variaveis
direcao = "ESQUERDA"
qtdePontos = 0
qtdeComprimento = 0
emPause = False
TAM = 10
DIS = 1

def on_grid_random():
    x = random.randint(3,61)
    y = random.randint(3,44)
    #random.randint(4,45)
    return (x*10, y*10)

def colisaoCelulas(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

def colisaoBorda(c1):
    if c1[0] > 610 or c1[0] < 30 or c1[1] > 440 or c1[1] < 30:
        return True

#Inicia o pygame
pygame.init()
screen = pygame.display.set_mode((650,500))  #Tamanho da tela
pygame.display.set_caption('Snake')          #Titulo da tela

fonteComicBranca = pygame.font.SysFont('Comis sans ms', 25)
labelScore = fonteComicBranca.render('High Score: ', True, WHITE)
labelLenght = fonteComicBranca.render('Lenght: ', True, (255, 255, 255))

fonteComicVermelha = pygame.font.SysFont('Comic sans ms', 16, False, True)
labelPause = fonteComicVermelha.render('Jogo em pause, pressione espaço para continuar...', True, RED)

snake = [(200, 200), (201+TAM, 200), (201+TAM*2,200), (201+TAM*3,200)]
snake_skin = pygame.Surface((TAM,TAM))
snake_skin.fill(GREEN)

apple_pos = on_grid_random()
apple = pygame.Surface((TAM,TAM))
apple.fill((255,0,0))

clock = pygame.time.Clock()
while True:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
            
        if event.type == KEYDOWN:
            if event.key == K_1:
                snake.append((0,0))
                qtdePontos += 10
                qtdeComprimento += 1
            if event.key == K_SPACE:
                if emPause == False:
                    emPause = True
                else:
                    emPause = False
            if event.key == K_UP:
                if direcao != "BAIXO":
                    direcao = "CIMA"
            if event.key == K_DOWN:
                if direcao != "CIMA":
                    direcao = "BAIXO"
            if event.key == K_LEFT:
                if direcao != "DIREITA":
                    direcao = "ESQUERDA"
            if event.key == K_RIGHT:
                if direcao != "ESQUERDA":
                    direcao = "DIREITA"
            time.sleep(0.06)

    if emPause == True:
        screen.blit(labelPause, (260, 0))
        pygame.display.flip()
        continue

    if colisaoBorda(snake[0]):
        pygame.quit()
        quit()

    if colisaoCelulas(snake[0], apple_pos):
        qtdePontos += 10
        apple_pos = on_grid_random()
        snake.append((0,0))
        qtdeComprimento += 1
    
    for i in range(1, len(snake)):
        if(colisaoCelulas(snake[0], snake[i])):
            pygame.quit()
            quit()

    for i in range(len(snake)-1, 0, -1):
        if direcao == "CIMA":
            snake[i] = (snake[i-1][0], snake[i-1][1]+DIS)
        if direcao == "BAIXO":
            snake[i] = (snake[i-1][0], snake[i-1][1]-DIS)
        if direcao == "DIREITA":
            snake[i] = (snake[i-1][0]-DIS, snake[i-1][1])
        if direcao == "ESQUERDA":
            snake[i] = (snake[i-1][0]+DIS, snake[i-1][1])

    if direcao == "CIMA":
        snake[0] = (snake[0][0], snake[0][1] - TAM)
    if direcao == "BAIXO":
        snake[0] = (snake[0][0], snake[0][1] + TAM)
    if direcao == "DIREITA":
        snake[0] = (snake[0][0] + TAM, snake[0][1])
    if direcao == "ESQUERDA":
        snake[0] = (snake[0][0] - TAM, snake[0][1])

    labelPontos = fonteComicBranca.render(str(qtdePontos), True, (255, 255, 255))
    labelLenghtQtde = fonteComicBranca.render(str(qtdeComprimento), True, (255, 255, 255))

    screen.fill((0,0,0))
    screen.blit(apple, apple_pos)
    
    borda1 = pygame.draw.line(screen, BORDA, [0,0], [650, 0], 40) #BORDA DE CIMA
    borda2 = pygame.draw.line(screen, BORDA, [0,0], [0, 500], 40) #BORDA DA ESQUERDA
    borda3 = pygame.draw.line(screen, BORDA, [650,500], [650, 0], 40) #BORDA DE BAIXO
    borda4 = pygame.draw.line(screen, BORDA, [0,500], [650, 500], 90) #BORDA DA DIREITA
    
    screen.blit(labelLenght, (30, 470))
    screen.blit(labelLenghtQtde, (110, 470))
    screen.blit(labelScore, (500, 470))
    screen.blit(labelPontos, (608, 470))
    pygame.display.flip()
    for pos in snake:
        screen.blit(snake_skin,pos)

    pygame.display.update()



    