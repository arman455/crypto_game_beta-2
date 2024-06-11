import pygame
import rectangles
import events
import binance_api

pygame.init()

window = pygame.display.set_mode((850, 540))
pygame.display.set_caption("Crypto Simulator")

time_game = pygame.time.Clock()

currency = binance_api.make_request()
timer_15 = 900

run = True
while run:
    timer_15 -= 1
    if timer_15 <= 0:
        print(1)
        currency = binance_api.make_request()
        timer_15 = 900

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        events.events(event)

    window.fill((50, 50, 50))

    rectangles.draw_rectangle(window, (105,105,105), rectangles.grafic_tab, False)
    rectangles.draw_rectangle(window, (0,255,127), rectangles.buy_button, True, (10, 10), "BUY", (0,0,0))
    rectangles.draw_rectangle(window, (152,251,152), rectangles.currency_tab, True, (18, 10), f"CURRENCY   {currency}", (0,0,0))
    rectangles.draw_rectangle(window, (60,179,113), rectangles.summa_tab, False)
    rectangles.draw_rectangle(window, (144,238,144), rectangles.coefficient_tab, False)
    rectangles.draw_rectangle(window, (46,139,87), rectangles.history_tab, False)
    rectangles.draw_rectangle(window, (0,250,154), rectangles.trade_tab, False)
    
    pygame.display.flip()
    time_game.tick(60)
