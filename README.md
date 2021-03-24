# SimpleMinecraftScripts
A brief collection of simple Python Scripts for Minecraft automation

These scripts are quite simple. Each one makes different basic Minecraft actions automatically, such as holding shift automatically to avoid falling. Tested on Minecraft Java Edition 1.14.4 (Windows 10), should work with almost every other Java version, not tested with Bedrock Edition. 

### Requirements
  - Python 3.x
  - PyAutoGUI Installed (except for HoldShift.py)

### Brief description
  - HoldShift: Holds shift for a variable amount of time
  - HoldRMB and HoldLMB: Holds Right and Left Mouse Buttons for a variable amount of time with a configurable delay between clicking the button and releasing it. Can be used for repeated clicking instead of holding.
  - RMB-SpaceLoop: Jumps while clicking RMB. Useful for making colums. In my case I used it for building a huge concrete powder column over a lake. Once done, I used HoldLMB to remove the powder converted to concrete.

#### Why does the program runs for less time than what I've input?
In the all-in-one program, time.sleep() function doesn't work properly unless `-u` argument is added to `python` options. However, it should work properly for single scripts. Run script like this if something fails.
`python3 -u main.py`

### Credits
Thread where I took the code to input keypresses to DirectInput: https://stackoverflow.com/questions/14489013/simulate-python-keypresses-for-controlling-a-game
  
#### Note: 
These scripts are actually extremely simple, so they may not work as well as a decent coder/programmer could have done them. I'm yet a beginner so my code is barely functional. I only recommend using them for very basic stuff.
