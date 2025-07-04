import pyautogui

def handle_mouse_command(command):
    command = command.lower()

    if "left click" in command:
        pyautogui.click()
    elif "right click" in command:
        pyautogui.click(button='right')
    elif "double click" in command:
        pyautogui.doubleClick()
    elif "middle click" in command:
        pyautogui.click(button='middle')
    elif "scroll up" in command:
        pyautogui.scroll(500)
    elif "scroll down" in command:
        pyautogui.scroll(-500)
    elif "hold left click" in command:
        pyautogui.mouseDown()
    elif "release left click" in command:
        pyautogui.mouseUp()
    elif "move mouse up" in command:
        x, y = pyautogui.position()
        pyautogui.moveTo(x, y - 100)
    elif "move mouse down" in command:
        x, y = pyautogui.position()
        pyautogui.moveTo(x, y + 100)
    elif "move mouse left" in command:
        x, y = pyautogui.position()
        pyautogui.moveTo(x - 100, y)
    elif "move mouse right" in command:
        x, y = pyautogui.position()
        pyautogui.moveTo(x + 100, y)
    elif "move mouse to" in command:
        try:
            # Example: "move mouse to 300 400"
            coords = command.replace("move mouse to", "").strip().split()
            x, y = int(coords[0]), int(coords[1])
            pyautogui.moveTo(x, y)
        except:
            print("Invalid coordinates provided for move mouse to")
    elif "drag to" in command:
        try:
            coords = command.replace("drag to", "").strip().split()
            x, y = int(coords[0]), int(coords[1])
            pyautogui.mouseDown()
            pyautogui.moveTo(x, y, duration=0.5)
            pyautogui.mouseUp()
        except:
            print("Invalid coordinates provided for drag to")
    else:
        return False

    return True
