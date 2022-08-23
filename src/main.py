from time import sleep
from keyboard import is_pressed
import re;
from tkinter.messagebox import *
import pyperclip
import pyautogui as pya

from Units import *

hotkey = "ctrl + F8"

def copy_clipboard() -> str:
    pyperclip.copy("") # <- This prevents last copy replacing current copy of null.
    pya.hotkey('ctrl', 'c')
    sleep(.01)  # ctrl-c is usually very fast but your program may execute faster
    return pyperclip.paste()

def SplitNumStr(st:str) -> list[str]:
    res = re.split('([-+]?\d+\.\d+)|([-+]?\d+)', st.strip())
    res_f = [r.strip() for r in res if r is not None and r.strip() != '']
    return res_f

if __name__ == "__main__":
    while True:
        if is_pressed(hotkey):
            selection = SplitNumStr(copy_clipboard())
            Value = detectUnit(selection)
            ConvertedValue = Value.preferedConversion()
            showinfo(f'Converted {Value} into', f' = {ConvertedValue}')
            print(ConvertedValue)
        sleep(.1)