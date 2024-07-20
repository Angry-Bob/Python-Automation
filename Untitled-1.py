import pyautogui
import pyscreeze
import time





time.sleep(2)

# Path to the image file to search for
image_path = 'endlessFishBot.png'

wait_time = 1

# Time to wait after finding and pressing Ctrl before starting the next search (in seconds)
post_action_wait_time = 2

print("Starting the image search loop...")

while True:
    # Search for the image on the screen
    location = pyautogui.locateCenterOnScreen(image_path, confidence=0.95)  # Adjust confidence if needed

    if location:
        print(f"Image found at {location}")
        # Move the cursor to the image location
        # Press the Ctrl key
        pyautogui.keyDown('ctrl')
        pyautogui.keyUp('ctrl')
        print("Ctrl key pressed.")

        # Wait for a specified time before starting the next search
        time.sleep(post_action_wait_time)
    else:
        print("Image not found. Trying again...")
    
    # Wait for a short period before trying again
    time.sleep(wait_time)