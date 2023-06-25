import pygame
import pygame
import tkinter as tk
from tkinter import simpledialog
import winsound

pygame.init()
tamanho = (800, 600)
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Space Marker")
icon=pygame.image.load("space.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
fundo = pygame.image.load("imagem.fundo.jpg")
pygame.mixer.music.load("Space_Machine_Power.mp3")
pygame.mixer.music.play(0,0,5)
branco=(255,255,255)
circulos=[]
estrelas = []
sys = SystemExit
