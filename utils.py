import pygame
import time

# Convert relative points to absolute coordinates based on the screen size
def get_absolute_points(relative_points, screen_width, screen_height):
    return [(int(x * screen_width), int(y * screen_height)) for x, y in relative_points]

# Function to draw the path gradually
def draw_path_slowly(screen, background_image, path_points, color, width=3, delay=0.1):
    for i in range(1, len(path_points)):
        # Draw the background image to clear previous drawings
        screen.blit(background_image, (0, 0))
        
        # Draw the line segment up to the current point
        pygame.draw.lines(screen, color, False, path_points[:i+1], width)
        
        # Update the display
        pygame.display.flip()
        
        # Wait for a short period to create animation effect
        time.sleep(delay)
