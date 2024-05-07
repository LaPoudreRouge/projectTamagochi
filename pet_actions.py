import variables as v
from random import randint


def check_status():
	"""
	check if any pet variable got to 0 or less
	"""
	for pet in v.pets:
		if pet["health"] <= 0 or pet["exhaustion"] <= 0:
			v.game_over = True
		if pet["boredom"] <= 0:
			pet["bored"] = True
		else:
			pet["bored"] = False


def status_update():
	"""
	update the status of every pet depending on their state
	"""
	any_pet_bored = False
	for pet in v.pets:
		if pet["bored"]:
			any_pet_bored = True
	for pet in v.pets:
		if pet["sleeping"]:  # Sleeping
			if pet["health"] < 200:
				pet["health"] += 1
			if pet["boredom"] < 200:
				pet["boredom"] += 1
			if pet["exhaustion"] < 200:
				pet["exhaustion"] += 1

		else:  # Awake
			if pet["hunger"] > 0:
				pet["hunger"] -= 5
			else:
				pet["health"] -= 5
			if pet["boredom"] > 0:
				pet["boredom"] -= 3
			if any_pet_bored:
				pet["health"] -= 5


def day_night_cycle():
	if v.day_night_timer <= 0:
		if v.day_state:
			for pet in v.pets:
				pet["sleeping"] = True
			v.night_time = randint(30, 60)
			v.day_night_timer = v.night_time
			v.day_state = False
		else:
			for pet in v.pets:
				pet["sleeping"] = False
			v.day_night_timer = v.day_time
			v.cookie_count = 50
			v.day_state = True
	v.day_night_timer -= 1


def status_update_timer():
	"""
	modify the pets variables every second
	"""
	v.sec_countdown -= 1
	if v.sec_countdown <= 0:
		v.sec_countdown = v.sec
		status_update()
		day_night_cycle()


def pet_feed():
	"""
	feed the pet
	add +50 to his hunger
	"""
	if v.day_state:
		if v.cookie_count > 0:
			v.pets[v.current_pet]["hunger"] = min(v.pets[v.current_pet]["hunger"] + 50, 200)
			v.cookie_count -= 1
		else:
			print("no more cookies")
	else:
		print("pet sleeping")


def pet_play():
	"""
	play with the pet
	add 50 to his boredom
	"""
	if v.day_state:
		v.pets[v.current_pet]["boredom"] = min(v.pets[v.current_pet]["boredom"] + 50, 200)
		v.pets[v.current_pet]["exhaustion"] = max(v.pets[v.current_pet]["exhaustion"] - 50, 0)
	else:
		print("pet sleeping")


def pet_action_main():
	if v.game_state["game running"]:
		status_update_timer()
		check_status()
