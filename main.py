# To update requirements.txt, run:
#   rm requirements.txt ; pigar generate --enable-feature requirement-annotations
import cv2 # pigar: required-imports=opencv-python
import numpy as np # pigar: required-imports=numpy
import PIL.ImageGrab
from pynput import keyboard
import sys

pressed = set()

shortcut = [{keyboard.Key.cmd, keyboard.Key.f12}]

def process(sshot):
    template = cv2.imread("images/natural-resources-header.png")
    result = cv2.matchTemplate(sshot, template, cv2.TM_CCOEFF_NORMED)
    print("Found at:" + str(np.unravel_index(result.argmax(), result.shape)))

def on_press(key):
    pressed.add(key)
    #print(pressed)
    for keys in shortcut:
        if keys.issubset(pressed):
            process(PIL.ImageGrab.grab())

def on_release(key):
    if key in pressed:
        pressed.remove(key)

if len(sys.argv) > 1:
    # Use given screenshot file for testing:
    process(cv2.imread(sys.argv[1]))
else:
    # Listen for shortcut and take screenshot:
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()