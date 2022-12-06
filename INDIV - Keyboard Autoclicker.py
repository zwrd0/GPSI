#---- Imports ----#
import time
import keyboard
from pynput.keyboard import Key, Listener

#---- Main ----#
def clickAuto(letra, tempo):
	letra = str(letra)
	keyboard.press_and_release(letra)
	time.sleep(tempo)
			
def show(key):
		if key == Key.f6:
			while True:
				clickAuto("e", 0.2)

while True:
    with Listener(on_press= show) as listener:
        listener.join()
