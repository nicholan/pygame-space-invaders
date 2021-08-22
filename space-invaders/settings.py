import pathlib
import os.path

class Settings:
    def __init__(self):
        """Store settings for Breadfall"""
        
        # FPS. Changing this value will change the game loop speed (increase/decrease movement speed of objects).
        self.fps = 60

        # Path to folders, image assets
        self.game_folder = pathlib.Path(__file__).parent.resolve()
        self.assets = os.path.join(self.game_folder, 'images')

        # Game screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (25, 25, 50)

        # Player settings
        self.player_speed = 15

        # Enemy settings
        self.enemy_speedup_scale = 1.1
        self.enemy_points = 50

        # Bullet settings
        self.bullet_width = 4
        self.bullet_height = 30
        self.bullet_speed = 30
        self.bullet_color = (255, 255, 0)

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Init settings that change during the game"""
        self.player_lives = 3
        self.enemy_speed = 3
        self.enemy_down_speed = 30

        # Enemy movement direction: 1 = right, -1 = left
        self.movement_direction = 1

    def _increase_speed(self):
        """Increase enemy speed settings"""
        self.enemy_speed *= self.enemy_speedup_scale




