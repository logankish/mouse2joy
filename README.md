# mouse2joy
This project was made as a shortcut to convert OpenTrack data to joystick without using vJoy. I did this for 2 reasons:
- vJoy is old and the newer forks don't work with opentrack.
- The joystick would stay where it was when you stopped moving, I wanted it to reset when you stop moving.

## Overview
mouse2joy converts mouse movements to joystick inputs! 

## Configuration
- `gamepad_mode`: Specifies the type of virtual gamepad to use. Options are `"VDS4Gamepad"` for a virtual DualShock 4 gamepad or `"XUSBGamepad"` for a virtual Xbox 360 gamepad.
- `scale_factor`: Sensitivity
- `speed`: The speed that the program updates the joystick's inputs.
- `quit_command`: This shortcut will close the program, no matter what window you are in.
- `print_values`: If set to `True`, the script will print the joystick values to the console. I don't know why you would need this (or why I added it) but here it is.

## Usage
1. Ensure you have the required libraries installed:
    ```sh
    pip install keyboard vgamepad pyautogui
    ```
2. Run the script:
    ```sh
    python mouse2joy.py
    ```
3. Move your mouse to control the virtual joystick!

## Error Handling
Any exceptions that occur during the execution of the script are caught and printed to the console. Please report these! (I doubt there are any due to the lightweight nature of this script, but you never know!)