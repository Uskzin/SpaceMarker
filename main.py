import pygame
import pygame
import tkinter as tk
from tkinter import simpledialog
import winsound

pygame.init()
sys = SystemExit
largura = 800
altura = 600
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("SPACE MARKER")
fundo = pygame.image.load("imagem.fundo.jpg")
fundo = pygame.transform.scale(fundo, (largura, altura))
pygame.mixer.music.load("Space_Machine_Power.mp3")
pygame.mixer.music.play(-1) 
icone = pygame.image.load("space.png")
pygame.display.set_icon(icone)
branco = (255, 255, 255)
vermelho = (255, 0, 0) 
marcacoes = {}
linhas = []
distancias = []
pontos = []
"Funçoes"
def obter_nome_estrela():
    root = tk.Tk()
    root.withdraw()
    nome = simpledialog.askstring("Nome da Estrela", "Digite o nome da estrela:")
    return nome

try:
    while True:
         for evento in pygame.event.get():
             if evento.type == pygame.MOUSEBUTTONDOWN:
                 if evento.button == 1:
                    posicao_mouse = pygame.mouse.get_pos()
                    pontos.append(posicao_mouse)
                    nome_estrela = obter_nome_estrela()
                    marcacoes[posicao_mouse] = nome_estrela
                    janela.blit(fundo, (0, 0))







    
except Exception as erro:
    # Lidar com erros
     print(f"Ocorreu um erro: {erro}")
     pygame.quit()
     sys()
