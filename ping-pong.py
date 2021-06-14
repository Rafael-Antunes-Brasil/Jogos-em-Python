import pygame
import random

# cores
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
        self.velocidade = 3
        self.imagem_retangulo[0] = 0

    def move(self, x, y):
        self.imagem_retangulo[0] += x * self.velocidade
        self.imagem_retangulo[1] += y * self.velocidade

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
        self.velocidade = 3
        self.imagem_retangulo[0] = 800

    def move(self, x, y):
        self.imagem_retangulo[0] += x * self.velocidade
        self.imagem_retangulo[1] += y * self.velocidade

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
        self.altura, self.largura = tamanho
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
        self.pos = list(tela_retangulo.center)

    def colide_parede(self):
        score1 = score2 = 0
        if self.imagem_retangulo.y < 0 or self.imagem_retangulo.y > tela_retangulo.bottom - self.altura:
            self.velo[1] *= -1

        if self.imagem_retangulo.x < 0 or self.imagem_retangulo.x > tela_retangulo.right - self.largura:
            self.velo[0] *= -1
            if self.imagem_retangulo.x == 0:
                score2 += 1
            if self.imagem_retangulo.x == 800:
                score1 += 1

    def colide_raquetea(self, raquete_rect):
        if self.imagem_retangulo.colliderect(raquete_rect):
            # self.velo *= -1
            print('Boa')

    def colide_raqueteb(self, raquete_rect):
        if self.imagem_retangulo.colliderect(raquete_rect):
            # self.velo *= -1
            print('Boa')

    def move(self):
        self.pos[0] += self.velo[0] * self.velocidade
        self.pos[1] += self.velo[1] * self.velocidade
        self.imagem_retangulo.center = self.pos

    def atualiza(self, raquete_rect):
        self.colide_parede()
        self.colide_raquetea(raquete_rect)
        self.colide_raqueteb(raquete_rect)
        self.move()

    def realiza(self):
        tela.blit(self.imagem, self.imagem_retangulo)

# Placar Jogador 1
class Placara:
    def __init__(self):
        pygame.font.init()
        self.fonte = pygame.font.Font(None, 36)
        self.pontos = 10

    def contagem(self):
        self.text = self.fonte.render('Pontos = ' + str(self.pontos), 1, (255, 255, 255))
        self.textpos = self.text.get_rect()
        self.textpos = tela.get_width()
        tela.blit(self.text, self.textpos)
        tela.blit(tela, (0, 0))

# Placar Jogador 2
class Placarb:
    def __init__(self):
        pygame.font.init()
        self.fonte = pygame.font.Font(None, 36)
        self.pontos = 10

    def contagem(self):
        self.text=self.fonte.render('Pontos = ' + str(self.pontos), 1, (255, 255, 255))
        self.textpos = self.text.get_rect()
        self.textpos = tela.get_width()
        tela.blit(self.text, self.textpos)
        tela.blit(tela, (0, 0))

# Tamanho
raquetea = Raquete1((10, 100))
raqueteb = Raquete2((10, 100))
bola = Bola((15, 15))
placar1 = Placara
placar2 = Placarb

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
    bola.atualiza(raquetea.imagem_retangulo)
    bola.atualiza(raqueteb.imagem_retangulo)
    placar1.contagem()
    placar2.contagem()
    pygame.display.update()
