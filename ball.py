from math import cos, sin, radians
from random import random
import pygame
from events_handler import check_win

from player import Player


class Ball:
  RADIUS: int = 17
  SPEED: int = 4

  def __init__(self, game):
    super().__init__()
    self.game = game
    self.surface: pygame.Surface = game.screen

    self.radius: int = self.__class__.RADIUS
    self.pos = pygame.math.Vector2(self.surface.get_width() / 2, self.surface.get_height() / 2)

    self.color = (200, 70, 50)

    self.vector = { "x": 0, "y": 0, "angle": (random() * 360) }

  def tick(self):
    delta_y = Ball.SPEED * cos(radians(self.vector["angle"]))
    delta_x = Ball.SPEED * sin(radians(self.vector["angle"]))

    self.pos.x += delta_x
    self.pos.y += delta_y

    angle = self.vector["angle"]

    if self.pos.x <= self.game.__class__.MARGIN + Player.WIDTH:
      if self.game.player1.y < self.pos.y < self.game.player1.y + Player.HEIGHT:
        angle = 360 - angle
    elif self.pos.x >= self.surface.get_width() - self.game.__class__.MARGIN - Player.WIDTH:
      if self.game.player2.y < self.pos.y < self.game.player2.y + Player.HEIGHT:
        angle = 180 + (180 - angle)

    if self.pos.x <= self.game.__class__.MARGIN: # ball left
      angle = 360 - angle
    if self.pos.y <= self.game.__class__.MARGIN: # ball up
      angle -= 2*(angle - 90)
    if self.pos.x >= self.surface.get_width() - self.game.__class__.MARGIN: # ball right
      angle = 180 + (180 - angle)
    if self.pos.y >= self.surface.get_height() - self.game.__class__.MARGIN: # ball down
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