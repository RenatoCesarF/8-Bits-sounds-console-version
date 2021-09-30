from typing import Tuple
from pynput.keyboard import Listener
from pynput import keyboard
import os
from pygame import mixer
from models.SoundModifier import SoundModifier
from random import randint
import json

mixer.init()
mixer.pre_init(44100, -16, 2, 512)
mixer.set_num_channels(32)

json_file = open("./configs.json")
configs = json.load(json_file)

#Keys combinations
open_signal_keys = [keyboard.KeyCode(char='['), keyboard.KeyCode(char='(')]
close_signal_keys = [keyboard.KeyCode(char=']'), keyboard.KeyCode(char=')')]
chaves_keys = [keyboard.KeyCode(char='{'), keyboard.KeyCode(char='}')]
arrow_keys = [keyboard.Key.left,keyboard.Key.right, keyboard.Key.down, keyboard.Key.up]
should_not_repeat_keys = [
    keyboard.Key.ctrl_r, 
    keyboard.Key.ctrl_l, 
    keyboard.Key.alt,
    keyboard.Key.alt_l,
    keyboard.Key.alt_r,
    keyboard.Key.alt_gr,
    keyboard.Key.cmd,
    keyboard.Key.cmd_l,
    keyboard.Key.cmd_r,
    keyboard.Key.shift,
    keyboard.Key.shift_l,
    keyboard.Key.shift_r,
    keyboard.Key.caps_lock,
    keyboard.Key.f1,
    ]

#=========================== Filling audio arrays =====================

# Generate all the pitch variatiosn of the audios in the ./audio directory into folders. 
# Those folders have the same name but in plural of each file
if configs['reconstruct']:
    print("Reconstruction audio files...")
    pitch_range: Tuple = [configs['min_pitch'], configs['max_pitch']]
    window_range: int = configs['pitch_window_range']

    for filename in os.listdir("./audio"):
        if os.path.isdir(f"./audio/{filename}"):
            continue
        SoundModifier.create_multiple_pitch_audios(f"./audio/{filename}",f"./audio/{filename[:-4]}s/",pitch_range, window_range)

    print("Finish")

#=========================== Creating the array with variations ==============
normal_key_sounds =       SoundModifier.load_folder_as_sound_array("./audio/normal_key_sounds/")
space_key_sounds =        SoundModifier.load_folder_as_sound_array("./audio/space_sounds/")
tab_key_sounds =          SoundModifier.load_folder_as_sound_array("./audio/tab_sounds/")
enter_key_sounds =        SoundModifier.load_folder_as_sound_array("./audio/enter_sounds/")
backspace_key_sounds =    SoundModifier.load_folder_as_sound_array("./audio/backspace_sounds/")
chaves_sounds =           SoundModifier.load_folder_as_sound_array("./audio/chaves_sounds/")
bracket_sounds =          SoundModifier.load_folder_as_sound_array("./audio/bracket_sounds/")
close_bracket_sounds =    SoundModifier.load_folder_as_sound_array("./audio/close_bracket_sounds/")
arrow_sounds =            SoundModifier.load_folder_as_sound_array("./audio/arrow_sounds/")

global last_pressed_key
last_pressed_key = ""

def on_press(pressedKey):
    global last_pressed_key
    if pressedKey in open_signal_keys:
        get_random_sound(bracket_sounds).play()
        return

    if pressedKey in close_signal_keys:
        get_random_sound(close_bracket_sounds).play()
        return

    if pressedKey in chaves_keys:
        get_random_sound(chaves_sounds).play()
        return
    
    if pressedKey in arrow_keys:
        get_random_sound(arrow_sounds).play()
        return

    if pressedKey == keyboard.Key.space:
        get_random_sound(space_key_sounds).play()
        return

    if pressedKey == keyboard.Key.tab:
        get_random_sound(tab_key_sounds).play()
        return

    if pressedKey == keyboard.Key.backspace: 
        get_random_sound(backspace_key_sounds).play()
        return

    if pressedKey == keyboard.Key.enter:
        get_random_sound(enter_key_sounds).play()
        return

    if last_pressed_key == pressedKey and pressedKey in should_not_repeat_keys:
        return
    
    get_random_sound(normal_key_sounds).play()
    last_pressed_key = pressedKey
    return

def get_random_sound(sounds_array):
    soundsQuantity = len(sounds_array)-1
    randomPosition = randint(0,soundsQuantity)

    return sounds_array[randomPosition]

def initListener():
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    last_pressed_key = ""
    initListener()