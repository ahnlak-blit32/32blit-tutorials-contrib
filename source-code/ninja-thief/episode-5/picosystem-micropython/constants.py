# Screen size in pixels
SCREEN_WIDTH = 120
SCREEN_HEIGHT = 120

# Actual game area in pixels
GAME_WIDTH = 120
GAME_HEIGHT = 120

# Each sprite on the spritesheet is 8x8 pixels
SPRITE_SIZE = 8

# Size of the spritesheet in pixels (only needed for PicoSystem)
SPRITESHEET_WIDTH = SPRITE_SIZE * 8
SPRITESHEET_HEIGHT = SPRITE_SIZE * 6

# Offset of game area from top left corner
GAME_OFFSET_X = (SCREEN_WIDTH - GAME_WIDTH) // 2
GAME_OFFSET_Y = (SCREEN_HEIGHT - GAME_HEIGHT) // 2

# Game area size in tiles
GAME_WIDTH_TILES = GAME_WIDTH // SPRITE_SIZE
GAME_HEIGHT_TILES = GAME_HEIGHT // SPRITE_SIZE

# The number of pixels by which a ninja can intersect a one-way platform,
# while still being moved back to the top of the platform during collision resolution
ONE_WAY_PLATFORM_TOLERANCE = 2

# Sprite data, including indices to use for rendering
class Sprites:
    # Offset of the red ninja from the blue ninja
    RED_OFFSET = 4

    # We'll only be using PLAYER_IDLE for now
    PLAYER_IDLE = 32
    PLAYER_CLIMBING_IDLE = 33
    PLAYER_CLIMBING_1 = 34
    PLAYER_CLIMBING_2 = 35
    PLAYER_WALKING_1 = 40
    PLAYER_WALKING_2 = 41
    PLAYER_JUMPING_UP = 42
    PLAYER_JUMPING_DOWN = 43

    LADDER = 11

    COIN = 19
    GEM = 18

    WATER = 30

    # A blank tile is represented by 0xff in the level arrays
    BLANK_TILE = 0xff
    
# Generic ninja data such as size
class Ninja:
    # The visible width of the ninja sprite
    WIDTH = 4

    # The gap between the edge of the sprite and the edge of the ninja on each side
    BORDER = (SPRITE_SIZE - WIDTH) // 2

# Player data such as speeds
class Player:
    # Speeds are measured in pixels per second
    MAX_SPEED = 50

    JUMP_SPEED = 125
    DEATH_JUMP_SPEED = 100
    CELEBRATION_JUMP_SPEED = 75
    
    CELEBRATION_JUMP_COUNT = 3

    CLIMBING_SPEED = 40

# Enemy data
class Enemy:
    MAX_SPEED = 20
    MIN_SPEED = 10

    CLIMBING_SPEED = 20

    # Hitbox width for detecting the edge of a platform
    PLATFORM_DETECTION_WIDTH = 6

    # Chance of climbing next ladder
    CLIMB_NEXT_LADDER_CHANCE = 0.2

# Data for "Collectables" (gems and coins), such as value of each
class Collectable:
    # The coin and gem sprites are smaller in size
    SIZE = 4
    # Calculate the gap between the edge of the sprite and the edge of the actual coin/gem
    BORDER = (SPRITE_SIZE - SIZE) // 2

    # Point value of each
    COIN_SCORE = 2
    GEM_SCORE = 5

# Environment data such as gravity strength
class Environment:
    GRAVITY_ACCELERATION = 375

# Level data
class LevelData:
    def __init__(self, platforms, extras, entity_spawns, pipes):
        # Platform data
        self.platforms = platforms

        # Coin, gem, and ladder data
        self.extras = extras

        # Entity spawn data
        self.entity_spawns = entity_spawns

        # Background pipe data
        self.pipes = pipes

    def copy(self):
        return LevelData(self.platforms.copy(), self.extras.copy(), self.entity_spawns.copy(), self.pipes.copy())

# Number of levels
LEVEL_COUNT = 3

