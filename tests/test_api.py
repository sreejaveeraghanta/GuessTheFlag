import pytest
import sys
import os
import requests
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from game import * 

def test_api_call(): 
    response = requests.get(countries_api)
    assert (response.status_code == 200)

def test_flag_country_extraction(): 
    response = get_data()
    countries = extract_countries_and_flags(response)
    assert (len(countries) == 195)
    