import pygame

def login_screen(screen):
    pygame.init()

    # Screen dimensions and colors
    SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()
    BG_COLOR = (0, 0, 0)
    TEXT_COLOR = (255, 255, 255)
    INPUT_BOX_COLOR = (50, 50, 50)  # Color for the input boxes 
    ACTIVE_BOX_COLOR = (100, 100, 100)  # Darker shade when active
    BUTTON_COLOR = (0, 128, 0)  # Green button color
    BUTTON_TEXT_COLOR = (255, 255, 255)  # White color for button text

    # Orange color for text
    ORANGE = (255, 165, 0)

    # Fonts
    font = pygame.font.Font(None, 50)

    # Input boxes and text
    name_box = pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 3, 300, 50)
    age_box = pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2, 300, 50)

    # Initial values
    name_text = ""
    age_text = ""
    active_box = None
    error_message = ""

    # Render button
    button_font = pygame.font.Font(None, 40)
    button_text = button_font.render("START", True, BUTTON_TEXT_COLOR)
    button_box = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT * 2 // 3, 200, 50)

    # Fullscreen toggle state
    fullscreen = False

    # Load background image
    background = pygame.image.load("Graphics/login_background.png")
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))  # Scale to fit the screen

    clock = pygame.time.Clock()

    while True:
        screen.fill(BG_COLOR)

        # Draw the background image
        screen.blit(background, (0, 0))

        # Draw input boxes (keep them the same color)
        pygame.draw.rect(screen, ACTIVE_BOX_COLOR if active_box == "name" else INPUT_BOX_COLOR, name_box, 0, 5)
        pygame.draw.rect(screen, ACTIVE_BOX_COLOR if active_box == "age" else INPUT_BOX_COLOR, age_box, 0, 5)

        # Draw start button with green color
        pygame.draw.rect(screen, BUTTON_COLOR, button_box, 0, 5)

        # Render instructions with orange color
        name_label = font.render("Enter Name:", True, ORANGE)
        age_label = font.render("Enter Age:", True, ORANGE)
        screen.blit(name_label, (name_box.x, name_box.y - 40))
        screen.blit(age_label, (age_box.x, age_box.y - 40))

        # Render input text
        name_surface = font.render(name_text, True, TEXT_COLOR)
        age_surface = font.render(age_text, True, TEXT_COLOR)
        screen.blit(name_surface, (name_box.x + 10, name_box.y + 10))
        screen.blit(age_surface, (age_box.x + 10, age_box.y + 10))

        # Render start button text with white color
        screen.blit(button_text, (button_box.x + 50, button_box.y + 10))

        # Render error message
        if error_message:
            error_surface = font.render(error_message, True, (255, 0, 0))
            screen.blit(error_surface, (SCREEN_WIDTH // 2 - error_surface.get_width() // 2, SCREEN_HEIGHT * 3 // 4))

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if input boxes are clicked
                if name_box.collidepoint(event.pos):
                    active_box = "name"
                elif age_box.collidepoint(event.pos):
                    active_box = "age"
                elif button_box.collidepoint(event.pos):
                    # Validate and proceed
                    if name_text.strip() and age_text.strip().isdigit():
                        return name_text.strip(), int(age_text.strip())
                    else:
                        error_message = "Please enter a valid name and age!"
                else:
                    active_box = None
            elif event.type == pygame.KEYDOWN:
                # Fullscreen toggling
                if event.key == pygame.K_f:
                    fullscreen = not fullscreen
                    if fullscreen:
                        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
                # Exit fullscreen
                elif event.key == pygame.K_ESCAPE and fullscreen:
                    fullscreen = False
                    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

                # Input handling
                if active_box == "name":
                    if event.key == pygame.K_BACKSPACE:
                        name_text = name_text[:-1]
                    elif event.key == pygame.K_RETURN:
                        active_box = "age"  
                    else:
                        name_text += event.unicode
                elif active_box == "age":
                    if event.key == pygame.K_BACKSPACE:
                        age_text = age_text[:-1]
                    elif event.key == pygame.K_RETURN:
                        active_box = "name"  
                    elif event.unicode.isdigit():
                        age_text += event.unicode

        pygame.display.update()
        clock.tick(30)
