import sys, pygame
from time import time
from math import floor

def handle_keys(event, game):
  match event.key:
    case pygame.K_ESCAPE:
      safe_exit(game)
    case pygame.K_j:
      game.ball.reset()

def handle_events(game):
  for event in pygame.event.get():
    match event.type:
      case pygame.QUIT:
        safe_exit(game)
      case pygame.KEYDOWN:
        handle_keys(event, game)

def check_win(game):
  if game.ball.pos.x <= game.__class__.MARGIN:
    game.player2.points += 1
    game.ball.reset()
    game.ball.click_sound.play()
  if game.ball.pos.x >= game.screen.get_width() - game.__class__.MARGIN:
    game.player1.points += 1
    game.ball.reset()
    game.ball.click_sound.play()

def safe_exit(game):
  print("Player 1 got", game.player1.points, "points")
  print("Player 2 got", game.player2.points, "points")

  try:
    file = open('./games/' + str(floor(time())) + ".log", "w")
    file.write("P1: " + str(game.player1.points) + "\n")
    file.write("P2: " + str(game.player2.points))
  except:
    print("Failed to save game results to file. Please create 'games' directory.")
    game.running = False
    sys.exit(0)

  sys.exit(0)