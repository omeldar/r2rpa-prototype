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

RED = (200, 25, 25)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define control points as relative positions (percentages of the original image dimensions)
s1_s41 = [
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

# Define control points for S1 to S12
s1_s12 = [
    (0.17, 0.85),
    (0.18, 0.91),
    (0.26, 0.87),
    (0.355, 0.84),
    (0.358, 0.755),
    (0.445, 0.72),
    (0.46, 0.698),
    (0.54, 0.679),
    (0.555, 0.67),
    (0.567, 0.73)
]

# Define control points for S12 to S41
s12_s41 = [
    (0.567, 0.73),
    (0.555, 0.67),
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
s1_s41_points = get_absolute_points(s1_s41, screen_width, screen_height)
s1_s12_points = get_absolute_points(s1_s12, screen_width, screen_height)
s12_s41_points = get_absolute_points(s12_s41, screen_width, screen_height)

control_points = s1_s41_points  # Default to S1 to S41 path

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

# Function to draw the path between selected points
def draw_selected_path(screen, background_image, control_points, color, width=3):
    # Always draw the full path
    path_points = control_points
    
    # Draw the background image
    screen.blit(background_image, (0, 0))
    
    # Draw the selected path
    pygame.draw.lines(screen, color, False, path_points, width)
    
    # Update the display
    pygame.display.flip()
    return path_points

# Main loop
running = True
path_drawn = False
font = pygame.font.Font(None, 36)

# Dropdown state variables
from_index = 0
to_index = 0
dropdown_open = False
selected_dropdown = None
dropdown_options = ['S1', 'S12', 'S41']
button_rect = pygame.Rect(screen_width - 200, 120, 150, 40)

# Store the currently drawn path points
current_path_points = []

def draw_ui():
    # Draw "FROM" dropdown
    from_dropdown_rect = pygame.Rect(screen_width - 200, 20, 150, 40)
    to_dropdown_rect = pygame.Rect(screen_width - 200, 70, 150, 40)
    pygame.draw.rect(screen, WHITE, from_dropdown_rect)
    pygame.draw.rect(screen, WHITE, to_dropdown_rect)
    
    # Draw text for "FROM" and "TO"
    from_text = font.render(f"FROM: {dropdown_options[from_index]}", True, BLACK)
    to_text = font.render(f"TO: {dropdown_options[to_index]}", True, BLACK)
    screen.blit(from_text, (screen_width - 190, 25))
    screen.blit(to_text, (screen_width - 190, 75))
    
    # Draw button
    pygame.draw.rect(screen, WHITE, button_rect)
    button_text = font.render("DRAW PATH", True, BLACK)
    screen.blit(button_text, (screen_width - 185, 125))

while running:
    screen.blit(background_image, (0, 0))
    draw_ui()

    # If a path has been drawn, keep it displayed
    if path_drawn and current_path_points:
        pygame.draw.lines(screen, RED, False, current_path_points, 10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            # Allow the user to exit fullscreen mode by pressing ESC
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            from_dropdown_rect = pygame.Rect(screen_width - 200, 20, 150, 40)
            to_dropdown_rect = pygame.Rect(screen_width - 200, 70, 150, 40)
            
            # Check if "FROM" dropdown clicked
            if from_dropdown_rect.collidepoint(mouse_pos):
                selected_dropdown = "FROM"
                dropdown_open = True
            # Check if "TO" dropdown clicked
            elif to_dropdown_rect.collidepoint(mouse_pos):
                selected_dropdown = "TO"
                dropdown_open = True
            # Check if button clicked
            elif button_rect.collidepoint(mouse_pos):
                # Clear the old path first
                screen.blit(background_image, (0, 0))
                pygame.display.flip()
                time.sleep(1)
                # Draw the new path
                if dropdown_options[from_index] == 'S1' and dropdown_options[to_index] == 'S12':
                    control_points = s1_s12_points
                elif dropdown_options[from_index] == 'S12' and dropdown_options[to_index] == 'S1':
                    control_points = list(reversed(s1_s12_points))
                elif dropdown_options[from_index] == 'S1' and dropdown_options[to_index] == 'S41':
                    control_points = s1_s41_points
                elif dropdown_options[from_index] == 'S41' and dropdown_options[to_index] == 'S1':
                    control_points = list(reversed(s1_s41_points))
                elif dropdown_options[from_index] == 'S12' and dropdown_options[to_index] == 'S41':
                    control_points = s12_s41_points
                elif dropdown_options[from_index] == 'S41' and dropdown_options[to_index] == 'S12':
                    control_points = list(reversed(s12_s41_points))
                elif dropdown_options[from_index] == 'S12' and dropdown_options[to_index] == 'S41':
                    control_points = s12_s41_points
                else:
                    control_points = s1_s41_points
                draw_path_slowly(screen, background_image, control_points, RED, 10, delay=0.1)
                current_path_points = control_points
                path_drawn = True
            else:
                dropdown_open = False
        elif event.type == pygame.MOUSEBUTTONUP and dropdown_open:
            mouse_pos = event.pos
            for i in range(len(dropdown_options)):
                option_rect = pygame.Rect(screen_width - 200, 20 + i * 30, 150, 30)
                if option_rect.collidepoint(mouse_pos):
                    if selected_dropdown == "FROM":
                      from_index = i
                    elif selected_dropdown == "TO":
                      to_index = i
                    dropdown_open = False

    # Draw dropdown options if open
    if dropdown_open:
        for i in range(len(dropdown_options)):
            option_rect = pygame.Rect(screen_width - 200, 20 + i * 30, 150, 30)
            pygame.draw.rect(screen, WHITE, option_rect)
            option_text = font.render(dropdown_options[i], True, BLACK)
            screen.blit(option_text, (screen_width - 190, 25 + i * 30))

    pygame.display.flip()

# Clean up and exit
pygame.quit()
