import pygame

from settings import Settings
from player import Player
from events import Events
from render import RenderScreen
from enemies import EnemyGroup
from bullet import BulletGroup
from game_stats import GameStats
from button import Button


class Gahbage:
    def __init__(self):
        """Overall class to manage game assets and behaviour. Initialize the game and create game resources-"""

        pygame.init()

        # Framerate capping to 60 with self.clockobject.tick(60)
        self.clockobject = pygame.time.Clock()

        # Initialize game settings, display mode and caption
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Gahbage")

        # Initialize game statistics and states, player, enemy sprites, player ammo. 
        self.stats = GameStats(self)
        self.player = Player(self)
        self.ammo = BulletGroup(self)
        self.enemy = EnemyGroup(self)

        # Init button, texts boxes
        self.play_button = Button(self, "PLAY", (50, 200, 50), 200, 50)
        self.game_over_button = Button(self, "GAME OVER", (200, 50, 50), 400, 50, -30)
        self.play_again_button = Button(self, "PLAY AGAIN", (50, 200, 50), 400, 50, 30)

        # Initialize mouse and keyboard events handler
        self.events = Events(self)
        
        # Initialize screen renderer
        self.render = RenderScreen(self)

        
    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self.clockobject.tick(self.settings.fps)
            self.events._check_events()

            if not self.stats.game_over and not self.stats.game_paused and self.stats.game_active:
                self.enemy._create_fleet()
                self.player._update()
                self.enemy._update()
                self.enemy._check_fleet_edges()
                self.enemy._check_player_collision()
                self.enemy._check_bullet_collision()
                self.enemy._check_bottom_collision()
                self.ammo._update()
            self.render._update_screen()
            
if __name__ == '__main__':
    game = Gahbage()
    game.run_game()

