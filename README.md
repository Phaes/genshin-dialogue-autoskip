# genshin-dialogue-autoskip (Keyboard and Mouse Only Version)

## Overview
This script automatically skips dialogue in Genshin Impact, always chooses the bottom dialogue option.

*This is for educational purposes only. I advice against relying on the script in daily gameplay, as it will ruin your story experience.*

## Requirements
- The game running on Main Display 1
- The script run as Admin to allow key and mouse emulation
- Required Python packages installed with `pip install -r requirements.txt`

## Usage
1. Run `autoskip_dialogue.py` with Admin privileges
	-  Tip: You can right-click the handy `run.bat` file and select "Run as administrator"
2. Confirm that the auto-detected resolution matches your screen dimensions (it will be saved in `.env`)
3. When you're ready, press F8 on your keyboard to start the main loop

## Experimental Gamepad Support
- The `main` branch of this repo which you're currently on, is for keyboard+mouse only. If you're using a gamepad to play the game, switch to the `gamepad_only` branch!
