import tkinter as tk
import threading
import time
import keyboard

file_name = 1
running = False
repeat_count = 0

def toggle_script():
    global running
    running = not running
    if running:
        print("Script started.")
        execute_key_presses()
    else:
        print("Script stopped.")

def execute_key_presses():
    global file_name, repeat_count, running
    while running and repeat_count > 0:
        # Reveal Layer
        time.sleep(0.5)
        keyboard.send('shift+v')
        time.sleep(0.5)
    
        # Open save menu
        keyboard.send('ctrl+;')
        time.sleep(0.5)

        # Remove default name
        keyboard.send('backspace')
        time.sleep(0.5)

        # Type out the variable 'file_name'
        keyboard.write(str(file_name))
        time.sleep(0.5)

        # Add 1 to the variable 'file_name'
        file_name += 1

        # Press Enter key
        keyboard.send('enter')
        time.sleep(0.5)
        
        # Press Enter key
        keyboard.send('enter')
        time.sleep(0.75)

        # Hide Layer
        keyboard.send('shift+v')
        time.sleep(0.5)
        
        # Move up a layer
        keyboard.send('alt+]')
        time.sleep(1)

        repeat_count -= 1

    # Script has completed all loops
    running = False
    print("Script stopped.")

def keyboard_listener():
    while True:
        if keyboard.is_pressed('ctrl+7'):
            if not running:
                start_script()
        time.sleep(0.01)

keyboard_thread = threading.Thread(target=keyboard_listener)
keyboard_thread.daemon = True
keyboard_thread.start()

def start_script():
    global repeat_count
    repeat_count = int(entry.get())
    print("Starting script with repeat count:", repeat_count)
    toggle_script()

root = tk.Tk()
root.title("Script Automation")
root.geometry("300x100")

hotkey_label = tk.Label(root, text="Press Ctrl + 7 to start/stop the script")
hotkey_label.pack()

hotkey_label = tk.Label(root, text="Hide ALL layers before running the script")
hotkey_label.pack()

label = tk.Label(root, text="Enter loop count:")
label.pack()

entry = tk.Entry(root)
entry.pack()

root.mainloop()
