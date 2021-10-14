from typing import Tuple
from pynput.keyboard import Listener
from json import load
from os import listdir,path

from models.KeyboardPlayer import KeyboardPlayer
from models.SoundModifier import SoundModifier


#BUG: increase and decrease volumn not working
audioPlayer = KeyboardPlayer();

json_file = open("./configs.json")
configs = load(json_file)

# Generate all the pitch variatiosn of the audios in the ./audio directory into folders. 
# Those folders have the same name but in plural of each file
if configs['reconstruct']:
    print("Reconstruction audio files...")
    pitch_range: Tuple = [configs['min_pitch'], configs['max_pitch']]
    window_range: int = configs['pitch_window_range']

    for filename in listdir("./audio"):
        if path.isdir(f"./audio/{filename}"):
            continue
        SoundModifier.create_multiple_pitch_audios(f"./audio/{filename}",f"./audio/{filename[:-4]}s/",pitch_range, window_range)

    print("Finish")


def on_press(pressedKey):
    audioPlayer.check_key_combinations(pressedKey)
    audioPlayer.play_sound_based_in_key(pressedKey)
    audioPlayer.last_pressed_key = pressedKey
    return

def on_release(key):
    try:
        audioPlayer.quit_press_keys.remove(key)
        audioPlayer.increase_volumn_press_keys.remove(key)
        audioPlayer.decrease_volumn_press_keys.remove(key)
    except:
        pass   

def initListener():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    last_pressed_key = ""
    initListener()