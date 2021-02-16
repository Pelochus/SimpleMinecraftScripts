# Jumps and presses RMB. Useful for making a tall column of blocks
# Second is used for time commands

import pyautogui
import time
import os
import ctypes
import win32api

# ---------- Classes and Functions ----------

# This was taken from a webpage a long time ago, I can't explain how it works
# It makes Minecraft understand key presses from the script
# PyAutoGUI wasnt capable of this 

PUL = ctypes.POINTER(ctypes.c_ulong)

class KeyBdInput(ctypes.Structure):
   _fields_ = [("wVk", ctypes.c_ushort),
               ("wScan", ctypes.c_ushort),
               ("dwFlags", ctypes.c_ulong),
               ("time", ctypes.c_ulong),
               ("dwExtraInfo", PUL)]


class HardwareInput(ctypes.Structure):
   _fields_ = [("uMsg", ctypes.c_ulong),
               ("wParamL", ctypes.c_short),
               ("wParamH", ctypes.c_ushort)]


class MouseInput(ctypes.Structure):
   _fields_ = [("dx", ctypes.c_long),
               ("dy", ctypes.c_long),
               ("mouseData", ctypes.c_ulong),
               ("dwFlags", ctypes.c_ulong),
               ("time", ctypes.c_ulong),
               ("dwExtraInfo", PUL)]


class Input_I(ctypes.Union):
   _fields_ = [("ki", KeyBdInput),
               ("mi", MouseInput),
               ("hi", HardwareInput)]


class Input(ctypes.Structure):
   _fields_ = [("type", ctypes.c_ulong),
("ii", Input_I)]

def press_key(key):
   extra = ctypes.c_ulong(0)
   ii_ = Input_I()

   flags = 0x0008

   ii_.ki = KeyBdInput(0, key, flags, 0, ctypes.pointer(extra))
   x = Input(ctypes.c_ulong(1), ii_)
   ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def release_key(key):
   extra = ctypes.c_ulong(0)
   ii_ = Input_I()

   flags = 0x0008 | 0x0002

   ii_.ki = KeyBdInput(0, key, flags, 0, ctypes.pointer(extra))
   x = Input(ctypes.c_ulong(1), ii_)
   ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))
	
# ----------- Main -----------

delay = 0.5 
elapsed = 0 
duration = 80 
space = 0x39 # Used link for conversion: https://gist.github.com/tracend/912308

time.sleep(5) # Margin before starting program
pyautogui.mouseDown(button = "right") # Holds RMB

while elapsed < duration:
        press_key(space)
        time.sleep(time)
        release_key(space)
        elapsed = elapsed + delay
        if elapsed >= duration:
           pyautogui.mouseUp(button = "right")			
        print("Elapsed time:", elapsed)

pyautogui.mouseUp(button = "right")
pyautogui.alert("Finished")