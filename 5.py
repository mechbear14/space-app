import pygame, random, sys, time
import pyscroll


class Balloon:
   def __init__(self):
       self.balloon = pygame.image.load('balloon.png')
       self.rect = self.balloon.get_rect()
       self.rect.left = self.rect.width + (random.random() * (screen.get_width() - self.rect.width * 2))
       self.rect.top = random.random() * (screen.get_height() - self.rect.height)
       if random.random() < 0.5:
           self.drift = -2
       else:
           self.drift = 2

   def update(self):
       self.rect.top -= 2
       self.rect.left += self.drift
       if self.rect.top < 2:
           self.rect.top = screen.get_height() - self.rect.height / 2
       if self.rect.left < 2 or self.rect.left > screen.get_width() - self.rect.width:
           self.drift *= -1
       screen.blit(self.balloon, self.rect)

   def eventcheck(self, events, score):
       for event in events:
           if event.type == pygame.QUIT:
               pygame.quit()
               raise SystemExit
           if event.type == pygame.MOUSEBUTTONDOWN:
               # Set the x, y postions of the mouse click
               x, y = event.pos
               if self.rect.collidepoint(x, y):
                   # pop.play()
                   score += 1
                   self.rect.left = self.rect.width + (random.random() * (screen.get_width() - self.rect.width * 2))
                   self.rect.top = screen.get_height() - self.rect.height / 2
                   events = []
       return events, score


pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Internet over seas")
# background = pygame.image.load('gingerbread.png')
background = pygame.image.load('map.gif')
bg_rect = background.get_rect()
bg_rect.left = 0
bg_rect.top = 0

# pop = pygame.mixer.Sound('Pop.wav')

font = pygame.font.Font(None, 60)
score = 0

stoptime = time.time() + 10
playing = True

clock = pygame.time.Clock()


screen.fill([255, 255, 255])

while playing:
   screen.blit(background, bg_rect)

   events = pygame.event.get()
   for e in events:
       if e.type == pygame.QUIT:
           sys.exit()
           raise SystemExit




   pygame.display.update()

   clock.tick(60)

   if stoptime - time.time() < 0:
       playing = False



