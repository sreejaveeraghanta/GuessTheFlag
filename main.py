import pygame
from process_inputs import *
from game import *
import time


# Get country data from api
response = get_data()
countries = extract_countries_and_flags(response)
country, flag = get_random_country_and_flag(countries)

pygame.init()
screen = pygame.display.set_mode([450, 420])
pygame.display.set_caption("Guess The Flag")
font = pygame.font.Font(pygame.font.get_default_font(), 25)
font2 = pygame.font.Font(pygame.font.get_default_font(), 16)
user_input = ''
guess_text = "Enter guess here"

input_rect = pygame.Rect(50, 350, 350, 30)
colour = pygame.Color('white')

finished = False
while not finished: 
    screen.fill((0, 0, 0))
    image = load_flag(flag)
    screen.blit(image,(0, 0))

    pygame.draw.rect(screen, colour, input_rect, 1)

    text = font.render(user_input, True, (255, 255, 255)) 
    screen.blit(text, (input_rect.x +5, input_rect.y +2))
    answer = font2.render("Answer", True, (255, 255, 255)) 
    screen.blit(answer, (190, input_rect.y +40))

    answer_rect = answer.get_rect(topleft=(190, input_rect.y + 40))

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            finished = True
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if event.button == 1: 
                if (answer_rect.collidepoint(event.pos)): 
                    user_input = country
                    time.sleep(0.5)

        if event.type == pygame.KEYDOWN: 
            user_input += get_user_input(event)
            if event.key == pygame.K_BACKSPACE: 
                user_input = user_input[:-1]
            if event.key == pygame.K_RETURN: 
                if(validate_user_input(user_input)): 
                    user_input = user_input[:-1]
                else: 
                    user_input = user_input[:-1]
                    user_input = ''
                    guess = font.render("INVALID!!", True, (255, 255, 255)) 
                    screen.blit(guess, (150, 325))
                    pygame.display.update()
                    time.sleep(0.5)
                    continue
                if (check_user_input(user_input, country)): 
                    user_input = ''
                    guess = font.render("CORRECT!!", True, (255, 255, 255)) 
                    screen.blit(guess, (150, 325))
                    pygame.display.update()
                    time.sleep(0.5)
                    country, flag = get_random_country_and_flag(countries)
                else: 
                    guess = font.render("INCORRECT", True, (255, 255, 255)) 
                    screen.blit(guess, (150, 325))
                    pygame.display.update()
                    time.sleep(0.5)
    pygame.display.flip()

pygame.quit()
