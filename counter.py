import pygame #Library of game creator
import time #Library with module handle time
import math #math module

pygame.init() # initialize game

# draw a window 500x600
screen = pygame.display.set_mode((500, 600))

GREY = (150, 150, 150) #RGB constant color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

font = pygame.font.SysFont('sans', 50) #font in pygame lib
# text with font format (String, antialias, color value)
# antialias to make it look smoother
text_1 = font.render('+', True, BLACK)
text_2 = font.render('-', True, BLACK)
text_3 = font.render('+', True, BLACK)
text_4 = font.render('-', True, BLACK)
text_5 = font.render('Start', True, BLACK)
text_6 = font.render('Reset', True, BLACK)

running = True # check for game running
tot_secs = 0 # time measurement
start = False # flag to check the waiting time

while running:
  screen.fill(GREY) #draw a surface

  #draw a rectangle on a surface with the coordinate
  # (2 first cord: top left x = 100, y = 50),(length = 50)
  # (width = 50)
  pygame.draw.rect(screen, WHITE, (100,50,50,50)) #plus min
  pygame.draw.rect(screen, WHITE, (100,200,50,50)) #minus min
  pygame.draw.rect(screen, WHITE, (200,50,50,50)) #plus sec
  pygame.draw.rect(screen, WHITE, (200,200,50,50)) #minus min
  pygame.draw.rect(screen, WHITE, (300,50,150,50)) #start btn
  pygame.draw.rect(screen, WHITE, (300,150,150,50)) #reset btn

  #blit use to add text start at coordinate
  screen.blit(text_1, (100, 50))
  screen.blit(text_2, (100, 200))
  screen.blit(text_3, (200, 50))
  screen.blit(text_4, (200, 200))
  screen.blit(text_5, (300, 50))
  screen.blit(text_6, (300, 150))

  #present box
  pygame.draw.rect(screen, BLACK, (50,520,400,50))
  pygame.draw.rect(screen, WHITE, (60,530,380,30))

  #circle(surface, color, (center x,y), raidus)
  pygame.draw.circle(screen, BLACK, (250, 400), 100)
  pygame.draw.circle(screen, WHITE, (250, 400), 95)
  pygame.draw.circle(screen, BLACK, (250, 400), 5)

  #pygame.mouse.get_pos is getting coordinate of the mouse
  mouse_x, mouse_y = pygame.mouse.get_pos()

  #event happend on the computer
  for event in pygame.event.get():
    if event.type == pygame.QUIT: #click quit event
      running = False
    if event.type == pygame.MOUSEBUTTONDOWN: #click mouse
      if event.button == 1: # 1 - right click, 2 - left click
        if (100 < mouse_x < 150) and (50 < mouse_y < 100):# click at coord
          tot_secs += 60
          print("press + min")
        if (100 < mouse_x < 150) and (200 < mouse_y < 250):
          tot_secs -= 60
          print("press - min")
        if (200 < mouse_x < 250) and (50 < mouse_y < 100):# click at coord
          tot_secs += 1
          print("press + sec")
        if (200 < mouse_x < 250) and (200 < mouse_y < 250):
          tot_secs -= 1
          print("press - sec")
        if (300 < mouse_x < 450) and (50 < mouse_y < 150):# click at coord
          start = True
          print("press start")
        if (300 < mouse_x < 400) and (150 < mouse_y < 250):
          tot_secs = 0
          start = False
          print("press reset")

  #run the clock
  if start:
    tot_secs -= 1
    time.sleep(1) #wait for 1 second

  #Time display string
  mins = int(tot_secs / 60)
  secs = tot_secs - mins * 60
  time_now = str(mins) + ' : ' + str(secs)

  text_time = font.render(time_now, True, BLACK)
  screen.blit(text_time, (120, 120))

  # Draw clock timing for sec
  x_sec = 250 + 90 * math.sin(6 * secs * math.pi / 180)
  y_sec = 400 - 90 * math.cos(6 * secs * math.pi / 180)
  pygame.draw.line(screen, BLACK, (250, 400), (x_sec, y_sec))

  # Draw clock timing for min
  x_min = 250 + 40 * math.sin(6 * mins * math.pi / 180)
  y_min = 400 - 40 * math.cos(6 * mins * math.pi / 180)
  pygame.draw.line(screen, RED, (250, 400), (x_min, y_min))

  pygame.display.flip() # for display

pygame.quit() #stop the game when done


"""
Note: 
- pyinstaller use to convert a .py file to exec (pyinstaller filename.py)
- exec could be run without python on machine
- no console (pyinstaller filename.py --nonconsole)
- we could import picture to app icon by using pyinstaller (pyinstaller --icon=filename.ico)
- only pay attention to file in dist
"""
