from time import sleep
from keyboard import is_pressed
import re;
from tkinter.messagebox import *

from Units import *
from Clipboard import *

def SplitNumStr(s:str) -> list[str]:
    res:list[str] = re.split('([-+]?\d+\.\d+)|([-+]?\d+)', s.strip())
    res_f:list[str] = [r.strip() for r in res if r is not None and r.strip() != '']
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