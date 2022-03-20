import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
from ball import Ball
from events_handler import handle_events
from player import Player
from config import Config

class Game(object):
  MARGIN = 10

  def __init__(self):
    self.load_config()
    self.max_tps = 70.0

    pygame.init()
    self.screen = pygame.display.set_mode((1500, 820))
    self.tps_clock = pygame.time.Clock()
    self.tps_delta = 0.0

    self.player1 = Player(self, 10)
    self.player2 = Player(self, self.screen.get_width() - 10 - Player.WIDTH)
    self.ball = Ball(self)


    pygame.display.set_caption("Pong!")

    if self.config.get_color("background"):
      self.background = self.config.get_color("background")
    else:
      bkg_file = self.config.get_string("background")
      self.background = pygame.image.load(bkg_file)

    while True:
      handle_events(self)

      self.tps_delta += self.tps_clock.tick() / 1000.0
      while self.tps_delta > 1/2.0/self.max_tps:
        self.tick()
        self.tps_delta -= 1/2.0/self.max_tps

      pygame.display.flip()

  def tick(self):
    self.player1.tick(False)
    self.player2.tick(True)
    self.ball.tick()

    if self.background.__class__ == pygame.Color:
      self.screen.fill(self.config.get_color("background", True))
    else:
      self.screen.blit(self.background, (0, 0))

    self.draw()

  def draw(self):
    self.player1.draw()
    self.player2.draw()
    self.ball.draw()

  def load_config(self):
    self.config = Config("./config.yml")

if __name__ == "__main__":
  Game()