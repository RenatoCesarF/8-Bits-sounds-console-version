from typing import Tuple
from pynput import keyboard
from pynput.keyboard import Listener, GlobalHotKeys,KeyCode
from json import load
from os import listdir,path
from modules.AudioManager import AudioManager
from modules.KeyboardPlayer import KeyboardPlayer
from modules.SoundModifier import SoundModifier
from modules.Configs import Configs


class EightBitsSoudns():
    def __init__(self):
        configs = Configs("./configs.json")
        self.configs = configs
        self.keyboardPlayer = KeyboardPlayer(configs.volume);

        if configs.reconstruct:
            self.reconstruct_sounds()

        self.init_hotkeys()
        self.init_listener()

    def reconstruct_sounds(self):
        # Generate all the pitch variatiosn of the audios in the ./audio directory into folders. 
        # Those folders have the same name but in plural of each file
        print("Reconstruction audio files...")
        pitch_range: Tuple = [self.configs.min_pitch, self.configs.max_pitch]
        window_range: int = self.configs.pitch_window_range

        for filename in listdir("./audio"):
            if path.isdir(f"./audio/{filename}"):
                continue
            SoundModifier.create_multiple_pitch_audios(f"./audio/{filename}",f"./audio/{filename[:-4]}s/",pitch_range, window_range)

        print("Finish reconstruction")

    def on_press(self, key):
        self.keyboardPlayer.play_sound_based_in_key(key)
        self.keyboardPlayer.last_pressed_key = key

    def quit_program(self):
        print("Quitting")
        self.hotkeys.stop()
        self.listener.stop()
        self.configs.save_volume_config(self.keyboardPlayer.volume)
        quit()

    def init_listener(self):
        with Listener(on_press= self.on_press) as listener:
            self.listener = listener
            listener.join()

    def init_hotkeys(self):
        self.hotkeys = GlobalHotKeys({
            '<ctrl>+<shift>+<f1>': self.quit_program,
            '<ctrl>+<alt>+=': self.keyboardPlayer.increase_volume,
            '<ctrl>+<alt>+-': self.keyboardPlayer.decrease_volume,
        })
        self.hotkeys.start()

if __name__ == '__main__':
    program = EightBitsSoudns()
