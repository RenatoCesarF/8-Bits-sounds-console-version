from pynput.keyboard import Listener
from pynput import keyboard
from pygame import mixer

mixer.init()
mixer.pre_init(44100, -16, 2, 512)
mixer.set_num_channels(32)

#importing sounds

defaultSound = mixer.Sound("./audio/normal_key_sound.wav")
space_audio = mixer.Sound("./audio/space_sound.wav")
backspace_audio = mixer.Sound("./audio/backspace.wav")
enter_audio = mixer.Sound("./audio/enter_sound.wav")
chaves_audio = mixer.Sound("./audio/chaves.wav")
open_signal_audio = mixer.Sound("./audio/bracket.wav")
close_signal_audio = mixer.Sound("./audio/close_bracket.wav")
arrow_audio = mixer.Sound("./audio/arrow_audio.wav")
tab_audio = mixer.Sound("./audio/tab_audio.wav")

open_signal_keys = [keyboard.KeyCode(char='['), keyboard.KeyCode(char='(')]
close_signal_keys = [keyboard.KeyCode(char=']'), keyboard.KeyCode(char=')')]
chaves_keys = [keyboard.KeyCode(char='{'), keyboard.KeyCode(char='}')]
arrow_keys = [keyboard.Key.left,keyboard.Key.right, keyboard.Key.down, keyboard.Key.up]

def on_press(pressedKey):
    if pressedKey in open_signal_keys:
        open_signal_audio.play()
        return

    if pressedKey in close_signal_keys:
        close_signal_audio.play()
        return

    if pressedKey in chaves_keys:
        chaves_audio.play()
        return
    
    if pressedKey in arrow_keys:
        arrow_audio.play()
        return

    if pressedKey == keyboard.Key.space:
        space_audio.play()
        return

    if pressedKey == keyboard.Key.backspace: 
        backspace_audio.play()
        return

    if pressedKey == keyboard.Key.enter:
        enter_audio.play()
        return

    if pressedKey == keyboard.Key.tab:
        tab_audio.play()
        return

    else:
        defaultSound.play()
        return

def initListener():
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    initListener()