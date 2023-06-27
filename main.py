import pygame
import sys
import math
import tkinter as tk
from tkinter import simpledialog

# Inicialização do Pygame
pygame.init()

sys = SystemExit
# Configuração da janela
largura = 800
altura = 600
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("SPACE MARKER")
tamanho_tela = (largura, altura)

# Carregamento do som de fundo
pygame.mixer.music.load("Space_Machine_Power.mp3")
pygame.mixer.music.play(-1)  # Reproduzir em looping

# Carregamento do ícone
icone = pygame.image.load("space.png")
pygame.display.set_icon(icone)

# Definição das cores
branco = (255, 255, 255)
vermelho = (255, 0, 0)

# Carregamento dos recursos (sons, imagens, etc.)
fundo = pygame.image.load("imagem.fundo.jpg")
fundo = pygame.transform.scale(fundo, (largura, altura))

# Criação da janela
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("SPACE MARKER")

# Variáveis para armazenar os pontos clicados
pontos = []

# Variáveis para armazenar as marcações das estrelas
marcacoes = {}

# Variáveis para armazenar as linhas e as somas das distâncias
linhas = []
distancias = []
circulos = []
estrelas_encontradas = 0