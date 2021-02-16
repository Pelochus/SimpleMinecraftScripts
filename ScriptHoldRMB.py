# Holds RMB. For example, triggering a button repeatedly
# Second is used as unit of time

import pyautogui
import os
import time
import ctypes
import win32api

delay = 0.8 
elapsed = 0
duration = 1800 

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

def hold(key):
   extra = ctypes.c_ulong(0)
   ii_ = Input_I()

   flags = 0x0008

   ii_.ki = KeyBdInput(0, key, flags, 0, ctypes.pointer(extra))
   x = Input(ctypes.c_ulong(1), ii_)
   ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def release(key):
   extra = ctypes.c_ulong(0)
   ii_ = Input_I()

   flags = 0x0008 | 0x0002

   ii_.ki = KeyBdInput(0, key, flags, 0, ctypes.pointer(extra))
   x = Input(ctypes.c_ulong(1), ii_)
   ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))
   
# Conversion Table used: https://gist.github.com/tracend/912308

shift = 0x2A
n1 = 0x02

# ---------- MAIN ----------

time.sleep(8) # Delay before starting
print("STARTING NOW...")
# hold(shift) # Used for avoiding hunger. May cause problems

while elapsed < duration:
       pyautogui.mouseDown(button = "right")
       time.sleep(delay)
       pyautogui.mouseUp(button = "right")
       elapsed = elapsed + delay
       print("Elapsed time:", elapsed)

# release(shift) # Uncomment if hold(shift) is also uncommented
pyautogui.alert("Finished")