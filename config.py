import sys, yaml
from pygame import Color
from typing import Tuple

class Config:
  def __init__(self, path: str):
    try:
      self.file = open(path)
      self.config = yaml.load(self.file.read(), yaml.Loader)
      self.file.close()
    except:
      print("Can't load config file, exiting!")
      print("You can download default config from https://raw.githubusercontent.com/goteusz-maszyk/pypong/master/config.yml")
      sys.exit(1)

  def get_color(self, path: str, raise_error: bool = False) -> Tuple:
    try:
      parsed: Tuple = tuple(map(int, self.config[path].split(" ")))
      return Color(parsed)
    except:
      if raise_error:
        print("Config value", path, "is invalid! Exiting.")
        sys.exit(1)
      return None
  
  def get_string(self, path: str, raise_error: bool = False) -> str:
    try:
      return str(self.config[path])
    except:
      if raise_error:
        print("Config value", path, "is invalid! Exiting.")
        sys.exit(1)
      return None

  def get_float(self, path: str, raise_error: bool = False) -> float:
    try:
      return float(self.config[path])
    except:
      if raise_error:
        print("Config value", path, "is invalid! Exiting.")
        sys.exit(1)
      return None