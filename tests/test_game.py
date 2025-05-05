import pytest
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from process_inputs import get_user_input
import pygame


@pytest.fixture
def setup_game_environment(): 
    pygame.init()
    yield 
    pygame.quit()

@pytest.mark.parametrize("input, expected", [
    (pygame.K_a, 'a'), 
    (pygame.K_b, 'b'),
    (pygame.K_EXCLAIM, "!"), 
])
def test_user_input(input, expected, setup_game_environment):
    event = pygame.event.Event(pygame.KEYDOWN, {'key': input, 'unicode': expected})
    user_input = get_user_input(event)
    assert(user_input == expected)

# TODO create a mock for the API to return a specific vesion of the thing, and then test
# @pytest.mark.parametrize("input", [])