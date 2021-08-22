import pygame
import os.path


class Player:
    def __init__(self, game):
        """Initialize player sprite and its starting position, and movement flags"""
        
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        # Load settings
        self.settings = game.settings

        # Load sprite and its rect
        self.image = pygame.image.load(os.path.join(self.settings.assets, 'player2.png'))
        self.rect = self.image.get_rect()

        # Start player at bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for player horizontal position
        self.x = float(self.rect.x)

        # Continuous movement flags
        self.moving_right = False
        self.moving_left = False

    def draw_player(self):
        """Draw player at its current location"""
        self.screen.blit(self.image, self.rect)

    def _update(self):
        """Update player position based on movement flags"""
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.player_speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.player_speed

        # Update rect objects from self.x
        self.rect.x = self.x
    

