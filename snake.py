import pygame, random
from pygame.locals import *

#Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

#Variaveis
direcao = "ESQUERDA"
qtdePontos = 0

def on_grid_random():
    x = random.randint(0,590)
    y = random.randint(60,590)
    return (x//10 * 10, y//10 * 10)

def colisaoCelulas(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

def colisaoBorda(c1):
    if c1[0] > 590 or c1[0] < 0 or c1[1] > 590 or c1[1] <= 50:
        return True
        

#Inicia o pygame
pygame.init()
screen = pygame.display.set_mode((600,600))                  #Tamanho da tela
pygame.display.set_caption('Snake') #Titulo da tela

fonte = pygame.font.SysFont('Comis sans ms', 40)
labelScore = fonte.render('Score: ', 1, WHITE)

snake = [(200, 200), (210, 200), (220,200), (230,200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill(WHITE)

apple_pos = on_grid_random()
apple = pygame.Surface((10,10))
apple.fill((255,0,0))

TICK = 10
clock = pygame.time.Clock()
while True:
    clock.tick(TICK)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            
        if event.type == KEYDOWN:
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

    if colisaoBorda(snake[0]):
        print('Voce perdeu 1')
        pygame.quit()
        break

    if colisaoCelulas(snake[0], apple_pos):
        qtdePontos += 10
        apple_pos = on_grid_random()
        snake.append((0,0))
    
    for i in range(1, len(snake)):
        if(colisaoCelulas(snake[0], snake[i])):
            print('Voce perdeu 2')
            pygame.quit()
            break

    for i in range(len(snake)-1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])
        

    if direcao == "CIMA":
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if direcao == "BAIXO":
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if direcao == "DIREITA":
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if direcao == "ESQUERDA":
        snake[0] = (snake[0][0] - 10, snake[0][1])
    
    labelPontos = fonte.render(str(qtdePontos), True, (255, 255, 255))
    screen.fill((0,0,0))
    screen.blit(labelScore, (10, 10))
    screen.blit(labelPontos, (110, 10))
    screen.blit(apple, apple_pos)


    linhaBranca = pygame.draw.line(screen, WHITE, [10,50], [590, 50], 2)
    pygame.display.flip()
    for pos in snake:
        screen.blit(snake_skin,pos)

    pygame.display.update()



    