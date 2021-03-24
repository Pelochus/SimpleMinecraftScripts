# Necessary class for SimpleMinecraftScripts

import pyautogui
import time
import mckey

class smcs:
    # Variables
    elapsed = 0
    delay = 0
    duration = 0
    # See: https://gist.github.com/tracend/912308
    shift = 0x2A
    space = 0x39

    # Constructor
    def __init__(self, input_duration):
        self.duration = input_duration

    def hold_lmb(self):
        self.delay = 0.4 # Use 0.625 if using an sword. Increase or decrease if used tool is faster or slower breaking blocks

        print("Starting in 8 seconds...")
        time.sleep(8)

        while self.elapsed < self.duration:
            pyautogui.mouseDown()
            time.sleep(self.delay)
            pyautogui.mouseUp()
            self.elapsed = self.elapsed + self.delay
            print("Elapsed time:", self.elapsed)
            
        pyautogui.alert("Finished")

    def hold_rmb(self):
        self.delay = 0.1 

        print("Starting in 8 seconds...")
        time.sleep(8)

        while self.elapsed < self.duration:
            pyautogui.mouseDown(button = "right")
            time.sleep(self.delay)
            pyautogui.mouseUp(button = "right")
            self.elapsed = self.elapsed + self.delay
            print("Elapsed time:", self.elapsed)

        pyautogui.alert("Finished")

    def hold_shift(self):
        self.delay = 1
        print("Starting in 8 seconds...")
        time.sleep(8)

        while self.elapsed < self.duration:
            mckey.press_key(self.shift)
            time.sleep(self.delay)
            self.elapsed = self.elapsed + self.delay
            
        mckey.release_key(self.shift)
        pyautogui.alert("Finished")
    
    def space_rmb_loop(self):
        self.delay = 0.5

        print("Starting in 8 seconds...")
        time.sleep(8)
        pyautogui.mouseDown(button = "right") # Holds RMB

        while self.elapsed < self.duration:
                mckey.press_key(self.space)
                time.sleep(self.delay)
                mckey.release_key(self.space)
                self.elapsed = self.elapsed + self.delay
                if self.elapsed >= self.duration:
                    pyautogui.mouseUp(button = "right")			
                    print("Elapsed time:", self.elapsed)

        pyautogui.mouseUp(button = "right")
        pyautogui.alert("Finished")
