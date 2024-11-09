# main.py

import pygame
import sys
import time

pygame.init()

image_path = "media/2D-Suurstoffi.png"
background_image = pygame.image.load(image_path)
screen_width, screen_height = background_image.get_size()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("R2RPA Prototype")

# Define colors
RED = (25, 200, 25)

# Define hardcoded points to draw the path (example points, you can change them)
points = [
    (120, 460),
    (125, 480),
    (180, 455),
    (245, 435),
    (245, 395)
]

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw the background image
    screen.blit(background_image, (0, 0))

    # Draw the path along all the points
    if len(points) > 1:
        pygame.draw.lines(screen, RED, False, points, 6)  # Set width to 3 for visibility

    # Update the display
    pygame.display.flip()