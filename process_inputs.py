import pygame
from unidecode import unidecode

def get_user_input(event): 
    user_input = ''
    if event.key == pygame.K_BACKSPACE: 
        user_input = user_input[:-1]
    else: 
        user_input+=event.unicode

    return user_input

def check_user_input(user_input, country):
    user_input = unidecode(user_input).lower().strip().title()
    country = unidecode(country).lower().title() 
    if user_input == country: 
        return True
    else: 
        return False

def validate_user_input(user_input): 
    invalid_characters = "!@#$%^&*()_+|}{:?><,./;'[]1234567890=`~"
    if not user_input: 
        return False
    for character in user_input: 
        if character in invalid_characters: 
            return False
    return True



