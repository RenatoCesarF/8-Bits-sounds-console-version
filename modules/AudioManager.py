from typing import Tuple
from random import randint

class AudioManager:
    @staticmethod
    def change_array_volume(volume: int, sounds_array: Tuple):
        for sound in sounds_array:
            sound.set_volume(volume)

    @staticmethod
    def get_random_sound(sounds_array):
        soundsQuantity = len(sounds_array)-1
        randomPosition = randint(0,soundsQuantity)

        return sounds_array[randomPosition]



  