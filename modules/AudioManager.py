from typing import Tuple
from os import listdir
from random import randint
from pygame import mixer

class AudioManager:

    @staticmethod
    def get_random_sound(sounds_array):
        soundsQuantity = len(sounds_array)-1
        randomPosition = randint(0,soundsQuantity)

        return sounds_array[randomPosition]

    @staticmethod
    def load_folder_as_sound_array(folder_path: str) -> Tuple:
        """With a `folder_path`, returs a tuple of mixer.Sounds with the finded audios in the folder"""
        sounds = []
        for filename in listdir(folder_path):
            file_dir = f"{folder_path}{filename}"
            sounds.append(mixer.Sound(file_dir))

        return sounds
    
    @staticmethod
    def change_sound_array_volume(volume: int, sounds_array: Tuple):
        for sound in sounds_array:
            sound.set_volume(volume)



  