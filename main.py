import pyxel as px

px.init(90, 90, title="Tamagochi")

import variables as v
from pet_actions import pet_action_main
from inputs import button_main
from display import display_draw_main


# with open(saveName,"w") as saveFile:


def update():
	button_main()
	pet_action_main()


def draw():
	px.cls(15)
	display_draw_main()


px.run(update, draw)

if __name__ == '__main__':
	pass
