import pyperclip
import pyautogui as pya
from time import sleep

hotkey = "ctrl + F8"

def copy_clipboard() -> str:
    pyperclip.copy("") # <- This prevents last copy replacing current copy of null.
    pya.hotkey('ctrl', 'c')
    sleep(.01)  # ctrl-c is usually very fast but your program may execute faster
    return pyperclip.paste()