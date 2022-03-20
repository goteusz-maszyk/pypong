import pygame
pygame.font.init()

class PointDisplay:

  def __init__(self, player):
    self.player = player
    self.game = player.game
    self.screen: pygame.Surface = self.game.screen
    self.font = pygame.font.SysFont(
      self.game.config.get_string("font-family", True),
      self.game.config.get_int("font-size", True))
    
    if self.player.is_p2:
      self.x = self.screen.get_width() / 2  + self.screen.get_width() / 10
    else:
      self.x = self.screen.get_width() / 2  - self.screen.get_width() / 10
    self.y = 10
  
  def tick(self):
    player_id = "P"
    if self.player.is_p2:
      player_id += "2"
    else:
      player_id += "1"

    final_text = player_id + ": " + str(self.player.points)

    textsurface = self.font.render(final_text, False, (10, 10, 10))
    self.screen.blit(textsurface, (self.x - self.font.size(final_text)[0], self.y))