from json import load
class Configs:
    def __init__(self,directory: str):
        json_file = open(directory,"r+")
        configs = load(json_file)
        self.configs = configs
        
        self.pitch_window_range = configs['pitch_window_range']
        self.max_pitch = configs['max_pitch']
        self.reconstruct = configs['reconstruct']
        self.min_pitch = configs['min_pitch']
        self.volume= float("{:.2f}".format(configs['volume']))
        print(f"CONFIGS: volume {self.volume}")

    def save_volume_config(self, new_volume: float):
        self.configs['volume'] = float("{:.2f}".format(new_volume))
        print(f"saving volume as {new_volume:.2f} ")
        
