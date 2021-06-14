import pygame
import random

# cores do projeto
PRETO = 0, 0, 0
BRANCO = 255, 255, 255
VERDE = 0, 255, 0
ROXO = 148, 0, 211
VERMELHO = 255, 0, 0

# tela jogo
fim = False
tamanho = 800, 600
tela = pygame.display.set_mode(tamanho)
tela_retangulo = tela.get_rect()

# Primeira Raquete
class Raquete1:
    def __init__(self, tamanho):
        self.imagem = pygame.Surface(tamanho)
        self.imagem.fill(VERDE)
        self.imagem_retangulo = self.imagem.get_rect()
        self.velocidade = 15

    def move(self, x, y):
        self.imagem_retangulo[0] += x
        self.imagem_retangulo[1] += y

    def atualiza(self, tecla):
        if tecla[pygame.K_w]:
            self.move(0, -1)

        if tecla[pygame.K_s]:
            self.move(0, 1)
        self.imagem_retangulo.clamp_ip(tela_retangulo)

    def realiza(self):
        tela.blit(self.imagem, self.imagem_retangulo)

# Segunda Raquete
class Raquete2:
    def __init__(self, tamanho):
        self.imagem = pygame.Surface(tamanho)
        self.imagem.fill(ROXO)
        self.imagem_retangulo = self.imagem.get_rect()
        self.velocidade = 15
        self.imagem_retangulo[0] = 800

    def move(self, x, y):
        self.imagem_retangulo[0] += x
        self.imagem_retangulo[1] += y

    def atualiza(self, tecla):
        if tecla[pygame.K_UP]:
            self.move(0, -1)

        if tecla[pygame.K_DOWN]:
            self.move(0, 1)
        self.imagem_retangulo.clamp_ip(tela_retangulo)

    def realiza(self):
        tela.blit(self.imagem, self.imagem_retangulo)

# Bola        
class Bola:
    def __init__(self, tamanho):
        self.imagem = pygame.Surface(tamanho)
        self.imagem.fill(VERMELHO)
        self.imagem_retangulo = self.imagem.get_rect()
        self.velocidade = 1
        self.set_bola()

    def aleatorio(self):
        while True:
            num = random.uniform(-1.0, 1.0)
            if -0.5 < num < 0.5:
                continue
            else:
                return num

    def set_bola(self):
        x = self.aleatorio()
        y = self.aleatorio()
        self.imagem_retangulo.x = tela_retangulo.centerx
        self.imagem_retangulo.y = tela_retangulo.centery
        self.velo = [x, y]

    def move(self):
        self.imagem_retangulo[0] += self.velo[0] * self.velocidade
        self.imagem_retangulo[1] += self.velo[1] * self.velocidade

    def atualiza(self):
        self.move()
        self.imagem_retangulo.clamp_ip(tela_retangulo)

    def realiza(self):
        tela.blit(self.imagem, self.imagem_retangulo)

# Tamanho         
raquetea = Raquete1((10, 100))
raqueteb = Raquete2((10, 100))
bola = Bola((15, 15))

# Jogo
while not fim:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            fim = True
    tecla = pygame.key.get_pressed()
    tela.fill(PRETO)
    raquetea.realiza()
    raqueteb.realiza()
    bola.realiza()
    raquetea.atualiza(tecla)
    raqueteb.atualiza(tecla)
    bola.atualiza()
    pygame.display.update()
