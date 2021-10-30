from json import load,dump
class Configs:
    def __init__(self,directory: str):
        self.directory = directory
        json_file = open(directory,"r+")
        self.configs = load(json_file)

        
        self.pitch_window_range = self.configs['pitch_window_range']
        self.max_pitch =  self.configs['max_pitch']
        self.reconstruct =  self.configs['reconstruct']
        self.min_pitch =  self.configs['min_pitch']
        self.volume= float("{:.2f}".format( self.configs['volume']))
        print(f"CONFIGS: volume {self.volume}")

    def save_volume_config(self, new_volume: float):
        self.configs['volume'] = float("{:.2f}".format(new_volume))
        with open(self.directory,'w') as f:
            dump(self.configs,f)
        print(f"saving volume as {new_volume:.2f} ")
        
