import pygame

PRETO = 0, 0, 0
BRANCO = 255, 255, 255
VERDE = 0, 255, 0

fim = False
tamanho = 800, 600
tela = pygame.display.set_mode(tamanho)
tela_retangulo = tela.get_rect()


class Raquete:
    def __init__(self, tamanho):
        self.imagem = pygame.Surface(tamanho)
        self.imagem.fill(VERDE)
        self.imagem_retangulo = self.imagem.get_rect()

    def realiza(self):
        tela.blit(self.imagem, self.imagem_retangulo)

raquete = Raquete((10, 50))

while not fim:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            fim = True
    tecla = pygame.key.get_pressed()
    print(tecla)
    tela.fill(PRETO)
    raquete.realiza()
    pygame.display.update()
