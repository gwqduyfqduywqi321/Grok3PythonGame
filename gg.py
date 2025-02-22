import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Set up window dimensions
WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Orbital animation with asteroids")

# Define colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
GRAY = (150, 150, 150)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Define parameters for the simulation
earth_radius = 100
ship_distance = 200  # Distance of the ship from Earth's center
ship_angle = 0
ship_speed = 0.05  # Rotation speed of the ship
astronaut_y = HEIGHT // 2  # Initial position of the astronaut inside the ship
camera_mode = "outside"  # Starting camera mode: outside view

# Set up font for text rendering
font = pygame.font.Font(None, 36)

# Define Asteroid class for creating and managing asteroids
class Asteroid:
    def __init__(self):
        # Randomly initialize asteroid position and speed
        self.x = random.randint(-100, WIDTH + 100)
        self.y = random.randint(-100, HEIGHT + 100)
        self.speed_x = random.uniform(-2, 2)
        self.speed_y = random.uniform(-2, 2)
        self.size = random.randint(5, 15)

    def update(self):
        # Update asteroid position based on speed
        self.x += self.speed_x
        self.y += self.speed_y
        # Respawn asteroid if it goes off-screen
        if self.x < -100 or self.x > WIDTH + 100 or self.y < -100 or self.y > HEIGHT + 100:
            self.x = random.randint(-100, WIDTH + 100)
            self.y = random.randint(-100, HEIGHT + 100)
            self.speed_x = random.uniform(-2, 2)
            self.speed_y = random.uniform(-2, 2)

    def draw(self, surface):
        # Draw the asteroid as a yellow circle
        pygame.draw.circle(surface, YELLOW, (int(self.x), int(self.y)), self.size)

# Create a list of 10 asteroids
asteroids = [Asteroid() for _ in range(10)]  # 10 asteroids

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Exit the loop if the window is closed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:  # Switch camera mode with 'C' key
                camera_mode = "inside" if camera_mode == "outside" else "outside"

    # Handle ship speed control with arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        ship_speed += 0.001  # Increase ship speed
    if keys[pygame.K_DOWN]:
        ship_speed -= 0.001  # Decrease ship speed

    # Limit ship speed to a reasonable range
    ship_speed = max(0.01, min(ship_speed, 0.1))  # Minimum 0.01, maximum 0.1

    # Update ship angle based on speed
    ship_angle += ship_speed

    # Update positions of all asteroids
    for asteroid in asteroids:
        asteroid.update()

    # Clear the screen with black (space background)
    screen.fill(BLACK)

    # Draw based on camera mode
    if camera_mode == "outside":
        # Draw Earth in the center
        pygame.draw.circle(screen, GREEN, (WIDTH // 2, HEIGHT // 2), earth_radius)
        
        # Calculate ship position on orbit
        ship_x = WIDTH // 2 + math.cos(ship_angle) * ship_distance
        ship_y = HEIGHT // 2 + math.sin(ship_angle) * ship_distance
        pygame.draw.rect(screen, GRAY, (ship_x - 10, ship_y - 10, 20, 20))  # Draw the ship

        # Draw all asteroids
        for asteroid in asteroids:
            asteroid.draw(screen)

        # Display "External View" text
        text = font.render("External View", True, WHITE)
        screen.blit(text, (10, 10))

    elif camera_mode == "inside":
        # Draw ship walls for internal view
        pygame.draw.rect(screen, GRAY, (0, 0, WIDTH, HEIGHT), 10)
        
        # Draw astronaut floating (sinusoidal movement up and down)
        astronaut_y = HEIGHT // 2 + math.sin(pygame.time.get_ticks() * 0.002) * 50
        pygame.draw.circle(screen, RED, (WIDTH // 2, int(astronaut_y)), 15)  # Draw astronaut

        # Draw radar
        radar_x, radar_y = WIDTH - 150, HEIGHT - 150  # Radar position
        radar_radius = 100
        
        # Draw radar background
        pygame.draw.circle(screen, GRAY, (radar_x, radar_y), radar_radius)
        pygame.draw.circle(screen, BLACK, (radar_x, radar_y), radar_radius - 5)
        
        # Draw radar waves (animated)
        wave_radius = (pygame.time.get_ticks() % 1000) / 1000 * radar_radius
        pygame.draw.circle(screen, GREEN, (radar_x, radar_y), int(wave_radius), 2)
        
        # Calculate Earth's position relative to the ship on radar
        earth_angle = -ship_angle  # Invert angle for internal perspective
        earth_dist = radar_radius * 0.7  # Distance of Earth on radar
        earth_x = radar_x + math.cos(earth_angle) * earth_dist
        earth_y = radar_y + math.sin(earth_angle) * earth_dist
        pygame.draw.circle(screen, GREEN, (int(earth_x), int(earth_y)), 10)
        
        # Indicate space (opposite direction)
        space_x = radar_x - math.cos(earth_angle) * earth_dist
        space_y = radar_y - math.sin(earth_angle) * earth_dist
        pygame.draw.circle(screen, BLUE, (int(space_x), int(space_y)), 5)

        # Calculate ship position (center of radar)
        ship_x = WIDTH // 2 + math.cos(ship_angle) * ship_distance
        ship_y = HEIGHT // 2 + math.sin(ship_angle) * ship_distance

        # Display asteroids on radar
        for asteroid in asteroids:
            # Calculate relative position of asteroid to ship
            rel_x = asteroid.x - ship_x
            rel_y = asteroid.y - ship_y
            distance = math.sqrt(rel_x**2 + rel_y**2)
            
            # Scale distance to fit radar size
            if distance > 0:  # Avoid division by zero
                radar_scale = min(1, radar_radius / distance)  # Limit scale
                asteroid_radar_x = radar_x + rel_x * radar_scale
                asteroid_radar_y = radar_y + rel_y * radar_scale
                pygame.draw.circle(screen, YELLOW, (int(asteroid_radar_x), int(asteroid_radar_y)), 3)

        # Display "Radar" label
        radar_text = font.render("Radar", True, WHITE)
        screen.blit(radar_text, (radar_x - 30, radar_y - radar_radius - 30))
        
        # Display "Internal View" text
        text = font.render("Internal View", True, WHITE)
        screen.blit(text, (10, 10))

    # Display current ship speed
    speed_text = font.render(f"Speed: {ship_speed:.3f}", True, WHITE)
    screen.blit(speed_text, (10, 50))
    
    # Update the display
    pygame.display.flip()
    clock.tick(60)  # Limit to 60 FPS

pygame.quit()  # Quit Pygame when the loop ends
