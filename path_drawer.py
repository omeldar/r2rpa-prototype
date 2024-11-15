import pygame

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