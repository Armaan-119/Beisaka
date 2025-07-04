import pyautogui


def press_button_command(query, speak=False):
    try:
        query = query.lower()

        # Extract key from query, e.g., "press E" → "e"
        if "press" in query:
            key = query.replace("press", "").strip().lower()

            # Handle special cases
            special_keys = {
                "left arrow": "left",
                "right arrow": "right",
                "up arrow": "up",
                "down arrow": "down",
                "escape": "esc",
                "spacebar": "space",
                "enter": "enter",
                "tab": "tab",
                "control": "ctrl",
                "shift": "shift",
                "alt": "alt",
            }

            key_to_press = special_keys.get(key, key)  # fallback to regular char if not special

            pyautogui.press(key_to_press)

            if speak:
                print(f"Pressed {key_to_press}")
                # speak(f"Pressed {key_to_press}")
        else:
            if speak:
                print("No valid press command found.")
                # speak("No valid press command found.")

    except Exception as e:
        print(f"Error processing press command: {e}")
        # speak("I couldn't press that key. Something went wrong.")
        
        
def perform_shortcut(command):
    command = command.lower()

    if "task manager" in command:
        pyautogui.hotkey('ctrl', 'shift', 'esc')
    elif "close window" in command:
        pyautogui.hotkey('alt', 'f4')
    elif "switch window" in command:
        pyautogui.hotkey('alt', 'tab')
    elif "minimize window" in command:
        pyautogui.hotkey('win', 'down')
    elif "maximize window" in command:
        pyautogui.hotkey('win', 'up')
    elif "lock screen" in command:
        pyautogui.hotkey('win', 'l')
    elif "file explorer" in command:
        pyautogui.hotkey('win', 'e')
    elif "open run" in command:
        pyautogui.hotkey('win', 'r')
    elif "settings" in command:
        pyautogui.hotkey('win', 'i')
    elif "action center" in command:
        pyautogui.hotkey('win', 'a')
    elif "clipboard history" in command:
        pyautogui.hotkey('win', 'v')
    elif "screenshot" in command:
        pyautogui.hotkey('win', 'shift', 's')
    elif "open desktop" in command:
        pyautogui.hotkey('win', 'd')
    elif "start menu" in command:
        pyautogui.press('win')  # or pyautogui.hotkey('ctrl', 'esc')
    else:
        return False  # Command not matched

    return True