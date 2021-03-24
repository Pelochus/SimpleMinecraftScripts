"""
--- SimpleMinecraftScripts --- 
A brief collection of simple Python Scripts for Minecraft automation

Made by: Pelochus

"""

import pyautogui
import smcs

# --- Functions ---
def show_menu():
    print("--------------------------------------------------------------------------------")

    print("1: Hold Left Mouse Button\n")
    print("\t Mainly used for breaking blocks or hitting mobs\n\n")

    print("2: Hold Right Mouse Button\n")
    print("\t Used for placing blocks or automating hoe\n\n")

    print("3: Hold Shift\n")
    print("\t Useful for old Java Editions which doesn't have shift hold options\n\n")

    print("4: Space-RMB Loop\n")
    print("\t Useful for making columns of blocks automatically\n\n")

    print("Any other value will close the program!")

    print("--------------------------------------------------------------------------------")

# --- Main Program ---

duration = int(input("How long do you want the script to keep working?\n"))
smcs = smcs.smcs(duration)
show_menu()
option = int(input("Now, choose which script do you want to run:\n"))

if (option == 1):
    smcs.hold_lmb()
elif (option == 2):
    smcs.hold_rmb()
elif (option == 3):
    smcs.hold_shift()
elif (option == 4):
    smcs.space_rmb_loop()
else:
    pyautogui.alert("Finished program")

