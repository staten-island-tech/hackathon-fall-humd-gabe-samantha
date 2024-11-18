import pygame

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Virtual Piano")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (100, 100, 255)

# Load piano sounds
NOTE_SOUNDS = {
    "A": pygame.mixer.Sound("sounds/c.wav"),  # C note
    "S": pygame.mixer.Sound("sounds/d.wav"),  # D note
    "D": pygame.mixer.Sound("sounds/e.wav"),  # E note
    "F": pygame.mixer.Sound("sounds/f.wav"),  # F note
    "G": pygame.mixer.Sound("sounds/g.wav"),  # G note
    "H": pygame.mixer.Sound("sounds/a.wav"),  # A note
    "J": pygame.mixer.Sound("sounds/b.wav"),  # B note
    "K": pygame.mixer.Sound("sounds/c_high.wav"),  # High C note
}

# Piano key mapping
KEY_MAPPING = {
    "A": {"pos": (50, 200, 80, 180)},  # x, y, width, height
    "S": {"pos": (150, 200, 80, 180)},
    "D": {"pos": (250, 200, 80, 180)},
    "F": {"pos": (350, 200, 80, 180)},
    "G": {"pos": (450, 200, 80, 180)},
    "H": {"pos": (550, 200, 80, 180)},
    "J": {"pos": (650, 200, 80, 180)},
    "K": {"pos": (750, 200, 80, 180)},
}

def draw_piano(keys_pressed):
    """Draw the piano keys."""
    screen.fill(WHITE)
    for key, data in KEY_MAPPING.items():
        rect = data["pos"]
        color = BLUE if key in keys_pressed else BLACK
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, GRAY, rect, 2)  # Outline

def play_sound(key):
    """Play the sound for the given key."""
    if key in NOTE_SOUNDS:
        NOTE_SOUNDS[key].play()

# Main game loop
def main():
    running = True
    keys_pressed = set()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                key = pygame.key.name(event.key).upper()
                if key in NOTE_SOUNDS:
                    keys_pressed.add(key)
                    play_sound(key)
            elif event.type == pygame.KEYUP:
                key = pygame.key.name(event.key).upper()
                if key in keys_pressed:
                    keys_pressed.remove(key)

        draw_piano(keys_pressed)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()