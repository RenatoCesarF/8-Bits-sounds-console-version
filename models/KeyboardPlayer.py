from typing import Tuple
from pynput import keyboard
from models.SoundModifier import SoundModifier
from models.AudioManager import AudioManager
from random import randint
from pygame import mixer

class KeyboardPlayer:
    def __init__(self):
        self.volume = 1

        self.init_mixer()
        self.create_key_arrays()    
        self.load_sounds()
        self.last_pressed_key = ""

    def play_sound_based_in_key(self, pressedKey):
        if pressedKey in self.open_signal_keys:
            self.get_random_sound(self.bracket_sounds).play()
            return

        if pressedKey in self.close_signal_keys:
            self.get_random_sound(self.close_bracket_sounds).play()
            return

        if pressedKey in self.chaves_keys:
            self.get_random_sound(self.chaves_sounds).play()
            return
        
        if pressedKey in self.arrow_keys:
            self.get_random_sound(self.arrow_sounds).play()
            return

        if pressedKey == keyboard.Key.space:
            self.get_random_sound(self.space_key_sounds).play()
            return

        if pressedKey == keyboard.Key.tab:
            self.get_random_sound(self.tab_key_sounds).play()
            return

        if pressedKey == keyboard.Key.backspace: 
            self.get_random_sound(self.backspace_key_sounds).play()
            return

        if pressedKey == keyboard.Key.enter:
            self.get_random_sound(self.enter_key_sounds).play()
            return

        if self.last_pressed_key == pressedKey and pressedKey in self.should_not_repeat_keys:
            return

        self.get_random_sound(self.normal_key_sounds).play()
    
    def change_volume(self, volume: int):
        AudioManager.change_array_volume(volume,self.normal_key_sounds)
        AudioManager.change_array_volume(volume,self.space_key_sounds)
        AudioManager.change_array_volume(volume,self.tab_key_sounds)
        AudioManager.change_array_volume(volume,self.enter_key_sounds)
        AudioManager.change_array_volume(volume,self.backspace_key_sounds)
        AudioManager.change_array_volume(volume,self.chaves_sounds)
        AudioManager.change_array_volume(volume,self.bracket_sounds)
        AudioManager.change_array_volume(volume,self.close_bracket_sounds)
        AudioManager.change_array_volume(volume,self.arrow_sounds)

    def increase_volume(self):
        if self.volume >= 1.1:
            print("volume is already at maximum")
            return
        self.volume += 0.1
        self.change_volume(self.volume)

    def decrease_volume(self):
        if self.volume <= 0:
            print("volume is already at minimun")
            return
        
        self.volume -= 0.1
        self.change_volume(self.volume)
    
    def init_mixer(self):
        mixer.init()
        mixer.pre_init(44100, -16, 2, 512)
        mixer.set_num_channels(32)

    def create_key_arrays(self):
        self.open_signal_keys = [keyboard.KeyCode(char='['), keyboard.KeyCode(char='(')]
        self.close_signal_keys = [keyboard.KeyCode(char=']'), keyboard.KeyCode(char=')')]
        self.chaves_keys = [keyboard.KeyCode(char='{'), keyboard.KeyCode(char='}')]
        self.arrow_keys = [keyboard.Key.left,keyboard.Key.right, keyboard.Key.down, keyboard.Key.up]
        self.should_not_repeat_keys = [
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
    
    def load_sounds(self):
        self.normal_key_sounds: Tuple =       SoundModifier.load_folder_as_sound_array("./audio/normal_key_sounds/")
        self.space_key_sounds: Tuple =        SoundModifier.load_folder_as_sound_array("./audio/space_sounds/")
        self.tab_key_sounds: Tuple =          SoundModifier.load_folder_as_sound_array("./audio/tab_sounds/")
        self.enter_key_sounds: Tuple =        SoundModifier.load_folder_as_sound_array("./audio/enter_sounds/")
        self.backspace_key_sounds: Tuple =    SoundModifier.load_folder_as_sound_array("./audio/backspace_sounds/")
        self.chaves_sounds: Tuple =           SoundModifier.load_folder_as_sound_array("./audio/chaves_sounds/")
        self.bracket_sounds: Tuple =          SoundModifier.load_folder_as_sound_array("./audio/bracket_sounds/")
        self.close_bracket_sounds: Tuple =    SoundModifier.load_folder_as_sound_array("./audio/close_bracket_sounds/")
        self.arrow_sounds: Tuple =            SoundModifier.load_folder_as_sound_array("./audio/arrow_sounds/")

    @staticmethod
    def get_random_sound(sounds_array):
        soundsQuantity = len(sounds_array)-1
        randomPosition = randint(0,soundsQuantity)

        return sounds_array[randomPosition]