LEVELS = [
    # Level 1
    LevelData(
        # Platform data
        [
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0x03, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x03, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x01, 0x02, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0x01, 0x01, 0x01, 0x02, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x01, 0x01, 0x01,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0x01, 0x01, 0x01, 0x02, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x01, 0x01, 0x01,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x01, 0x02, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff
        ],
        
        # Coin, gem and ladder data
        [
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0x12, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x12, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x13, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0x13, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x13, 0xff,
            0xff, 0x0b, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0b, 0xff,
            0xff, 0x0b, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0b, 0xff,
            0xff, 0x0b, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0b, 0xff,
            0xff, 0x0b, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0b, 0xff,
            0xff, 0x0b, 0xff, 0xff, 0xff, 0xff, 0xff, 0x13, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0b, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff
        ],

        # Entity spawn data
        [
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x24, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0x24, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x24, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x20, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff
        ],

        # Background pipe data
        [
            0xff, 0xff, 0xff, 0xff, 0x0c, 0xff, 0xff, 0xff, 0x1c, 0x16, 0x17, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0x0d, 0xff, 0xff, 0xff, 0x0c, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0x05, 0x16, 0x16, 0x16, 0x17, 0xff, 0xff, 0xff, 0x0c, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0x0c, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0c, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0x0c, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0c, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0x0c, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0c, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0x17, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0c, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x14, 0x05, 0x16, 0x16, 0x16, 0x16, 0x16,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0c, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0c, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0x11, 0x05, 0x06, 0x16, 0x17, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0x19, 0x0c, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0x06, 0x07, 0xff, 0xff, 0xff, 0x19, 0x0c, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0x0c, 0xff, 0xff, 0xff, 0x19, 0x0c, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff
        ]
    ),

    # Level 2
    LevelData(
        # Platform data
        [
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0x01, 0x02, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x01,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x01, 0x02, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0x00, 0x01, 0x02, 0xff, 0xff, 0xff, 0x00, 0x01, 0x02, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0x01, 0x01, 0x02, 0xff, 0xff, 0xff, 0x00, 0x01, 0x02, 0xff, 0xff, 0xff, 0x00, 0x01, 0x01
        ],

        # Coin, gem and ladder data
        [
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x13, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0x12, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x12,
            0x0b, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0b,
            0x0b, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0b, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0b,
            0x0b, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0b, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0b,
            0x0b, 0xff, 0xff, 0xff, 0x13, 0xff, 0xff, 0x0b, 0xff, 0xff, 0x13, 0xff, 0xff, 0xff, 0x0b,
            0x0b, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0b, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0b,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0b, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0b, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0b, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0b, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0x13, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0b, 0xff, 0xff, 0xff, 0xff, 0xff, 0x13, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0b, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0b, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff
        ],

        # Entity spawn data
        [
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x24, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0x24, 0xff, 0xff, 0xff, 0xff, 0xff, 0x24, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0x24, 0xff, 0xff, 0xff, 0xff, 0xff, 0x20, 0xff, 0xff, 0xff, 0xff, 0xff, 0x24, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff
        ],

        # Background pipe data
        [
            0xff, 0xff, 0xff, 0xff, 0x0c, 0xff, 0xff, 0xff, 0x14, 0x16, 0x1d, 0xff, 0xff, 0x0c, 0xff,
            0xff, 0xff, 0xff, 0xff, 0x0c, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0c, 0xff, 0xff, 0x0c, 0xff,
            0xff, 0xff, 0xff, 0xff, 0x0c, 0xff, 0xff, 0xff, 0xff, 0xff, 0x14, 0x06, 0x16, 0x1d, 0xff,
            0xff, 0xff, 0xff, 0xff, 0x0f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0c, 0xff,
            0x16, 0x16, 0x16, 0x05, 0x17, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0f, 0xff,
            0xff, 0xff, 0xff, 0x0c, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x14, 0x16,
            0xff, 0xff, 0xff, 0x0c, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0x0c, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0x0c, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0x0d, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0x04, 0x16, 0x16, 0x15, 0x10, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0x0c, 0xff, 0xff, 0xff, 0x18, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0x0c, 0xff, 0xff, 0xff, 0x18, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x11, 0x06, 0x07, 0xff,
            0x1c, 0x16, 0x06, 0x07, 0x18, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x19, 0xff, 0x1c, 0x16,
            0x0c, 0xff, 0xff, 0x0c, 0x18, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x19, 0xff, 0x0c, 0xff
        ]
    ),
    
    # Level 3
    LevelData(
        # Platform data
        [
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0x00, 0x01, 0x02, 0xff, 0xff, 0xff, 0x00, 0x01, 0x02, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0x02, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00,
            0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x01, 0x01, 0x01, 0x02, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0x01, 0x01, 0x02, 0xff, 0xff, 0xff, 0x00, 0x01, 0x02, 0xff, 0xff, 0xff, 0x00, 0x01, 0x01,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff
        ],

        # Coin, gem and ladder data
        [
            0xff, 0xff, 0xff, 0xff, 0x13, 0xff, 0xff, 0xff, 0xff, 0xff, 0x13, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0x0b, 0xff, 0xff, 0xff, 0x0b, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0x0b, 0xff, 0xff, 0xff, 0x0b, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0x0b, 0xff, 0x13, 0xff, 0x0b, 0xff, 0xff, 0xff, 0xff, 0xff,
            0x12, 0xff, 0xff, 0xff, 0xff, 0x0b, 0xff, 0xff, 0xff, 0x0b, 0xff, 0xff, 0xff, 0xff, 0x12,
            0xff, 0xff, 0xff, 0xff, 0xff, 0x0b, 0xff, 0xff, 0xff, 0x0b, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0x0b, 0xff, 0x0b, 0xff, 0x0b, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0b, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0b, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0x13, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x13, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff
        ],

        # Entity spawn data
        [
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0x24, 0xff, 0xff, 0xff, 0xff, 0xff, 0x24, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x24, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0x24, 0xff, 0xff, 0xff, 0xff, 0xff, 0x20, 0xff, 0xff, 0xff, 0xff, 0xff, 0x24, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff
        ],

        # Background pipe data
        [
            0xff, 0x0c, 0xff, 0xff, 0xff, 0xff, 0x0c, 0xff, 0xff, 0xff, 0xff, 0x0c, 0xff, 0x0c, 0xff,
            0xff, 0x0c, 0xff, 0xff, 0xff, 0xff, 0x0f, 0xff, 0xff, 0xff, 0xff, 0x14, 0x06, 0x1d, 0xff,
            0xff, 0x14, 0x07, 0xff, 0xff, 0xff, 0x0c, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x14, 0x16,
            0xff, 0xff, 0x1c, 0x16, 0x16, 0x16, 0x17, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0x0c, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0x0c, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0x05, 0x16, 0x0e, 0x06, 0x10, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
            0x0c, 0xff, 0x0c, 0xff, 0x18, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x04, 0x16, 0x16,
            0x14, 0x16, 0x1d, 0xff, 0x18, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0f, 0xff, 0xff,
            0xff, 0xff, 0x0c, 0xff, 0x18, 0xff, 0xff, 0xff, 0xff, 0xff, 0x04, 0x16, 0x15, 0x16, 0x16,
            0xff, 0xff, 0x0c, 0xff, 0x18, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0c, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0x0c, 0xff, 0x18, 0xff, 0xff, 0xff, 0x11, 0x06, 0x1d, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0x0f, 0xff, 0x18, 0xff, 0xff, 0xff, 0x19, 0xff, 0x0c, 0xff, 0xff, 0xff, 0xff,
            0x16, 0x16, 0x15, 0x07, 0x18, 0xff, 0xff, 0xff, 0x19, 0xff, 0x0c, 0xff, 0xff, 0xff, 0xff,
            0xff, 0xff, 0xff, 0x0c, 0x18, 0xff, 0xff, 0xff, 0x19, 0xff, 0x0c, 0xff, 0xff, 0xff, 0xff
        ]
    )
]