#pragma once

#include <string>

#include "32blit.hpp"

#include "player_ninja.hpp"
#include "constants.hpp"

class Level {
public:
	Level();
	Level(uint8_t _level_number);

	void update(float dt);
	void render();

private:
	void render_border();

	Constants::LevelData level_data = {};
	uint8_t level_number = 0;

	PlayerNinja player;
};