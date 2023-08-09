from random import randint, uniform
from threading import Thread
from typing import Tuple, Union
from time import sleep, time

import pyautogui
from pynput.mouse import Controller
from pynput.keyboard import Key, KeyCode, Listener

# Dimensions of bottom dialogue option.
BOTTOM_DIALOGUE_MIN_X = 1300
BOTTOM_DIALOGUE_MAX_X = 1700
BOTTOM_DIALOGUE_MIN_Y = 790
BOTTOM_DIALOGUE_MAX_Y = 800

# Pixel coordinates for white part of the autoplay button.
PLAYING_ICON_X = 84
PLAYING_ICON_Y = 46

# Pixel coordinates for white part of the speech bubble in bottom dialogue option.
DIALOGUE_ICON_X = 1301
DIALOGUE_ICON_LOWER_Y = 808
DIALOGUE_ICON_HIGHER_Y = 790

# Pixel coordinates near middle of the screen known to be white while the game is loading.
LOADING_SCREEN_X = 1200
LOADING_SCREEN_Y = 700


def get_pixel(x: int, y: int) -> Tuple[int, int, int]:
    """
    Return the RGB value of a pixel.
    :param x: The x coordinate of the pixel.
    :param y: The y coordinate of the pixel.
    :return: The RGB value of the pixel.
    """

    return pyautogui.pixel(x, y)


def random_interval() -> float:
    """
    Return a random interval between 0.12 and 0.18 seconds, or 0.18 and 0.2 seconds if a 6 is rolled.
    :return: A random interval between 0.12 and 0.18 seconds, or 0.18 and 0.3 seconds if a 6 is rolled.
    """

    return uniform(0.18, 0.2) if randint(1, 6) == 6 else uniform(0.12, 0.18)


def random_cursor_position() -> Tuple[int, int]:
    """
    The cursor is moved to a random position in the bottom dialogue option.
    :return: A random (x, y) in range of the bottom dialogue option.
    """

    x = randint(BOTTOM_DIALOGUE_MIN_X, BOTTOM_DIALOGUE_MAX_X)
    y = randint(BOTTOM_DIALOGUE_MIN_Y, BOTTOM_DIALOGUE_MAX_Y)

    return x, y


def exit_program() -> None:
    """
    Listen for keyboard input to start, stop, or exit the program.
    :return: None
    """

    def on_press(key: (Union[Key, KeyCode, None])) -> None:
        """
        Start, stop, or exit the program based on the key pressed.
        :param key: The key pressed.
        :return: None
        """

        key_pressed: str = str(key)

        if key_pressed == 'Key.f8':
            main.status = 'run'
            print('RUNNING')
        elif key_pressed == 'Key.f9':
            main.status = 'pause'
            print('PAUSED')
        elif key_pressed == 'Key.f12':
            main.status = 'exit'
            exit()

    with Listener(on_press=on_press) as listener:
        listener.join()


def main() -> None:
    """
    Skip Genshin Impact dialogue when it's present based on the colors of 3 specific pixels.
    :return: None
    """
    def is_dialogue_playing():
        return get_pixel(PLAYING_ICON_X, PLAYING_ICON_Y) == (236, 229, 216)

    def is_dialogue_option_available():
        # Confirm loading screen is not white
        if get_pixel(LOADING_SCREEN_X, LOADING_SCREEN_Y) == (255, 255, 255):
            return False

        # Check if lower dialogue icon pixel is white
        if get_pixel(DIALOGUE_ICON_X, DIALOGUE_ICON_LOWER_Y) == (255, 255, 255):
            return True

        # Check if higher dialogue icon pixel is white
        if get_pixel(DIALOGUE_ICON_X, DIALOGUE_ICON_HIGHER_Y) == (255, 255, 255):
            return True

        return False

    main.status = 'pause'
    last_reposition: float = 0.0
    time_between_repositions: float = random_interval() * 40

    print('-------------\n'
          'F8 to start\n'
          'F9 to stop\n'
          'F12 to quit\n'
          '-------------')

    while True:
        while main.status == 'pause':
            sleep(0.5)

        if main.status == 'exit':
            print('Main program closing')
            break

        if is_dialogue_playing() or is_dialogue_option_available():
            if time() - last_reposition > time_between_repositions:
                last_reposition = time()
                time_between_repositions = random_interval() * 40
                mouse.position = random_cursor_position()

            # pyautogui.press('f')
            # pyautogui.click()
            # pyautogui.press('space')
            pyautogui.click()


if __name__ == "__main__":
    mouse = Controller()
    Thread(target=main).start()
    Thread(target=exit_program).start()
