from typing import Tuple
from pydub import AudioSegment
from os import mkdir
from pygame import mixer
import os
import shutil


class SoundModifier:
    @staticmethod
    def create_multiple_pitch_audios(file_directory: str, folder_output: str,pitch_range: Tuple = [-1, 2],window_of_each: float = 0.3):
        pitch_value = pitch_range[0]
        last_value = pitch_range[1]
        try:
            shutil.rmtree(folder_output) 
        except:
            pass
            
        mkdir(folder_output)

        while pitch_value <= last_value:
            SoundModifier.make_file_audio_pitched(file_directory, f"{folder_output}sound_{pitch_value:.1f}_pitch",pitch_value )
            pitch_value += window_of_each

    @staticmethod
    def make_file_audio_pitched(file_directory: str, output_directory: str,octaves: int= 0.5)-> None:
        sound = AudioSegment.from_file(file_directory, format="wav")

        # octaves: shift the pitch up by half an octave (speed will increase proportionally)

        new_sample_rate = int(sound.frame_rate * (2.0 ** octaves))

        # keep the same samples but tell the computer they ought to be played at the 
        # new, higher sample rate. This file sounds like a chipmunk but has a weird sample rate.
        hipitch_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})
        hipitch_sound = hipitch_sound.set_frame_rate(44100)
        hipitch_sound.export(output_directory+".wav", format="wav")
        # print(output_directory+".wav")
        # play(hipitch_sound)

    @staticmethod
    def load_folder_as_sound_array(folder_path: str) -> Tuple:
        """With a `folder_path`, returs a tuple of mixer.Sounds with the finded audios in the folder"""
        sounds = []
        for filename in os.listdir(folder_path):
            file_dir = f"{folder_path}{filename}"
            sounds.append(mixer.Sound(file_dir))

        return sounds


  
     
