import pygame
import os.path
from pygame.sprite import Sprite
from random import choice
from time import sleep

class Enemy(Sprite):
    def __init__(self, game):
        """Single enemy character sprite."""

        super().__init__()
        self.game = game
        self.screen_rect = self.game.screen.get_rect()

        # Load sprites and their rects
        self.image = pygame.image.load(self._load_random_image())
        self.rect = self.image.get_rect()

        # Enemy location on screen 
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store x as float
        self.x = float(self.rect.x)

    def _load_random_image(self):
        """Load random image to represent enemy."""
        sprite_images = ['enemy4.png', 'enemy5.png', 'enemy6.png', 'enemy7.png', 'enemy8.png']
        sprite_image = os.path.join(self.game.settings.assets, choice(sprite_images))
        return sprite_image

    def _check_edges(self):
        """Check whether enemy has hit left or right edge of the screen."""
        if self.rect.right >= self.screen_rect.right or self.rect.left <= 0:
            return True
        
    def _update(self):
        """Move enemy."""
        self.rect.x += (self.game.settings.enemy_speed * self.game.settings.movement_direction)

        
class EnemyGroup:
    def __init__(self, game):
        """Class to manage group of enemy sprites."""

        self.game = game
        self.enemies = pygame.sprite.Group()
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        
    
    def _create_fleet(self):
        """Create a rows of enemies depending on screen and enemy sprite size."""
        if len(self.enemies) == 0:
            self.game.settings._increase_speed()
            new_enemy = Enemy(self)
            enemy_width, enemy_height = new_enemy.rect.size
            available_space_x = self.game.settings.screen_width - enemy_width
            number_enemies_x = available_space_x // (2 * enemy_width)

            player_height = self.game.player.rect.height
            available_space_y = (self.game.settings.screen_height - (3 * enemy_height) - player_height)
            number_of_rows = available_space_y // (2 * enemy_height)

            for row_number in range(number_of_rows):    
                for enemy_num in range(number_enemies_x):
                    enemy = Enemy(self)
                    enemy.x = enemy_width + 2 * enemy_width * enemy_num
                    enemy.rect.y = enemy.rect.y + 2 * enemy.rect.height * row_number
                    enemy.rect.x = enemy.x
                    self.enemies.add(enemy)

    def _update(self):
        """Update enemies."""
        for enemy in self.enemies:
            enemy._update()

    def _check_fleet_edges(self):
        """Detect if an enemy is colliding with an edge of the screen, change movement direction and move enemies down y-axis."""
        for enemy in self.enemies:
            if enemy._check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Change enemies movement direction."""
        for enemy in self.enemies.sprites():
            enemy.rect.y += self.game.settings.enemy_down_speed
        self.game.settings.movement_direction *= -1    

    def _check_player_collision(self):
        """Check collision between enemies and player."""
        if pygame.sprite.spritecollideany(self.game.player, self.enemies):
            self._player_hit()
    
    def _check_bottom_collision(self):
        """Check collision between enemy and bottom of the screen."""
        for enemy in self.enemies:
            if enemy.rect.bottom >= self.screen_rect.bottom:
                self._player_hit()
                break
    
    def _check_bullet_collision(self):
        """Check collision between bullets and enemies, remove both if they collide."""
        collisions = pygame.sprite.groupcollide(self.game.ammo.bullets, self.enemies, True, True)
        if collisions:
            for enemies in collisions.values():
                self.game.stats.score += self.game.settings.enemy_points * len(enemies)
            self.game.stats.prep_score()

    def _player_hit(self):
        """Called when player collides with enemy or enemy reaches bottom of the screen."""
        self.game.stats.player_lives -= 1
        self.game.stats.prep_lives()
        if self.game.stats.player_lives == 0:
            self.game.stats.game_over = True
        else:
            self.enemies.empty()
            self.game.ammo.bullets.empty()
            self._create_fleet()

        # Pause
        sleep(0.5)
                    
    def draw_enemy(self):
        """Draw enemy at its current location."""
        for enemy in self.enemies.sprites():
            enemy.game.screen.blit(enemy.image, enemy.rect)
    