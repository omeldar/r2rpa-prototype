# main.py
import pygame
import sys
import time
import numpy as np

pygame.init()

# Get the display size for fullscreen mode
screen_info = pygame.display.Info()
screen_width, screen_height = screen_info.current_w, screen_info.current_h

# Set up the display in fullscreen mode
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("R2RPA Prototype")

# Load and scale the background image to fit the screen
image_path = "media/2D-Suurstoffi.png"
background_image = pygame.image.load(image_path)
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# Define colors
BLACK = (0, 0, 0)
RED = (200, 25, 25)

# Define control points as relative positions (percentages of the original image dimensions)
relative_control_points = [
    (0.17, 0.85),
    (0.18, 0.91),
    (0.26, 0.87),
    (0.355, 0.84),
    (0.358, 0.755),
    (0.445, 0.72),
    (0.46, 0.698),
    (0.54, 0.679),
    (0.565, 0.65),
    (0.62, 0.637),
    (0.658, 0.598),
    (0.72, 0.586),
    (0.748, 0.59),
    (0.79, 0.568),
    (0.791, 0.54),
    (0.83, 0.523),
    (0.88, 0.43),
    (0.91, 0.28),
    (0.87, 0.27)

]

# Convert relative points to absolute coordinates based on the screen size
def get_absolute_points(relative_points, screen_width, screen_height):
    return [(int(x * screen_width), int(y * screen_height)) for x, y in relative_points]

# Generate absolute points for the current screen size
control_points = get_absolute_points(relative_control_points, screen_width, screen_height)

# Function to generate a path with straight lines and smoothed corners between control points
def generate_smooth_corners_path(control_points, corner_radius=10, corner_points=5):
    path = []
    for i in range(len(control_points) - 1):
        p1 = control_points[i]
        p2 = control_points[i + 1]

        # Add the straight segment leading to the next point
        if i == 0:
            path.append(p1)
        else:
            # Move the end of the previous line to avoid overlap with the corner
            p1_adjusted = np.array(p1) + (np.array(p2) - np.array(p1)) / np.linalg.norm(np.array(p2) - np.array(p1)) * corner_radius
            path.append(tuple(p1_adjusted))

        # If there is a next segment, smooth the corner
        if i < len(control_points) - 2:
            p3 = control_points[i + 2]
            
            # Calculate vectors
            v1 = np.array(p2) - np.array(p1)
            v2 = np.array(p3) - np.array(p2)
            
            # Normalize the vectors
            v1 = v1 / np.linalg.norm(v1)
            v2 = v2 / np.linalg.norm(v2)
            
            # Find the tangent points for smoothing
            tangent1 = np.array(p2) - v1.astype(float) * corner_radius
            tangent2 = np.array(p2) + v2.astype(float) * corner_radius

            # Add the first tangent point
            path.append(tuple(tangent1))

            # Create points for the rounded corner arc
            arc_points = []
            for t in np.linspace(0, 1, corner_points):
                arc_point = (1 - t) * tangent1 + t * tangent2
                arc_points.append(tuple(arc_point))
            path.extend(arc_points)

    # Add the last point
    path.append(control_points[-1])
    return path

# Generate the path with smoothed corners
smooth_corners_path = generate_smooth_corners_path(control_points, corner_radius=10, corner_points=5)

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
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            # Allow the user to exit fullscreen mode by pressing ESC
            running = False

    # Only draw the path once at the beginning
    if not path_drawn:
        draw_path_slowly(screen, background_image, smooth_corners_path, RED, 10, 0.005)
        path_drawn = True
    
    # After the path is drawn, keep the background and path visible
    else:
        # Redraw the background and the complete path
        screen.blit(background_image, (0, 0))
        pygame.draw.lines(screen, RED, False, smooth_corners_path, 10)  # Full path drawn

    # Update the display continuously to keep the window open
    pygame.display.flip()

# Clean up and exit
pygame.quit()