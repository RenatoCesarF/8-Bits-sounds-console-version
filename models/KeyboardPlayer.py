from pynput import keyboard
from models.SoundModifier import SoundModifier
from random import randint
from pygame import mixer

class KeyboardPlayer:
    mixer.init()
    mixer.pre_init(44100, -16, 2, 512)
    mixer.set_num_channels(32)

    last_pressed_key = ""

    quit_press_keys = set();
    increase_volumn_press_keys = set();
    decrease_volumn_press_keys = set();

    # Key arrays
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

    # Combination keys
    quit_key_combination  = {keyboard.Key.shift_l, keyboard.Key.ctrl_l, keyboard.Key.f1}
    increase_volumn_combination = {keyboard.Key.shift_l, keyboard.Key.ctrl_l, keyboard.KeyCode(char='+')}
    decrease_volumn_combination = {keyboard.Key.shift_l, keyboard.Key.ctrl_l, keyboard.KeyCode(char='-')}

    # Load sounds
    normal_key_sounds =       SoundModifier.load_folder_as_sound_array("./audio/normal_key_sounds/")
    space_key_sounds =        SoundModifier.load_folder_as_sound_array("./audio/space_sounds/")
    tab_key_sounds =          SoundModifier.load_folder_as_sound_array("./audio/tab_sounds/")
    enter_key_sounds =        SoundModifier.load_folder_as_sound_array("./audio/enter_sounds/")
    backspace_key_sounds =    SoundModifier.load_folder_as_sound_array("./audio/backspace_sounds/")
    chaves_sounds =           SoundModifier.load_folder_as_sound_array("./audio/chaves_sounds/")
    bracket_sounds =          SoundModifier.load_folder_as_sound_array("./audio/bracket_sounds/")
    close_bracket_sounds =    SoundModifier.load_folder_as_sound_array("./audio/close_bracket_sounds/")
    arrow_sounds =            SoundModifier.load_folder_as_sound_array("./audio/arrow_sounds/")

    def check_key_combinations(self, pressedKey):
        if pressedKey in self.quit_key_combination:
            self.quit_press_keys.add(pressedKey)
            if all(k in self.quit_press_keys for k in self.quit_key_combination):
                print("Quitting...")
                quit()

        if pressedKey in self.increase_volumn_combination:
            self.increase_volumn_press_keys.add(pressedKey)
            if all(k in self.increase_volumn_press_keys for k in self.increase_volumn_combination):
                print("+")
                return

        if pressedKey in self.decrease_volumn_combination:
            self.decrease_volumn_press_keys.add(pressedKey)
            if all(k in self.decrease_volumn_press_keys for k in self.decrease_volumn_combination):
                print("-")

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
        
    @staticmethod
    def get_random_sound(sounds_array):
        soundsQuantity = len(sounds_array)-1
        randomPosition = randint(0,soundsQuantity)

        return sounds_array[randomPosition]
