sec = 30  # a second

sec_countdown = sec

# pet dict
pets = [
	{"hunger": 200, "health": 200, "boredom": 200, "exhaustion": 200, "sleeping": False, "bored": False},
	{"hunger": 200, "health": 200, "boredom": 200, "exhaustion": 200, "sleeping": False, "bored": False},
	{"hunger": 200, "health": 200, "boredom": 200, "exhaustion": 200, "sleeping": False, "bored": False},
	{"hunger": 200, "health": 200, "boredom": 200, "exhaustion": 200, "sleeping": False, "bored": False},
	{"hunger": 200, "health": 200, "boredom": 200, "exhaustion": 200, "sleeping": False, "bored": False},
]

current_pet = 0  # 0 to 4. show which pet you are on (important for displays and feed and play...)

# status of the game
game_state = {"main menu": True, "game running": False, "paused": False, "game over": False}


def game_state_change(target_state):
	for state in game_state.items():
		game_state[state[0]] = False
	game_state[target_state] = True


load = False

day_time = 180  # sec  3min

night_time = 0

day_state = True  # true is day and false is night

day_night_timer = day_time

cookie_count = 50

sprite_pos = [(0, 0), (32, 0), (0, 32), (32, 32), (0, 64)]

day_anim = [(0, 128), (16, 128), (32, 128), (48, 128), (0, 144), (16, 144), (32, 144), (48, 144)]
night_anim = [(0, 96), (16, 96), (32, 96), (48, 96), (0, 112), (16, 112), (32, 112), (48, 112)]

survival_time = 0


def survival_time_separator(time):
	return time // 3600, (time % 3600) // 60, time % 60  # (h, min, sec)
