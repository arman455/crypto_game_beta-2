import pygame
import texts

grafic_tab = pygame.Rect(10,10,600,400)
buy_button = pygame.Rect(10,420,150,50)
currency_tab = pygame.Rect(170,420,440,50)
summa_tab = pygame.Rect(10,480,295,50)
coefficient_tab = pygame.Rect(315,480,295,50)
history_tab = pygame.Rect(620,10,220,210)
trade_tab = pygame.Rect(620,230,220,300)

button_sell = pygame.Rect(100,180,100,50)

def draw_rectangle(window, color, rectangle, with_text=None, text_space=None, text=None, text_color=None):
    pygame.draw.rect(window, color, rectangle)
    if with_text == True:
        texts.addText(window, (rectangle.x + text_space[0], rectangle.y + text_space[1]), text, text_color, texts.font40)