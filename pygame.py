import pygame
import random

def main():
  pygame.init()

  # Screen setup
  WIDTH = 800
  HEIGHT = 600
  screen = pygame.display.set_mode((WIDTH, HEIGHT))
  pygame.display.set_caption("Flood Escape: Save the Village")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)
GREEN = (0, 255, 0)
RED = (255, 0 , 0)
BLACK = (0, 0, 0)

# Player
player = pygame.Rect(50, 400, 30, 30)
player_speed = 5

# Villagers
villagers = [pygame.Rect(random.randint(100, 750), random.randint(50, 450), 20, 20) for i in range(5)]

# Safe zone
safe_zone =pygame.Rect(700, 50, 80, 80)

#Flood level
flood_level = HEIGHT
flood_speed = 0.2

score = 0
font = pygame.font.SysFont(None, 30)

clock = pygame.time.clock()
running =  True

def draw_text(text, x, y, color="black"):
  img = font.render(text,  True, color)
  screen.blit(img, (x, y))
while running:
  clock.tick(60)
  screen.fill(WHITE)
  
  # Events
  for event in pygame.event.get():
    if event.type == pygame.Quit:
      running = False

  # controls
  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT]:
    player.x -= player_speed
  elif keys[pygame.K_RIGHT]:
    play.x += player_speed
  elif keys[pygame.K_UP]:
    play.y -= player_speed
  else:
     play.y += player_speed

  # Flood rising
  flood_level -= flood_speed
  flood_rect = pygame(0, flood_level, WIDTH, HEIGHT - flood_level)

  # Collision with flood (game over)
   if player.colliderect(flood_rect):
     draw_text("Game Over - Flood caught you!", 200,200, RED)
     pygame.display.update()
     pygame.time.delay(2000)
     running = False

  # Collect Villagers
   for v in villagers [:]:
     if player.colliderect(v):
       villagers.remove(v)
       score += 10

  # Win condition
   if player.colliderect(safe_zone) and len(villagers) == 0:
     draw.text("you Won! All Villagers Saved!", 200, 200, GREEN)
     pygame.display.update()
     pygame.time.delay(3000)
     running = False

  # Draw safe zone
  pygame.draw.rect(screen, GREEN, safe_zone)

  # Draw flood
  pygame.draw.rect(screen, BLUE, flood_rect)

  # Draw player
  pygame.draw.rect(screen, BLACK, player)

  # Draw villagers
  for v in villages:
    pygame.draw.rect(screen, RED, v)

   #UI
  draw_text(f"Score: {score}", 10, 10)
  draw.text(f"Villagers left: {len(villagers)}", 10, 40)
  pygame.display.update()
pygame.quit()

if __name__ == "__main__":
  main()

