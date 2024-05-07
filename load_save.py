import variables as v

# game_data.txt
# line 0 -> info pet 1.
# line 1 -> info pet 2.
# line 2 -> info pet 3.
# line 3 -> info pet 4.
# line 4 -> info pet 5.
# line 5 -> info state of the day (Day/Night).
# line 6 -> info time.
# line 7 -> info number of cookies.

if v.load:
	try:
		info = open('game_data.txt', 'r+')
	except FileNotFoundError:
		open('game_data.txt', 'w')
		info = open('game_data.text', 'r+')
	content = info.read()
	if len(content) != 0:
		list = content.split("\n")
		for i in range(len(list)):
			temp = list[i].split(" ")
			list[i] = temp
		# list to be transformed into a dictionary
		# utiliser boucle for
		# une boucle pour faire cylce des 5 animaux
		# la boucle contient un pointeur*

		v.pets = [
			{"hunger": int(list[0][0]), "health": int(list[0][1]), "boredom": int(list[0][2]),
			 "exhaustion": int(list[0][3]), "sleeping": bool(list[0][4]), "bored": bool(list[0][5])},
			{"hunger": int(list[1][0]), "health": int(list[1][1]), "boredom": int(list[1][2]),
			 "exhaustion": int(list[1][3]), "sleeping": bool(list[1][4]), "bored": bool(list[1][5])},
			{"hunger": int(list[2][0]), "health": int(list[2][1]), "boredom": int(list[2][2]),
			 "exhaustion": int(list[2][3]), "sleeping": bool(list[2][4]), "bored": bool(list[2][5])},
			{"hunger": int(list[3][0]), "health": int(list[3][1]), "boredom": int(list[3][2]),
			 "exhaustion": int(list[3][3]), "sleeping": bool(list[3][4]), "bored": bool(list[3][5])},
			{"hunger": int(list[4][0]), "health": int(list[4][1]), "boredom": int(list[4][2]),
			 "exhaustion": int(list[4][3]), "sleeping": bool(list[4][4]), "bored": bool(list[4][5])}
		]
		v.day_state = bool(list[5])
		v.day_night_timer = int(list[6][0])
		v.cookie_count = int(list[7][0])


# print(v.pets)
# print(v.day_state)
# print(v.day_night_timer)
# print(v.cookie_count)

def save():
	text_saved = ""
	sub = []
	for i in range(len(v.pets)):
		for key in v.pets[i]:
			sub.append(v.pets[i][key])
	text = ""
	place = 0
	for i in range(5):
		for j in range(6):
			text += str(sub[j + place]) + " "
		text += '\n'
		place += 6
	text = text.rstrip(text[-1])
	text_saved = text
	text_saved += "\n" + str(v.day_state) + "\n" + str(v.day_night_timer) + "\n" + str(v.cookie_count)
	file = open("game_data.txt", "r+")
	file.truncate(0)
	file.write(text_saved)
	file.close()

