# Holds LMB to, for example, break blocks
# Second is used as unit of time

import pyautogui
import time

delay = 0.4 # Use 0.625 if using an sword. Increase or decrease if used tool is faster or slower breaking blocks
elapsed = 0 
duration = 100

time.sleep(8) # Seconds before starting program

while elapsed < duration:
       pyautogui.mouseDown()
       time.sleep(delay)
       pyautogui.mouseUp()
       elapsed = elapsed + delay
       print("Elapsed time:", elapsed)

pyautogui.alert("Finished")
