import pyxel as px
import variables as v

px.load("textures.pyxres")

clear = lambda: print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
pet_change = v.current_pet


def display_main():
	global pet_change
	if v.sec_countdown == 30:
		clear()
		print(v.current_pet, v.pets[v.current_pet], v.day_night_timer, v.cookie_count)
	elif pet_change != v.current_pet:
		clear()
		print(v.current_pet, v.pets[v.current_pet], v.day_night_timer, v.cookie_count)
		pet_change = v.current_pet


def pets_stats_bars_(x, y):
	px.rect(1, 1, 65, 27, 0)
	px.rect(2, 2, 63, 25, 7)

	px.rect(x + 14, y + 3, 50, 5, 13)
	px.rect(x + 14, y + 9, 50, 5, 13)
	px.rect(x + 14, y + 15, 50, 5, 13)
	px.rect(x + 14, y + 21, 50, 5, 13)

	px.rect(x + 14, y + 3, v.pets[v.current_pet]["hunger"] // 4, 5, 1)
	px.rect(x + 14, y + 9, v.pets[v.current_pet]["health"] // 4, 5, 2)
	px.rect(x + 14, y + 15, v.pets[v.current_pet]["boredom"] // 4, 5, 3)
	px.rect(x + 14, y + 21, v.pets[v.current_pet]["exhaustion"] // 4, 5, 4)

	px.text(x + 3, y + 3, "HU:", 0)
	px.text(x + 3, y + 9, "HP:", 0)
	px.text(x + 3, y + 15, "BO:", 0)
	px.text(x + 3, y + 21, "EX:", 0)


def draw_pet():
	a, b = v.sprite_pos[v.current_pet]
	px.blt(29, 40, 0, a, b, 32, 32)


def draw_clock_anim():
	if v.day_state:
		a, b = v.day_anim[7 - int(v.day_night_timer // (v.day_time / 8))]
	else:
		a, b = v.night_anim[7 - int(v.day_night_timer // (v.night_time / 8))]
	px.blt(70, 3, 0, a, b, 16, 16)

def draw_commands():
	px.blt(53, 67, 0, 64, 96, 35, 21)  # feed, play, pause
	px.blt(2, 52, 0, 64, 124, 16, 7)  # <- f
	px.blt(70, 52, 0, 80, 124, 16, 7)  # h ->


def draw_pause():
	# write "game paused"
	# write actions p = play, s = save data
	px.blt(19, 29, 0, 24, 176, 52, 9)  # game paused
	px.blt(31, 40, 0, 24, 187, 28, 9)  # p = play
	px.blt(30, 51, 0, 0, 160, 30, 9)  # s = save

def draw_game_over():
	px.rect(25, 40, 40, 9, 0)
	px.rect(26, 41, 38, 7, 7)
	px.text(27, 42, "GAME OVER", 0)


def draw_cookies():
	px.blt(1, 74, 0, 32, 64, 16, 16)
	px.text(17, 80, ":" + str(v.cookie_count), 0)


def draw_main_menu():
	px.blt(23, 20, 0, 32, 81, 44, 9)  # title
	px.blt(32, 30, 0, 67, 1, 26, 23)  # house
	px.blt(18, 58, 0, 53, 187, 54, 9)  # space to play
	if v.load:
		px.blt(30, 70, 0, 80, 160, 30, 9)  # load green
	else:
		px.blt(30, 70, 0, 116, 160, 30, 9)  # load red
	pass


def display_draw_main():
	if v.game_state["game running"] or v.game_state["paused"]:
		draw_clock_anim()
		draw_cookies()
		pets_stats_bars_(0, 0)
		draw_pet()
		draw_commands()
		if v.game_state["paused"]:
			draw_pause()
	elif v.game_state["main menu"]:
		draw_main_menu()
	elif v.game_state["game over"]:
		draw_game_over()
