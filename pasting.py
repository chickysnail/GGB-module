from pynput.mouse import Listener, Button
import time
import keyboard
from threading import Thread

previous_left = 0

def on_click(x, y, button, pressed):
    global previous_left
    # double click left button
    if pressed and button == Button.left:
        previous_left = time.time()

    if pressed and button == Button.right:
        current_right = time.time()

        diff = current_right-previous_left

        if diff < 0.4:
            # print('double click')
            keyboard.press_and_release("ctrl+v, enter")
            # keyboard.press_and_release('esc')
            # print("pasted")

def background_listener():
    with Listener(on_click=on_click) as listener:
        listener.join()

def main():
    daemon = Thread(target=background_listener, daemon=True, name='Monitor')
    daemon.start()


if __name__=="__main__":
    main()