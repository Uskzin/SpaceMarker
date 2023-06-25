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
