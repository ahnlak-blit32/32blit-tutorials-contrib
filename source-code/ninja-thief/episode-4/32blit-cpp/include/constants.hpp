#pragma once

#include <cstdint>

namespace Constants {
    // Screen size in pixels
    const uint8_t SCREEN_WIDTH = 160;
    const uint8_t SCREEN_HEIGHT = 120;

    // Actual game area in pixels
    const uint8_t GAME_WIDTH = 120;
    const uint8_t GAME_HEIGHT = 120;

    // Each sprite on the spritesheet is 8x8 pixels
    const uint8_t SPRITE_SIZE = 8;

    // Offset of game area from top left corner
    const float GAME_OFFSET_X = (SCREEN_WIDTH - GAME_WIDTH) / 2;
    const float GAME_OFFSET_Y = (SCREEN_HEIGHT - GAME_HEIGHT) / 2;

    // Game area size in tiles
    const uint8_t GAME_WIDTH_TILES = GAME_WIDTH / SPRITE_SIZE;
    const uint8_t GAME_HEIGHT_TILES = GAME_HEIGHT / SPRITE_SIZE;

    // The number of pixels by which a ninja can intersect a one-way platform,
    // while still being moved back to the top of the platform during collision resolution
    const uint8_t ONE_WAY_PLATFORM_TOLERANCE = 2;

    // Sprite data, including indices to use for rendering
    namespace Sprites {
        // Offset of the red ninja sprites from the blue ninja sprites
        const uint8_t RED_OFFSET = 4;

        // We'll only be using PLAYER_IDLE for now
        const uint8_t PLAYER_IDLE = 32;
        const uint8_t PLAYER_CLIMBING_IDLE = 33;
        const uint8_t PLAYER_CLIMBING_1 = 34;
        const uint8_t PLAYER_CLIMBING_2 = 35;
        const uint8_t PLAYER_WALKING_1 = 40;
        const uint8_t PLAYER_WALKING_2 = 41;
        const uint8_t PLAYER_JUMPING_UP = 42;
        const uint8_t PLAYER_JUMPING_DOWN = 43;

        const uint8_t LADDER = 11;

        const uint8_t COIN = 19;
        const uint8_t GEM = 18;

        // These will be used to draw a border either side of the screen, to make the game area 120x120
        const uint8_t BORDER_LEFT = 10;
        const uint8_t BORDER_FULL = 9;
        const uint8_t BORDER_RIGHT = 8;

        // A blank tile is represented by 0xff in the level arrays
        const uint8_t BLANK_TILE = 0xff;
    }

    // Generic ninja data such as size
    namespace Ninja {
        // The visible width of the ninja sprite
        const uint8_t WIDTH = 4;

        // The gap between the edge of the sprite and the edge of the ninja on each side
        const uint8_t BORDER = (SPRITE_SIZE - WIDTH) / 2;
    }

    // Player data such as speeds
    namespace Player {
        // Speeds are measured in pixels per second
        const float MAX_SPEED = 50.0f;

        const float JUMP_SPEED = 125.0f;

        const float CLIMBING_SPEED = 40.0f;
    }

    // Enemy constants
    namespace Enemy {
        const float MAX_SPEED = 15.0f;

        const float CLIMBING_SPEED = 20.0f;

        // Hitbox width for detecting the edge of a platform
        const uint8_t PLATFORM_DETECTION_WIDTH = 6;

        // Chance of climbing next ladder
        const float CLIMB_NEXT_LADDER_CHANCE = 0.2f;
    }

    // Environment data such as gravity strength
    namespace Environment {
        const float GRAVITY_ACCELERATION = 375.0f;
    }

    // Level data
    struct LevelData {
        // Platform data
        uint8_t platforms[GAME_WIDTH_TILES * GAME_HEIGHT_TILES];

        // Coin, gem, and ladder data
        uint8_t extras[GAME_WIDTH_TILES * GAME_HEIGHT_TILES];

        // Entity spawn data
        uint8_t entity_spawns[GAME_WIDTH_TILES * GAME_HEIGHT_TILES];
    };

    // Number of levels
    const uint8_t LEVEL_COUNT = 1;

    const LevelData LEVELS[LEVEL_COUNT] = {
        // Level 1
        {
            // Platform data
            {
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
            },

            // Coin, gem and ladder data
            {
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
            },
            
            // Entity spawn data
            {
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
            }
        }
    };
}