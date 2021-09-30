import librosa
from pygame import mixer

mixer.init()
mixer.pre_init(44100, -16, 2, 512)
mixer.set_num_channels(32)

y, sr = librosa.load('./audio/normal_key_sound.wav', sr=16000) # y is a numpy array of the wav file, sr = sample rate
y_shifted = librosa.effects.pitch_shift(y, sr, n_steps=4) # shifted by 4 half steps

mixer.Sound(y_shifted).play()