from time import sleep
from keyboard import is_pressed
import re;
from tkinter import *
from tkinter import messagebox
import pyperclip
import pyautogui as pya

from Units import *

hotkey = "ctrl + F8"

def copy_clipboard() -> str:
    pyperclip.copy("") # <- This prevents last copy replacing current copy of null.
    pya.hotkey('ctrl', 'c')
    sleep(.01)  # ctrl-c is usually very fast but your program may execute faster
    return pyperclip.paste()

def ShowBox(InitialValue:UnitBase, ConvertedValue:UnitBase):
    root = Tk()
    root.withdraw()
    messagebox.showinfo("Unit converted",f'{str(InitialValue.val.__round__(2)) + InitialValue.unitExt} = {str(ConvertedValue.val.__round__(2)) + ConvertedValue.unitExt}')
    root.destroy()

def SplitNumStr(st:str):
    res = re.split('([-+]?\d+\.\d+)|([-+]?\d+)', st.strip())
    return [r.strip() for r in res if r is not None and r.strip() != '']

if __name__ == "__main__":
    while True:
        if is_pressed(hotkey):
            selection = SplitNumStr(copy_clipboard())
            InitialValue = detectUnit(selection)
            ConvertedValue = InitialValue.preferedConversion()
            ShowBox(InitialValue, ConvertedValue)
        sleep(.1)