from pynput import mouse, keyboard
from print import notice
import time


move_count = 0


def on_move(x, y):
    global move_count
    move_count += 1


def on_click(x, y, button, pressed):
    global move_count
    move_count += 1



def on_scroll(x, y, dx, dy):
    global move_count
    move_count += 1


def on_press(key):
    try:
        global move_count
        move_count += 1


    except AttributeError:
        move_count += 1

mouse_listener = mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll)


keyboard_listener = keyboard.Listener(
        on_press=on_press)


def function():
    use_time = 0
    global move_count
    mouse_listener.start()
    keyboard_listener.start()
    while use_time <3600:
        time.sleep(10)
        if move_count > 0:
            use_time += 10
            move_count = 0
            print(use_time)
        if use_time >= 1800 and use_time < 1810:
            notice(30)
    notice(60)
    return 0

if __name__ == '__main__':
    function()

