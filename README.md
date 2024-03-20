# CSP_Automation
Automates the task of saving Clip Studio Paint layers as their own PNG images.

# Installation
## Windows
1. Download the exe file from the [releases](https://github.com/HiroNewf/CSP_Automation/releases) section of this repo
## Linux
1. Clone this repo `git clone <https://github.com/HiroNewf/CSP_Automation.git`>
2. Move into the repo's directory `cd CSP_Automation`
3. Install the requirements `pip install -r requirements.txt`
4. Run the python script `python3 clip.py`
# Dependancies
This program utilizes hotkeys in Clip Studio Paint to perform the necessary actions for saving each layer as its own PNG file. Before you run this script you must have the following hotkeys set in Clip Studio Paint:
- Change Selected Layer (Layer Above): Up arrow
- Show Layer: Shift+V
- Export (Single Layer) as .png: Ctrl+;

Additionally you must not have any png files within your default Clip Studio Paint export location that has a name like '1', '2', '3', etc as this will cause conflicts with the program's own attempts at saving files with names like these.
# Usage
1. Open Clip Studio Paint and set all of your layers to not visible (with the exception of your background layer if you want one)
2. Select your first layer (or whatever layer you want the script to start with)
3. Run the exe file / python script
4. Set the number of times you want the script to run (i.e the number of layers you want to be exported to PNGs)
5. Tab back into Clip Studio Paint and start the script with control+7
