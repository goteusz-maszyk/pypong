import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
from ball import Ball
from events_handler import handle_events
from player import Player

class Game(object):
  MARGIN = 10

  def __init__(self):
    self.max_tps = 70.0

    pygame.init()
    self.screen = pygame.display.set_mode((1500, 820))
    self.tps_clock = pygame.time.Clock()
    self.tps_delta = 0.0

    self.player1 = Player(self, 10)
    self.player2 = Player(self, self.screen.get_width() - 10 - Player.WIDTH)
    self.ball = Ball(self)

    pygame.display.set_caption("Pong!")

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
    self.screen.fill((153, 217, 232))
    self.draw()

  def draw(self):
    self.player1.draw()
    self.player2.draw()
    self.ball.draw()

if __name__ == "__main__":
  Game()