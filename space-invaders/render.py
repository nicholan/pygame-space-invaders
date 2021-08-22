import pygame 

class RenderScreen:
    def __init__(self, game):
        """Functions for rendering and updating screen"""

        self.game = game

    def _update_screen(self):
        """Update images on screen, and flip to the new screen"""

        # Set bg color
        self.game.screen.fill(self.game.settings.bg_color)

        # Draw entities to the screen
        self.game.player.draw_player()
        self.game.enemy.draw_enemy()
        self.game.ammo.draw_bullet()
        if self.game.stats.game_over:
            self.game.game_over_button.draw_button()
            self.game.play_again_button.draw_button()
        if not self.game.stats.game_active:
            self.game.play_button.draw_button()
        self.game.stats.draw_score()
        self.game.stats.draw_lives()

        # Make the most recently drawn screen visibile.
        pygame.display.flip()