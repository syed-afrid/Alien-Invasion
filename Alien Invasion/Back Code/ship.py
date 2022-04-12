import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    """This is the blueprint of our with all behaviours"""
    def __init__(self, ai_settings, screen):
        """Initialize ship and set starting position"""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # Load ship image and get its rect
        self.image = pygame.image.load('Images/ship.bmp')
        self.rect = self.image.get_rect()  # The ship element as rectangle
        self.screen_rect = screen.get_rect()  # Make the screen as rect(element) where we have drawn the ship
        # Start each ship at bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)
        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement_right"""
        # Update the ship's center not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        # Update rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at it's current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.centerx
