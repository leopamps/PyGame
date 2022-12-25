import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

larguraTela = 640
alturaTela = 480
x_snake = int(larguraTela/2)
y_snake = int(alturaTela/2)

speed =20
x_control = speed
y_control = 0

x_apple = randint(40, 600)
y_apple = randint(50, 430)
points = 0
fonte = pygame.font.SysFont('arial', 40, True, False)

'''não tem comando pra mudar a cor de fundo'''
tela = pygame.display.set_mode((larguraTela, alturaTela))
pygame.display.set_caption('Joguinho Bunito')
clock = pygame.time.Clock()
list_snake = []
comprimento_inicial = 5
dead = False


def increase_snake(list_snake):
   for xey in list_snake:
        pygame.draw.rect(tela, (0, 255, 0), (xey[0], xey[1], 25, 25))


def restart_game():
    global points, comprimento_inicial,x_apple,x_snake,y_snake,y_apple,list_snake,list_head,dead
    points = 0
    comprimento_inicial = 5
    x_snake = int(larguraTela/2)
    y_snake = int(alturaTela/2)
    list_snake = []
    list_head = []
    x_apple = randint(40, 600)
    y_apple = randint(50, 430)
    dead = False


while True:
    clock.tick(20)
    tela.fill((100,100,100))
    mensagem = f'Pontos: {points}'
    texto_formatado = fonte.render(mensagem, True, (0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_control == speed:
                    pass
                else:
                    x_control = -speed
                    y_control = 0
            if event.key == K_d:
                if x_control == -speed:
                    pass
                else:
                    x_control = speed
                    y_control = 0
            if event.key == K_s:
                if y_control == -speed:
                    pass
                else:
                    x_control = 0
                    y_control = speed
            if event.key == K_w:
                if y_control == speed:
                    pass
                else:
                    x_control = 0
                    y_control = -speed

    x_snake += x_control
    y_snake += y_control

    snake = pygame.draw.rect(tela, (0, 255, 0), (x_snake, y_snake, 25, 25))
    apple = pygame.draw.rect(tela, (255, 0, 0), (x_apple, y_apple, 25, 25))

    if snake.colliderect(apple):
        x_apple = randint(40, 600)
        y_apple = randint(50, 430)
        points += 1
        comprimento_inicial +=3

    list_head = []
    list_head.append(x_snake)
    list_head.append(y_snake)

    list_snake.append(list_head)

    if list_snake.count(list_head) > 1:
        font2 = pygame.font.SysFont('arial', 20, True, True)
        mensagem = 'Game Over! Pressione R para reiniciar'
        texto_formatado = font2.render(mensagem, True, (0, 0, 0))
        ret_text = texto_formatado.get_rect()

        '''não sei que houve, mas esse som não tá funcionando'''
        #death_music = pygame.mixer.music.load('Reverb Fart - Sound Effect (HD).mp3')
        #pygame.mixer.music.play()

        dead = True

        while dead:
            tela.fill((100, 100, 100))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        restart_game()

            ret_text.center = (larguraTela//2, alturaTela//2)
            tela.blit(texto_formatado, ret_text)
            pygame.display.update()

    if x_snake > larguraTela:
        x_snake = 0
    if x_snake < 0:
        x_snake = larguraTela
    if y_snake < 0:
        y_snake = alturaTela
    if y_snake > alturaTela:
        y_snake = 0

    if len(list_snake) > comprimento_inicial:
        del list_snake[0]

    increase_snake(list_snake)

    tela.blit(texto_formatado, (450, 40))
    pygame.display.update()
