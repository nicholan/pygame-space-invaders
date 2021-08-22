import pygame.font


class Button:
    def __init__(self, game, msg, button_color, width, height, y_offset=0):    
        """Init button attributes, arguments taken: 
        message, button color (0, 0, 0), button width and height, 
        button offset on y axis, defaults to center of the screen."""

        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of button
        self.button_color = button_color
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Buttons rect object, centering, y-offsetting
        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = self.screen_rect.center 
        self.rect.y += y_offset

        # Prep message
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

