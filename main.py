# main.py
import pygame
import sys
import time
import numpy as np
from scipy.interpolate import splev, splprep

pygame.init()

image_path = "media/2D-Suurstoffi.png"
background_image = pygame.image.load(image_path)
screen_width, screen_height = background_image.get_size()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("R2RPA Prototype")

# Define colors
BLACK = (0, 0, 0)
RED = (25, 200, 25)

# Define hardcoded points to draw the path (example points, you can change them)
control_points = [
    (120, 460),
    (125, 480),
    (180, 455),
    (245, 435),
    (245, 395)
]

# Function to generate a smooth curve between control points
def generate_smooth_path(control_points, num_points=100):
    points = np.array(control_points).T  # Transpose for interpolation
    tck, u = splprep(points, s=0)  # s=0 means interpolation exactly through points
    u_fine = np.linspace(0, 1, num_points)
    smooth_points = splev(u_fine, tck)
    return list(zip(smooth_points[0], smooth_points[1]))

# Generate the smooth path points
smooth_path = generate_smooth_path(control_points, num_points=500)  # More points for smoother animation

# Function to draw the path gradually
def draw_path_slowly(screen, background_image, path_points, color, width=3, delay=0.01):
    for i in range(1, len(path_points)):
        # Draw the background image to clear previous drawings
        screen.blit(background_image, (0, 0))
        
        # Draw the line segment up to the current point
        pygame.draw.lines(screen, color, False, path_points[:i+1], width)
        
        # Update the display
        pygame.display.flip()
        
        # Wait for a short period to create animation effect
        time.sleep(delay)

# Main loop
running = True
path_drawn = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Only draw the path once at the beginning
    if not path_drawn:
        draw_path_slowly(screen, background_image, smooth_path, RED, 6, 0.005)
        path_drawn = True
    
    # After the path is drawn, keep the background and path visible
    else:
        # Redraw the background and the complete path
        screen.blit(background_image, (0, 0))
        pygame.draw.lines(screen, RED, False, smooth_path, 6)  # Full path drawn

    # Update the display continuously to keep the window open
    pygame.display.flip()