import pyxel as px
import variables as v
from pet_actions import pet_feed, pet_play,pet_reset
import load_save as ls

button_pressed = {"g": False, "h": False, "f": False, "j": False, "sp": False, "l": False, "p": False, "s": False, "q": False}


def feed_button():
	global button_pressed
	if px.btn(px.KEY_G):
		if not (button_pressed["g"]):
			button_pressed["g"] = True
			pet_feed()
	else:
		button_pressed["g"] = False


def play_button():
	global button_pressed
	if px.btn(px.KEY_H):
		if not (button_pressed["h"]):
			button_pressed["h"] = True
			pet_play()
	else:
		button_pressed["h"] = False


def left_pet():
	global button_pressed
	if px.btn(px.KEY_F):
		if not (button_pressed["f"]):
			button_pressed["f"] = True
			v.current_pet -= 1
			if v.current_pet < 0:
				v.current_pet = 4
	else:
		button_pressed["f"] = False


def right_pet():
	global button_pressed
	if px.btn(px.KEY_J):
		if not (button_pressed["j"]):
			button_pressed["j"] = True
			v.current_pet += 1
			if v.current_pet > 4:
				v.current_pet = 0
	else:
		button_pressed["j"] = False


def game_quit():
	global button_pressed
	if px.btn(px.KEY_Q):
		if not (button_pressed["q"]):
			button_pressed["q"] = True
			px.quit()
	else:
		button_pressed["q"] = False


def pause_game():
	global button_pressed
	if px.btn(px.KEY_P):
		if not (button_pressed["p"]):
			button_pressed["p"] = True
			v.game_state_change("paused")
	else:
		button_pressed["p"] = False


def game_over():
	global button_pressed
	if px.btn(px.KEY_SPACE):  # launch game
		if not (button_pressed["sp"]):
			button_pressed["sp"] = True
			print("space")
			v.game_state_change("main menu")
	else:
		button_pressed["sp"] = False

	game_quit()


def main_menu():
	global button_pressed
	if px.btn(px.KEY_SPACE):  # launch game
		if not (button_pressed["sp"]):
			button_pressed["sp"] = True
			if v.load:
				ls.load()
			else:
				pet_reset()
			v.game_state_change("game running")
	else:
		button_pressed["sp"] = False

	if px.btn(px.KEY_L):  # load save toggle
		if not (button_pressed["l"]):
			button_pressed["l"] = True
			if v.load:
				v.load = False
			else:
				v.load = True
	else:
		button_pressed["l"] = False


def pause_menu():
	global button_pressed
	if px.btn(px.KEY_P):
		if not (button_pressed["p"]):
			button_pressed["p"] = True
			v.game_state_change("game running")
	else:
		button_pressed["p"] = False
	if px.btn(px.KEY_S):
		if not (button_pressed["s"]):
			button_pressed["s"] = True
			ls.save()
	else:
		button_pressed["s"] = False

	game_quit()


def button_main():
	if v.game_state["game running"]:
		play_button()
		feed_button()
		left_pet()
		right_pet()
		pause_game()
	elif v.game_state["main menu"]:
		main_menu()
	elif v.game_state["paused"]:
		pause_menu()
	elif v.game_state["game over"]:
		game_over()
