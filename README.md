<p align='center'>
  <img src="https://user-images.githubusercontent.com/62253156/135390247-0873764c-6bbe-401a-829f-63af2b6bda6a.png" width="600" height="275.2"/>
</p>

<p align= 'center'>
  <a href="https://gitmoji.carloscuesta.me">
      <img src="https://img.shields.io/badge/gitmoji-%20😜%20😍-FFDD67.svg?style=flat" alt="Gitmoji">
  </a>
</p>


## Python program to play old video-game sounds when you type ⌨️🔊.
> ### There is a [VSCode Extension](https://marketplace.visualstudio.com/items?itemName=RenatoCesarF.8-bits-sounds) like this program :wink:

### 📝Task List:
- [x] Make sounds to ", Home, End, operations and etc
- [x] .exe file
- [x] Add custom icon
- [x] Quit command
- [x] Add a shortcut to change volume
- [X] Save changed volume as preferences
- [X] On quit sound

## ⚓Requirements
### Linux & mac
- install python
- `pip install -r ./requirements.txt` inside the project folder
- if everything goes well it is just run python `main.py`

## ⌨️Commands
- **Increase Volume** <kbd>Ctrl</kbd> <kbd>Alt</kbd> <kbd>+</kbd>
- **Decrease Volume** <kbd>Ctrl</kbd> <kbd>Alt</kbd> <kbd>-</kbd>
- **Quit Command** <kbd>Ctrl</kbd> <kbd>Shift</kbd> <kbd>F1</kbd>


## 📝How to use
If you are in the Windows you can just run the `.exe`, if you are in another SO you need to install Python, install the requirements and run the python main file,
maybe you will need to find a way to run it in the background instead of in a terminal, in the future I will try that and explain it here.

> if you wanna to build from the source code, use: `pyinstaller main.py -F --noconsole --icon=res/icon.ico`
> You need to add the `audio` folder and the `config.json` file to the dist directory

- You can replace the audio files with another one with the same name and generate you onw audios. If you change any file, you need to change `"reconstruct"` configuration to `true`.
- if you don't like the pitch change you can just put the `min_pitch` and `max_pitch`  to 0.
- the range between the pitch changes can be adjusted with the `pitch_window_range` param

## 🚀Releases 
- **[v0.2.0](https://github.com/RenatoCesarF/8-Bits-sounds-console-version/releases/tag/v0.2)**: Add volume controll.
- **[v0.1.5](https://github.com/RenatoCesarF/8-Bits-sounds-console-version/releases/tag/v0.1.5)**: Second Windows release, now with quit command and icon.
- **[v0.1.0](https://github.com/RenatoCesarF/8-Bits-sounds-console-version/releases/tag/pre-release)**: First Windows release, you can change some configurations in the json and run the 8-Bits-sounds.exe program.


## 📺 Demonstration:
### Default sounds demonstration
<video src="https://user-images.githubusercontent.com/62253156/135508166-c95c762d-4bcb-4b9a-8128-e02dc8316469.mp4" />


### Changed sound demonstration</h3>
<video src="https://user-images.githubusercontent.com/62253156/135508504-4e7a1518-5a97-4784-908c-37ed898de0e1.mp4" />


## Contributing
Any pull request is welcome.
