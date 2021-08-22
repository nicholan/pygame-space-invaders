import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, game):
        """Class for single bullet."""

        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.bullet_color
        self.speed = self.settings.bullet_speed

        # Create bullet rect at (0, 0) and then set corrent position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = game.player.rect.midtop

        # Store bullet's position as float
        self.y = float(self.rect.y)


class BulletGroup:
    def __init__(self, game):
        """A class to group bullets fired from the ship."""

        self.bullets = pygame.sprite.Group()
        self.screen = game.screen
        self.settings = game.settings
        self.player = game.player

    def _create_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update(self):
        """Move the bullet up the screen."""
        for bullet in self.bullets:
            bullet.y -= bullet.speed
            bullet.rect.y = bullet.y

            # Delete out of bounds bullets.
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def draw_bullet(self):
        """Draw bullet to the screen"""
        for bullet in self.bullets.sprites():
            pygame.draw.rect(bullet.screen, bullet.color, bullet.rect)
