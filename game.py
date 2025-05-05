import requests
import random
import pygame
import io

countries_api = "https://restcountries.com/v3.1/all"

def get_data(): 
    try: 
        response = requests.get(countries_api)
        return response.json()
    except: 
        print("cannot load the country data")
        return None 

def extract_countries_and_flags(response): 
    countries = []
    for country in response: 
        if 'name' in country and 'flags' in country and country['independent']: 
            country_entry = {'country':country['name']['common'], "flag":country['flags']['png']}
            countries.append(country_entry)
    return countries

def get_random_country_and_flag(countries): 
    random_country = random.choices(countries)[0]
    return random_country['country'], random_country['flag']

def load_flag(flag): 
    try: 
        flag = requests.get(flag)
        flag = io.BytesIO(flag.content) 
        image = pygame.image.load(flag)
        image = pygame.transform.scale(image, (450, 300))
        return image
    except: 
        print("cannot load flag; invalid url")
        return None


