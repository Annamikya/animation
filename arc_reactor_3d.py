import pygame
import math
import random
import sys

pygame.init()

# ==========================================
# WINDOW
# ==========================================

WIDTH = 1000
HEIGHT = 750

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Iron Man Style Arc Reactor 3D")

clock = pygame.time.Clock()

CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2

# ==========================================
# SETTINGS
# ==========================================

angle = 0
rotation_speed = 1.5
running_animation = True

pulse = 0

sparks = []

font = pygame.font.SysFont("consolas", 20)
big_font = pygame.font.SysFont("consolas", 28, bold=True)

# ==========================================
# COLORS
# ==========================================

BACKGROUND = (3, 7, 15)

CYAN = (0, 220, 255)
LIGHT_CYAN = (120, 245, 255)
WHITE = (255, 255, 255)

DARK_BLUE = (5, 40, 70)
METAL = (70, 80, 90)

ORANGE = (255, 120, 20)

# ==========================================
# GLOW CIRCLE
# ==========================================

def glow_circle(surface, center, radius, color):

    glow = pygame.Surface(
        (radius * 4, radius * 4),
        pygame.SRCALPHA
    )

    gx = radius * 2
    gy = radius * 2

    for r in range(radius * 2, radius, -5):

        alpha = max(
            0,
            int(
                100 *
                (1 - (r - radius) / radius)
            )
        )

        pygame.draw.circle(
            glow,
            (*color, alpha),
            (gx, gy),
            r
        )

    surface.blit(
        glow,
        (
            center[0] - gx,
            center[1] - gy
        )
    )

# ==========================================
# 3D RING
# ==========================================

def draw_3d_ring(radius, thickness, rotation, segments=16):

    for i in range(segments):

        angle1 = math.radians(
            i * (360 / segments) + rotation
        )

        angle2 = math.radians(
            (i + 0.65) *
            (360 / segments) +
            rotation
        )

        x1 = CENTER_X + math.cos(angle1) * radius
        y1 = CENTER_Y + math.sin(angle1) * radius * 0.88

        x2 = CENTER_X + math.cos(angle2) * radius
        y2 = CENTER_Y + math.sin(angle2) * radius * 0.88

        pygame.draw.line(
            screen,
            CYAN,
            (x1, y1),
            (x2, y2),
            thickness
        )

# ==========================================
# METAL RING
# ==========================================

def draw_metal_ring(radius):

    pygame.draw.ellipse(
        screen,
        METAL,
        (
            CENTER_X - radius,
            CENTER_Y - radius * 0.88,
            radius * 2,
            radius * 1.76
        ),
        8
    )

# ==========================================
# ENERGY MODULES
# ==========================================

def draw_energy_modules(radius, rotation):

    modules = 12

    for i in range(modules):

        a = math.radians(
            i * (360 / modules) + rotation
        )

        x = CENTER_X + math.cos(a) * radius
        y = CENTER_Y + math.sin(a) * radius * 0.88

        pygame.draw.circle(
            screen,
            DARK_BLUE,
            (int(x), int(y)),
            20
        )

        glow_circle(
            screen,
            (int(x), int(y)),
            12,
            CYAN
        )

        pygame.draw.circle(
            screen,
            LIGHT_CYAN,
            (int(x), int(y)),
            8
        )

# ==========================================
# TRIANGLE CORE
# ==========================================

def draw_triangle_core(size):

    points = []

    for i in range(3):

        a = math.radians(
            -90 + i * 120
        )

        x = CENTER_X + math.cos(a) * size
        y = CENTER_Y + math.sin(a) * size

        points.append((x, y))

    # Glow layers
    for thickness in [20, 15, 10]:

        pygame.draw.polygon(
            screen,
            CYAN,
            points,
            thickness
        )

    pygame.draw.polygon(
        screen,
        WHITE,
        points,
        4
    )

# ==========================================
# INNER ROTATING BLADES
# ==========================================

def draw_blades(radius, rotation):

    blades = 8

    for i in range(blades):

        a = math.radians(
            i * (360 / blades) - rotation
        )

        inner = radius * 0.45

        x1 = CENTER_X + math.cos(a) * inner
        y1 = CENTER_Y + math.sin(a) * inner

        x2 = CENTER_X + math.cos(a) * radius
        y2 = CENTER_Y + math.sin(a) * radius

        pygame.draw.line(
            screen,
            LIGHT_CYAN,
            (x1, y1),
            (x2, y2),
            4
        )

# ==========================================
# SPARKS
# ==========================================

