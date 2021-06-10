#importações
import pygame
from pygame.locals import *
from random import randint

#função para randomizar a maça
def on_grid_random():
    x = randint(0, 590)
    y = randint(0, 590)
    return x // 10 * 10, y // 10 * 10 #retornar em valor exato, para não dar diferença entre a maça e a cobra

#função para pegar a maça
def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

#botões
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

#tela
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')

#cobra
snake = [(200, 200), (210, 200), (220, 200)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((255, 255, 255))

#maça
apple_pos = on_grid_random()
apple = pygame.Surface((10, 10))
apple.fill((255, 0, 0))

#direção inicial
my_direction = LEFT

#movimento da cobra
clock = pygame.time.Clock()

#fonte
font = pygame.font.Font('freesansbold.ttf', 18)
score = 0

game_over = False

while not game_over:
    clock.tick(15)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            
        #Direção
        if event.type == KEYDOWN:
            if event.key == K_UP and my_direction != DOWN:
                my_direction = UP
            if event.key == K_DOWN and my_direction != UP:
                my_direction = DOWN
            if event.key == K_RIGHT and my_direction != LEFT:
                my_direction = RIGHT
            if event.key == K_LEFT and my_direction != RIGHT:
                my_direction = LEFT
    
    #pegou a maça
    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0, 0))
        score += 1
        
    # game over batendo no limite da tela
    if snake[0][0] == 600 or snake[0][1] == 600 or snake[0][0] < 0 or snake[0][1] < 0:
        game_over = True
        break
    
    #game over batendo na propria cobra
    for i in range(1, len(snake) - 1):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            game_over = True
            break

    if game_over:
        break
    
    # movimento corpo
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i - 1][0], snake[i - 1][1])
    
    #direção
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])

    screen.fill((0, 0, 0))
    screen.blit(apple, apple_pos)
    
    score_font = font.render(f'Score: {score}', True, (255, 255, 255))
    score_rect = score_font.get_rect()
    score_rect.topleft = (600 - 120, 10)
    screen.blit(score_font, score_rect)

    for pos in snake:
        screen.blit(snake_skin, pos)

    pygame.display.update()
    
    while True:
    game_over_font = pygame.font.Font('freesansbold.ttf', 75)
    game_over_screen = game_over_font.render('Game Over', True, (255, 255, 255))
    game_over_rect = game_over_screen.get_rect()
    game_over_rect.midtop = (600 / 2, 10)
    screen.blit(game_over_screen, game_over_rect)
    pygame.display.update()
    pygame.time.wait(500)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
              
