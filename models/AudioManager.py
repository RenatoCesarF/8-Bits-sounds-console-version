from typing import Tuple
import pygame
from pygame import mixer

class AudioManager:
    @staticmethod
    def change_array_volume(volume: int, sounds_array: Tuple):
        for sound in sounds_array:
            sound.set_volume(volume)


  