def create_spark():

    a = random.uniform(
        0,
        math.pi * 2
    )

    radius = random.randint(
        250,
        350
    )

    x = CENTER_X + math.cos(a) * radius
    y = CENTER_Y + math.sin(a) * radius

    dx = random.uniform(-2, 2)
    dy = random.uniform(-3, 1)

    sparks.append(
        [
            x,
            y,
            dx,
            dy,
            random.randint(20, 45)
        ]
    )

def update_sparks():

    for spark in sparks[:]:

        x, y, dx, dy, life = spark

        x += dx
        y += dy

        dy += 0.03

        life -= 1

        spark[0] = x
        spark[1] = y
        spark[2] = dx
        spark[3] = dy
        spark[4] = life

        if life <= 0:

            sparks.remove(spark)

        else:

            pygame.draw.circle(
                screen,
                ORANGE,
                (int(x), int(y)),
                2
            )

# ==========================================
# UI
# ==========================================

def draw_ui():

    title = big_font.render(
        "ARC REACTOR SYSTEM",
        True,
        CYAN
    )

    screen.blit(
        title,
        (25, 20)
    )

    instructions = [
        "R = Reverse Rotation",
        "SPACE = Start / Stop",
        "+ = Increase Speed",
        "- = Decrease Speed",
        "ESC = Exit"
    ]

    y = 70

    for text in instructions:

        line = font.render(
            text,
            True,
            WHITE
        )

        screen.blit(
            line,
            (25, y)
        )

        y += 30

    speed_text = font.render(
        f"Speed: {abs(rotation_speed):.2f}",
        True,
        LIGHT_CYAN
    )

    screen.blit(
        speed_text,
        (25, 240)
    )

    status = (
        "ONLINE"
        if running_animation
        else
        "PAUSED"
    )

    status_text = font.render(
        f"Reactor: {status}",
        True,
        CYAN
    )

    screen.blit(
        status_text,
        (WIDTH - 250, 30)
    )

# ==========================================
# MAIN LOOP
# ==========================================

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        if event.type == pygame.KEYDOWN:

            # Exit
            if event.key == pygame.K_ESCAPE:

                running = False

            # Reverse
            elif event.key == pygame.K_r:

                rotation_speed *= -1

            # Start / Stop
            elif event.key == pygame.K_SPACE:

                running_animation = not running_animation

            # Increase speed
            elif event.key in [
                pygame.K_PLUS,
                pygame.K_EQUALS
            ]:

                if rotation_speed >= 0:
                    rotation_speed += 0.3
                else:
                    rotation_speed -= 0.3

            # Decrease speed
            elif event.key == pygame.K_MINUS:

                if rotation_speed > 0:

                    rotation_speed = max(
                        0.2,
                        rotation_speed - 0.3
                    )

                elif rotation_speed < 0:

                    rotation_speed = min(
                        -0.2,
                        rotation_speed + 0.3
                    )

    # ======================================
    # BACKGROUND
    # ======================================

    screen.fill(BACKGROUND)

    # ======================================
    # ANIMATION
    # ======================================

    if running_animation:

        angle += rotation_speed
        pulse += 0.06

    # Pulse size
    pulse_value = (
        math.sin(pulse) + 1
    ) / 2

    core_radius = int(
        55 + pulse_value * 12
    )

    # ======================================
    # OUTER GLOW
    # ======================================

    glow_circle(
        screen,
        (CENTER_X, CENTER_Y),
        250,
        DARK_BLUE
    )

    # ======================================
    # ARC REACTOR LAYERS
    # ======================================

    draw_metal_ring(260)

    draw_3d_ring(
        230,
        7,
        angle
    )

    draw_energy_modules(
        195,
        -angle * 0.7
    )

    draw_metal_ring(165)

    draw_3d_ring(
        145,
        5,
        -angle * 1.3,
        20
    )

    draw_blades(
        125,
        angle * 1.5
    )

    # ======================================
    # CORE GLOW
    # ======================================

    glow_circle(
        screen,
        (CENTER_X, CENTER_Y),
        core_radius,
        CYAN
    )

    pygame.draw.circle(
        screen,
        LIGHT_CYAN,
        (CENTER_X, CENTER_Y),
        core_radius
    )

    pygame.draw.circle(
        screen,
        WHITE,
        (CENTER_X, CENTER_Y),
        int(core_radius * 0.55)
    )

    # ======================================
    # TRIANGLE
    # ======================================

    draw_triangle_core(85)

    # ======================================
    # SPARKS
    # ======================================

    if random.random() < 0.25:

        create_spark()

    update_sparks()

    # ======================================
    # UI
    # ======================================

    draw_ui()

    # Footer
    footer = font.render(
        "PROOF THAT TONY STARK HAS A HEART",
        True,
        CYAN
    )

    footer_rect = footer.get_rect(
        center=(WIDTH // 2, HEIGHT - 30)
    )

    screen.blit(
        footer,
        footer_rect
    )

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()