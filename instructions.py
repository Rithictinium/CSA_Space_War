import pygame
import sys

def show_instructions(screen, font):
    """
    Displays the game instructions with fullscreen toggle functionality.

    Args:
        screen (pygame.Surface): The game screen.
        font (pygame.font.Font): The font used to render the text.
    """
    # Define colors
    background_color = (0, 0, 0)
    text_color = (243, 216, 63)
    button_color = (255, 0, 0)

    # Define the instructions text
    instructions = [
        "### Space War: Quick Instructions ###",
        "",
        "- Goal: Hit the mystery ship 3 times to win. Avoid losing all 3 lives before that.",
        "",
        "- Controls:",
        "  Arrow Keys (←/→): Move the spaceship.",
        "  Spacebar: Shoot lasers.",
        "",
        "- Scoring:",
        "  Destroy aliens (100–300 points based on type).",
        "  Hit the mystery ship for 500 points.",
        "",
        "- Win/Lose:",
        "  Win: Hit the mystery ship 3 times.",
        "  Lose: Fail to hit the mystery ship 3 times AND lose all lives.",
        "",
        "Good luck and have fun!"
    ]

    fullscreen = False
    font_small = pygame.font.Font(None, 24)  # Smaller font size

    # Load and scale background image
    background_image = pygame.image.load('Graphics/inst.png')  # Make sure the image is in the correct folder
    background_image = pygame.transform.scale(background_image, (screen.get_width(), screen.get_height()))  # Scale it to the screen size

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:  # Toggle fullscreen
                    fullscreen = not fullscreen
                    if fullscreen:
                        screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode((750, 700))  # Return to windowed mode

                if event.key == pygame.K_ESCAPE and fullscreen:  # Exit fullscreen
                    fullscreen = False
                    screen = pygame.display.set_mode((750, 700))

                if event.key == pygame.K_SPACE:  # Start the game
                    running = False

        # Draw the background image first
        screen.blit(background_image, (0, 0))

        # Display instructions on top of the background
        y_offset = 30
        for line in instructions:
            text_surface = font_small.render(line, True, text_color)
            screen.blit(text_surface, (30, y_offset))
            y_offset += 25

        continue_text = font_small.render("Press SPACE to start the game!", True, button_color)
        screen.blit(continue_text, (screen.get_width() // 2 - continue_text.get_width() // 2, y_offset + 40))

        pygame.display.update()
import pygame
import sys

def show_instructions(screen, font):
    """
    Displays the game instructions with fullscreen toggle functionality and centers the text on the background.

    Args:
        screen (pygame.Surface): The game screen.
        font (pygame.font.Font): The font used to render the text.
    """
    # Define colors
    background_color = (0, 0, 0)
    text_color = (243, 216, 63)
    button_color = (255, 0, 0)

    # Define the instructions text
    instructions = [
        "Space War: Quick Instructions",
        "",
        "- Goal: Hit the mystery ship 3 times to win. Avoid losing all 3 lives before that.",
        "",
        "- Controls:",
        "  Arrow Keys: Move the spaceship.",
        "  Spacebar: Shoot lasers.",
        "",
        "- Scoring:",
        "  Destroy aliens (100–300 points based on type).",
        "  Hit the mystery ship for 500 points.",
        "",
        "- Win/Lose:",
        "  Win: Hit the mystery ship 3 times.",
        "  Lose: Fail to hit the mystery ship 3 times AND lose all lives.",
        "",
        "Good luck and have fun!"
    ]

    fullscreen = False
    font_small = pygame.font.Font(None, 24)  # Smaller font size

    # Load and scale background image
    background_image = pygame.image.load('Graphics/inst.png')  # Ensure the image is in the correct folder
    background_image = pygame.transform.scale(background_image, (screen.get_width(), screen.get_height()))  # Scale it to the screen size

    # Calculate the total height of the instructions block
    line_height = 25  # Height of each line
    total_text_height = line_height * len(instructions)  # Total height of all lines combined
    y_start = (screen.get_height() - total_text_height) // 2  # Start position to vertically center the text

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:  # Toggle fullscreen
                    fullscreen = not fullscreen
                    if fullscreen:
                        screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode((750, 700))  # Return to windowed mode

                if event.key == pygame.K_ESCAPE and fullscreen:  # Exit fullscreen
                    fullscreen = False
                    screen = pygame.display.set_mode((750, 700))

                if event.key == pygame.K_SPACE:  # Start the game
                    running = False

        # Draw the background image first
        screen.blit(background_image, (0, 0))

        # Display instructions on top of the background
        y_offset = y_start  # Start from the calculated vertical center
        for line in instructions:
            text_surface = font_small.render(line, True, text_color)
            screen.blit(text_surface, (screen.get_width() // 2 - text_surface.get_width() // 2, y_offset))
            y_offset += line_height

        # Display the "Press SPACE" text below the instructions
        continue_text = font_small.render("Press SPACE to start the game!", True, button_color)
        screen.blit(continue_text, (screen.get_width() // 2 - continue_text.get_width() // 2, y_offset + 40))

        pygame.display.update()


