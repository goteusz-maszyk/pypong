from math import cos, sin, radians
from random import random
import pygame
from events_handler import check_win
from player import Player

pygame.mixer.init()

class Ball:
  RADIUS: int = 17
  SPEED: int = 4
  click_sound = pygame.mixer.Sound("./assets/click.wav")
  wall_sound = pygame.mixer.Sound("./assets/ball_wall.wav")

  def __init__(self, game):
    super().__init__()
    self.game = game
    self.surface: pygame.Surface = game.screen

    self.radius: int = self.__class__.RADIUS * game.config.get_float("window-size-multipier")
    self.pos = pygame.math.Vector2(self.surface.get_width() / 2, self.surface.get_height() / 2)

    self.color = self.game.config.get_color('ball-color', True)

    self.vector = { "x": 0, "y": 0, "angle": (random() * 360) }

  def tick(self):
    delta_y = Ball.SPEED * cos(radians(self.vector["angle"]))
    delta_x = Ball.SPEED * sin(radians(self.vector["angle"]))

    self.pos.x += delta_x
    self.pos.y += delta_y

    angle = self.vector["angle"]

    if self.pos.x <= self.game.__class__.MARGIN + Player.WIDTH * self.game.config.get_float("window-size-multipier"):
      if self.game.player1.y < self.pos.y < self.game.player1.y + Player.HEIGHT * self.game.config.get_float("window-size-multipier"):
        angle = 360 - angle
        angle += (random() * 20) - 10
        Ball.wall_sound.play()
    elif self.pos.x >= self.surface.get_width() - self.game.__class__.MARGIN - Player.WIDTH * self.game.config.get_float("window-size-multipier"):
      if self.game.player2.y < self.pos.y < self.game.player2.y + Player.HEIGHT * self.game.config.get_float("window-size-multipier"):
        angle = 180 + (180 - angle)
        angle += (random() * 20) - 10
        Ball.wall_sound.play()

    if self.pos.y <= self.game.__class__.MARGIN: # ball up
      angle -= 2*(angle - 90)
      Ball.wall_sound.play()
    if self.pos.y >= self.surface.get_height() - self.game.__class__.MARGIN: # ball down
      Ball.wall_sound.play()
      if angle < 360: # ball down-left
        angle = 270 - (angle - 270)
      else: # ball down-right
        angle = 270 + angle


    while angle > 360:
      angle -= 360
    self.vector["angle"] = angle

    check_win(self.game)

  def draw(self):
    pygame.draw.circle(self.surface, self.color, self.pos, self.radius)
  
  def teleport(self, x: int, y: int):
    self.pos.x = x
    self.pos.y = y

  def reset(self):
    self.teleport(self.surface.get_width() / 2, self.surface.get_height() / 2)
    self.vector["angle"] = random() * 360