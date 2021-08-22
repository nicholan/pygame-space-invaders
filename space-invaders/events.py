import pygame
import sys

class Events:
    def __init__(self, game):
        """Class to handle mouse and keyboard events."""

        self.game = game

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.game.player.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.game.player.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

        elif event.key == pygame.K_w and self.game.stats.game_active and not self.game.stats.game_paused:
            self.game.ammo._create_bullet()

        elif event.key == pygame.K_y and self.game.stats.game_over == True:
            self.game.stats.reset_stats()
            self.game.enemy.enemies.empty()
            self.game.settings.initialize_dynamic_settings()
            self.game.ammo.bullets.empty()
            self.game.stats.prep_score()
            self.game.stats.prep_lives()
            self.game.stats.game_over = False


        # Game pausing
        elif event.key == pygame.K_p and not self.game.stats.game_paused:
            self.game.stats.game_paused = True
        elif event.key == pygame.K_p and self.game.stats.game_paused:
            self.game.stats.game_paused = False
                
    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.game.player.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.game.player.moving_left = False

    def _check_events(self):
            """Respond to keyboard and mouse events."""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)

                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)
    
    def _check_play_button(self, mouse_pos):
        """Check whether player clicks on "Play" or "Play Again" buttons."""
        if self.game.play_button.rect.collidepoint(mouse_pos):
            self.game.stats.game_active = True

        if self.game.play_again_button.rect.collidepoint(mouse_pos):
            self.game.settings.initialize_dynamic_settings()
            self.game.stats.reset_stats()
            self.game.enemy.enemies.empty()
            self.game.ammo.bullets.empty()
            self.game.stats.prep_score()
            self.game.stats.prep_lives()
            self.game.stats.game_over = False