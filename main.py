import pygame, sys, random
from game import Game
from login_page import login_screen
from database import Database
from instructions import show_instructions  
# Initialize Pygame
pygame.init()

# Screen dimensions and offset
SCREEN_WIDTH = 750
SCREEN_HEIGHT = 700
OFFSET = 50

# Load and scale background image
background = pygame.image.load("Graphics/black-hole.png")
background = pygame.transform.scale(background, (SCREEN_WIDTH + OFFSET, SCREEN_HEIGHT + 2 * OFFSET))

# Setup screen
screen = pygame.display.set_mode((SCREEN_WIDTH + OFFSET, SCREEN_HEIGHT + 2 * OFFSET))
pygame.display.set_caption("Python Space Invaders")

# Initialize Database
db = Database()

# Show the login screen and get player details
player_name, player_age = login_screen(screen)

# Add the player to the database
db.add_player(player_name, player_age)

# Show the instruction screen before starting the game
font = pygame.font.Font(None, 40)
show_instructions(screen, font)

# Initialize clock and game instance
clock = pygame.time.Clock()
game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, OFFSET)

# Custom events
SHOOT_LASER = pygame.USEREVENT
pygame.time.set_timer(SHOOT_LASER, 300)

MYSTERYSHIP = pygame.USEREVENT + 1
pygame.time.set_timer(MYSTERYSHIP, random.randint(4000, 8000))

# Fullscreen toggle state
fullscreen = False

# Pause state
paused = False

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == SHOOT_LASER and not paused and game.run:
            game.alien_shoot_laser()

        if event.type == MYSTERYSHIP and not paused and game.run:
            game.create_mystery_ship()
            pygame.time.set_timer(MYSTERYSHIP, random.randint(4000, 8000))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((SCREEN_WIDTH + OFFSET, SCREEN_HEIGHT + 2 * OFFSET), pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode((SCREEN_WIDTH + OFFSET, SCREEN_HEIGHT + 2 * OFFSET))

            if event.key == pygame.K_ESCAPE and fullscreen:
                fullscreen = False
                screen = pygame.display.set_mode((SCREEN_WIDTH + OFFSET, SCREEN_HEIGHT + 2 * OFFSET))

            # Pause and resume functionality
            if event.key == pygame.K_p:
                paused = not paused  # Toggle the paused state

            # Reset the game when space is pressed after game over
            if event.key == pygame.K_SPACE and not game.run:
                game.reset()

    if not paused:  # Only update game elements if not paused
        if game.run:
            game.spaceship_group.update()
            game.move_aliens()
            game.alien_lasers_group.update()
            game.mystery_ship_group.update()
            game.check_for_collisions()

    # Draw background and UI
    screen.blit(background, (0, 0))
    
    pygame.draw.rect(screen, (243, 216, 63), (10, 10, 780, 780), 2) 
    pygame.draw.line(screen, (243, 216, 63), (25, 730), (775, 730), 3)

    # Draw lives
    x = 50
    for life in range(game.lives):
        screen.blit(game.spaceship_group.sprite.image, (x, 745))
        x += 50

    # Display hits and game status
    hits_surface = font.render(f"HITS {game.mystery_ship_hits}", False, (243, 216, 63))
    status_surface = None
    if not game.run:
        if game.game_status == "win":
            status_surface = font.render("YOU WIN!", False, (0, 255, 0))
            # Update stats in the database (increase wins)
            db.update_stats(player_name, game.mystery_ship_hits, game.lives)
        elif game.game_status == "game over":
            status_surface = font.render("GAME OVER", False, (255, 0, 0))
            # Update stats in the database (increase losses)
            db.update_stats(player_name, game.mystery_ship_hits, game.lives)

    # Place hits at the left, and status in the center
    screen.blit(hits_surface, (570, 745))

    # If there is a status message, display it in the center of the row
    if status_surface:
        text_width = status_surface.get_width()
        screen.blit(status_surface, ((SCREEN_WIDTH - text_width) // 2, 745))  # Center the message

    # Draw game elements
    game.spaceship_group.draw(screen)
    game.spaceship_group.sprite.lasers_group.draw(screen)
    for obstacle in game.obstacles:
        obstacle.blocks_group.draw(screen)
    game.aliens_group.draw(screen)
    game.alien_lasers_group.draw(screen)
    game.mystery_ship_group.draw(screen)

    # If the game is paused, display a pause message
    if paused:
        pause_text = font.render("PAUSED", True, (255, 0, 0))
        screen.blit(pause_text, (SCREEN_WIDTH // 2 - pause_text.get_width() // 2, SCREEN_HEIGHT // 2))

    pygame.display.update()
    clock.tick(60)
