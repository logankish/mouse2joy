import keyboard
import vgamepad as vg
import pyautogui
import time

# Configuration
gamepad_mode = "VDS4Gamepad"  
scale_factor = 50
speed = 0.0005
quit_command = "ctrl+shift+c"  
print_values = True  

# Gamepad initialization
if gamepad_mode == "VDS4Gamepad":
    gamepad = vg.VDS4Gamepad()
elif gamepad_mode == "XUSBGamepad":
    gamepad = vg.VX360Gamepad()

# Function to convert mouse movement to joystick values
def mouse2joy(delta_x, delta_y, scale_factor):
    x_value = max(-1, min(1, delta_x / scale_factor))
    y_value = max(-1, min(1, delta_y / scale_factor))
    return x_value, y_value

# Init mouse position
screen_width, screen_height = pyautogui.size()
center_x, center_y = screen_width / 2, screen_height / 2
pyautogui.moveTo(center_x, center_y)
prev_x, prev_y = center_x, center_y

# Main loop
print(f"Program started. Press {quit_command} to exit.")
try:
    while True:
        if keyboard.is_pressed(quit_command):
            break
        curr_x, curr_y = pyautogui.position()
        delta_x = curr_x - center_x
        delta_y = curr_y - center_y
        x_value, y_value = mouse2joy(delta_x, delta_y, scale_factor)
        gamepad.right_joystick_float(x_value_float=x_value, y_value_float=y_value)
        gamepad.update()
        if print_values:
            print("Joystick values:", x_value, y_value)
        pyautogui.moveTo(center_x, center_y)
        time.sleep(speed)
except Exception as e:
    print("Error:", e)

print("Program terminated.")
