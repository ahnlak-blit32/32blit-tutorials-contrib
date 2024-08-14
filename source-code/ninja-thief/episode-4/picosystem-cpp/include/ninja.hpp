#pragma once

#include <cmath>

#include "picosystem.hpp"

#include "constants.hpp"

class Ninja {
public:
    enum class Colour {
        BLUE = 0,
        RED = 1
    };

    Ninja();
    Ninja(Colour _colour, float x, float y);

    void update(float dt, Constants::LevelData& level_data);
    void render();

    bool check_colliding(float object_x, float object_y, uint8_t object_size);

protected:
    void jump(float jump_speed);

    Colour colour;

    float position_x = 0.0f;
    float position_y = 0.0f;
    float velocity_x = 0.0f;
    float velocity_y = 0.0f;

    enum class HorizontalDirection {
        LEFT = -1,
        RIGHT = 1
    };

	enum class VerticalDirection {
		UP = -1,
		DOWN = 1
	};

    HorizontalDirection facing_direction = HorizontalDirection::RIGHT;

    bool can_jump = false;
    bool can_climb = false;
    
    enum class ClimbingState {
        NONE,
        IDLE,
        UP,
        DOWN
    };

    ClimbingState climbing_state = ClimbingState::NONE;

private:
    void handle_collisions(Constants::LevelData& level_data);
    void handle_platform(Constants::LevelData& level_data, uint8_t x, uint8_t y);
    void handle_ladder(Constants::LevelData& level_data, uint8_t x, uint8_t y);
};