# To update requirements.txt, run:
#   pipreqs --ignore .venv --encoding=utf-8 --force .
from pynput import keyboard
import PIL.ImageGrab

pressed = set()

shortcut = [{keyboard.Key.cmd, keyboard.Key.f12}]

def activate():
    im = PIL.ImageGrab.grab()
    im.show()

def on_press(key):
    pressed.add(key)
    #print(pressed)
    for keys in shortcut:
        if keys.issubset(pressed):
            activate()

def on_release(key):
    if key in pressed:
        pressed.remove(key)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()