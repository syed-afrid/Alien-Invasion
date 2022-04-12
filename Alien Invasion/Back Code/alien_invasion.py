import pygame
from pygame.sprite import Group
import sys

import game_functions
from settings import Settings
from ship import Ship
from alien import Alien
from button import Button
from game_stats import GameStats
from scoreboard import Scoreboard
import game_functions as gf
def run_game():
    # Initialize game and create screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # Make the play button
    play_button = Button(ai_settings, screen, " 'Play' ")
    # Create an instance to store game statistics
    stats = GameStats(ai_settings)
    # Create a ship object
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets in
    bullets = Group()
    # Make a group of aliens
    aliens = Group()
    # create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # Create an instance to store game statistics and create a scoreboard
    sb = Scoreboard(ai_settings, screen, stats)
    # Start program main loop for the game
    while True:
        # Watch for keyboard and mouse events
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            # Moving of Ship
            ship.update()
            # Update bullets
            # Get rid of bullets that disappears.
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            # Update the positions of aliens
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)
        # updating the screen
        # Make the most recently drawn screen visible
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()
