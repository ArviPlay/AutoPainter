import mouse, pyautogui, time

while True:
    if mouse.is_pressed(button='left'):
        while mouse.is_pressed(button='left'): time.sleep(0.01)
        print(f"{pyautogui.position().x} {pyautogui.position().y}")
        break