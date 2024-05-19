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
	if v.day_state:
		a, b = v.sprite_pos_day[v.current_pet]
	else:
		a, b = v.sprite_pos_night[v.current_pet]
	px.blt(29, 40, 0, a, b, 32, 32)


def draw_clock_anim():
	if v.day_state:
		a, b = v.day_anim[7 - int(v.day_night_timer // (v.day_time / 8))]
	else:
		a, b = v.night_anim[7 - int(v.day_night_timer // (v.night_time / 8))]
	px.blt(70, 3, 0, a, b, 16, 16)

def draw_commands():
	px.blt(53, 67, 0, 64, 96, 35, 21)  # feed, play, pause
	if v.day_state:
		px.blt(2, 52, 0, 64, 124, 16, 7)  # <- f
		px.blt(72, 52, 0, 80, 124, 16, 7)  # h ->
	else:
		px.blt(2, 52, 0, 64, 132, 16, 7)  # <- f
		px.blt(72, 52, 0, 80, 132, 16, 7)  # h ->


def draw_pause():
	px.rect(14, 16, 62, 61, 0)
	px.rect(15, 17, 60, 59, 12)
	px.blt(19, 19, 0, 24, 176, 52, 9)  # game paused
	px.blt(31, 30, 0, 24, 187, 28, 9)  # p = play
	if v.save:
		px.blt(30, 41, 0, 32, 160, 30, 9)  # s = save
	else:
		px.blt(30, 41, 0, 0, 160, 30, 9)
	px.blt(28, 52, 0, 24, 199, 34, 9)  # q : quit
	px.blt(16, 63, 0, 80, 178, 58, 9)

def draw_game_over():
	px.cls(15)
	px.blt(24, 4, 0, 58, 199, 42, 9)  # game over
	px.blt(16, 50, 0, 80, 178, 58, 9)  # space to menu
	px.blt(28, 61, 0, 24, 199, 34, 9)  # q quit
	px.rect(2, 16, 86, 32, 0)
	px.rect(3, 17, 84, 30, 9)
	px.blt(4, 19, 0, 64, 147, 67, 5)
	px.text(0, 26, f" {v.survival_time_separator(v.survival_time)[0]} hours",0)
	px.text(0, 33, f" {v.survival_time_separator(v.survival_time)[1]} minutes",0)
	px.text(0, 40, f" {v.survival_time_separator(v.survival_time)[2]} seconds",0)
	px.blt(1, 68, 0, 67,36, 26, 20)  # dead one
	px.blt(63, 68, 0, 67, 36, 26, 20)  # dead one
	px.blt(6, 2, 0, 66, 56, 12, 12)  # flower
	px.blt(72, 2, 0, 66, 56, 12, 12)  # flower
	px.blt(34, 71, 0, 133, 68, 22, 17)

def draw_cookies():
	if v.day_state:
		px.blt(1, 74, 0, 32, 64, 16, 16)
	else:
		px.blt(1, 74, 0, 48, 64, 16, 16)
	px.text(17, 80, ":" + str(v.cookie_count), 0)


def draw_main_menu():
	px.blt(21, 10, 0, 32, 81, 48, 9)  # title
	px.blt(32, 20, 0, 65, 0, 30, 27)  # house
	px.blt(18, 49, 0, 53, 187, 54, 9)  # space to play
	px.blt(28, 71, 0, 24, 199, 34, 9)  # q : quit
	if v.load:
		px.blt(30, 60, 0, 80, 160, 30, 9)  # load green
	else:
		px.blt(30, 60, 0, 116, 160, 30, 9)  # load red
	pass


def display_draw_main():
	if v.game_state["game running"] or v.game_state["paused"]:
		if v.day_state:
			px.cls(15)
		else:
			px.cls(1)
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
