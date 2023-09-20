import pygame as pg
from random import choice, randrange


class Symbol: 
    def __init__(self, x, y, speed):
        self.x, self.y = x, y
        self.speed = speed
        self.value = choice(green_katakana)
        self.interval = randrange(5, 30)
        
    def draw(self, color):
        frames = pg.time.get_ticks()
        if not frames % self.interval:
            self.value = choice(green_katakana if color == 'green' else light_green_katakana)
        self.y = self.y + self.speed if self.y < HEIGHT else -FONT_SIZE
        surface.blit(self.value, (self.x, self.y))

class SymbolsColumn:
    def __init__ (self, x, y):
        self.column_height = randrange(8, 64, 2)
        self.speed = randrange(2, 6)
        self.symbols = [Symbol(x, i, self.speed) for i in range(y, y - FONT_SIZE * self.column_height, -FONT_SIZE)]
    
    def draw(self):
        [symbol.draw('green') if i else symbol.draw('lightgreen') for i, symbol in enumerate(self.symbols)]

RES = WIDTH, HEIGHT = 1920, 1080
FONT_SIZE = 16
FPS = 90
alpha_value = 0


pg.init()
screen = pg.display.set_mode(RES)
surface = pg.Surface(RES)
surface.set_alpha(alpha_value)
pg.display.set_caption("Matrix animation")
clock = pg.time.Clock()

katakana = [chr(int('0x30a0', 16) + i) for i in range(96)]
numbers = [chr(int('0x0030', 16) + i) for i in range(10)]

symbols_list = numbers + katakana

font = pg.font.Font('font\MS Mincho.ttf', FONT_SIZE)
# add symbols
green_katakana = [font.render(char, True, (0, randrange(160, 256), 0)) for char in symbols_list] 
light_green_katakana = [font.render(char, True, pg.Color('lightgreen')) for char in symbols_list] 

symbols_column = [SymbolsColumn(x, randrange(-HEIGHT, 0)) for x in range(0, WIDTH, FONT_SIZE)]

while True: 
    screen.blit(surface, (0, 0))
    surface.fill(pg.Color('black'))
    
    [symbol_column.draw() for symbol_column in symbols_column]    
    
    if not pg.time.get_ticks() % 20 and alpha_value < 170:
        alpha_value += 25
        surface.set_alpha(alpha_value)
    
    [exit() for i in pg.event.get() if i.type == pg.QUIT]
    pg.display.flip()
    clock.tick(FPS)

