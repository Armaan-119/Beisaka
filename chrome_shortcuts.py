# chrome_shortcuts.py
import pyautogui
import webbrowser
from time import sleep

def handle_chrome_commands(query, speak):
    if "open new tab" in query:
        pyautogui.hotkey("ctrl", "t")
        speak("Opened a new tab.")

    elif "close tab" in query:
        pyautogui.hotkey("ctrl", "w")
        speak("Closed the current tab.")

    elif "reopen closed tab" in query:
        pyautogui.hotkey("ctrl", "shift", "t")
        speak("Reopened the last closed tab.")

    elif "next tab" in query:
        pyautogui.hotkey("ctrl", "tab")
        speak("Switched to the next tab.")

    elif "previous tab" in query:
        pyautogui.hotkey("ctrl", "shift", "tab")
        speak("Switched to the previous tab.")

    elif "open downloads" in query:
        pyautogui.hotkey("ctrl", "j")
        speak("Opening downloads.")

    elif "open history" in query:
        pyautogui.hotkey("ctrl", "h")
        speak("Opening history.")

    elif "open chrome" in query:
        webbrowser.open("https://www.google.com/chrome/")
        speak("Opening Google Chrome.")

    else:
        return False  # not a chrome command

    return True  # command handled
