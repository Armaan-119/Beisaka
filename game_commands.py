# game_commands.py

import pyautogui
import time

def execute_skyrim_command(query):
    query = query.lower()

    if "attack" in query:
        for _ in range(5):
            pyautogui.mouseDown(button='left')
            time.sleep(0.1)
            pyautogui.mouseUp(button='left')

    elif "block" in query:
        pyautogui.mouseDown(button='right')
        time.sleep(1)
        pyautogui.mouseUp(button='right')

    elif "sprint" in query:
        pyautogui.keyDown("shift")
        pyautogui.keyDown("w")
        time.sleep(2)
        pyautogui.keyUp("w")
        pyautogui.keyUp("shift")

    elif "shout" in query:
        pyautogui.press("z")

    elif "draw weapon" in query:
        pyautogui.press("r")

    elif "sneak" in query:
        pyautogui.press("ctrl")

    elif "open map" in query:
        pyautogui.press("m")

    elif "quick save" in query:
        pyautogui.press("f5")

    else:
        print("Unrecognized Skyrim command.")
