from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
import pyautogui
import time, sys, os

os.system("mode con cols=31 lines=4")
os.system("title Keep On Mouse")

print()
print(' ( close this window to stop )')

now = time.time()

def log_same_line(msg):
    sys.stdout.write("\033[K")
    print(f'    {msg}', end='\r')

def move_mouse():
    global now
    screenWidth, screenHeight = pyautogui.size()
    log_same_line( f'(     )  moving mouse' )
    pyautogui.moveTo( 50, screenHeight / 2)
    time.sleep(0.5)
    log_same_line( f'( .   )  moving mouse' )
    pyautogui.click()
    time.sleep(0.5)
    log_same_line( f'( ..  )  moving mouse' )
    pyautogui.moveTo( screenWidth - 50, screenHeight / 2 )
    time.sleep(0.5)
    log_same_line( f'( ... )  moving mouse')
    pyautogui.click()
    time.sleep(0.5)
    now = time.time()

def on_press(key):
    global now
    now = time.time()

def on_move(x, y):
    global now
    now = time.time()

def on_click(x, y, button, pressed):
    global now
    now = time.time()

def on_scroll(x, y, dx, dy):
    global now
    now = time.time()

# Setup the listener threads
keyboard_listener = KeyboardListener(
    on_press=on_press
    # ,on_release=on_release
)
mouse_listener = MouseListener(
    on_move=on_move
    ,on_click=on_click
    ,on_scroll=on_scroll
)

keyboard_listener.start()
mouse_listener.start()

while True:
    last = int(time.time()) - int(now)
    if last >= 30: move_mouse()
    log_same_line( 'last activity: %02d sec' % last )
    time.sleep(1)