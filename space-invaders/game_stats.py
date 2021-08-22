import pygame

class GameStats:
    def __init__(self, game):
        """Class to track game statistics (score, lives) and state."""
        self.game = game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.reset_stats()

        # Game states, start the game in inactive state.
        self.game_active = False
        self.game_over = False
        self.game_paused = False

        # Score and lives text settings, preparation
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()
        self.prep_lives()
        
    def reset_stats(self):
        """Init stats that can change during the game."""
        self.player_lives = self.game.settings.player_lives
        self.score = 0

    def prep_score(self):
        """Turn the score into rendered image"""
        score_str = str(self.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.game.settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_lives(self):
        """Turn player lives into rendered image"""
        lives_str = str(self.player_lives)
        self.lives_image = self.font.render(lives_str, True, self.text_color, self.game.settings.bg_color)
        self.lives_rect = self.lives_image.get_rect()
        self.lives_rect.right = self.screen_rect.left + 30
        self.lives_rect.top = 20

    def draw_lives(self):
        """Draw lives on the screen at top left corner"""
        self.screen.blit(self.lives_image, self.lives_rect)

    def draw_score(self):
        """Draw score on the screen at top right corner"""
        self.screen.blit(self.score_image, self.score_rect)