import pygame

class Player(object):
  WIDTH = 30
  HEIGHT = 200
  MOVE_SPEED = 3

  def __init__(self, game, start_x):
    super().__init__()
    self.game = game
    self.surface: pygame.Surface = game.screen
    self.pos = pygame.math.Vector2

    self.x: int = start_x
    self.y: int = 10
    self.width: int = Player.WIDTH * game.config.get_float("window-size-multipier")
    self.height: int = Player.HEIGHT * game.config.get_float("window-size-multipier")

    self.color = self.game.config.get_color('player-color', True)
    self.points = 0

  def tick(self, is_p2):
    keys = pygame.key.get_pressed()
    v = Player.MOVE_SPEED

    if keys[pygame.K_w] and not is_p2:
      self.move(-v, "y")
    if keys[pygame.K_s] and not is_p2:
      self.move(v, "y")
    if keys[pygame.K_UP] and is_p2:
      self.move(-v, "y")
    if keys[pygame.K_DOWN] and is_p2:
      self.move(v, "y")
  
  def move(self, offset, axis):
    if axis == "y":
      new_y = self.y + offset
      if new_y < self.surface.get_height() - self.height - 10 and new_y > 10:
        self.y += offset

  def draw(self):
    pygame.draw.rect(self.surface, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
  
  def teleport(self, x: int, y: int):
    self.x = x - self.width / 2
    self.y = y - self.height / 2