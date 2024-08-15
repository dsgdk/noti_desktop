
# Telegram Keyword Monitor 

A Python-based application that monitors specified Telegram channels for certain keywords and displays matching messages in a GUI.

## Features
- **Keyword Monitoring**: Monitors multiple Telegram channels for predefined keywords.
- **Graphical Interface**: Displays the channel name and message text in a dark-themed, minimalist PyQt5-based GUI.
- **Sound Alerts**: Plays a sound alert when a keyword is detected in a message.
- **Customizable**: Easily add channels, keywords, and change the alert sound via a configuration file.
- **Control Buttons**: Includes buttons to stop the sound alert and clear the message display area.

## Requirements
- Python 3.7+
- [Telethon](https://github.com/LonamiWebs/Telethon)
- [PyQt5](https://pypi.org/project/PyQt5/)
- [Pydub](https://github.com/jiaaro/pydub) (for sound playback)

## Installation
1. **Clone the repository**:
    ```bash
    git clone 
    cd noti_v2
    ```
2. **Install the required Python packages**:
    ```bash
    pip install -r requirements.txt
    ```
3. **Configure the application**:
   - Edit the `config.ini` file to add your Telegram API credentials, channels to monitor, and keywords to search for.
4. **Prepare the sound file**:
   - Place your `.mp4` sound file in the `sounds` directory.
5. **Run the application**:
    ```bash
    python main.py
    ```

## Configuration
Edit the `config.ini` file to customize the application's settings:
```ini
[Telegram]
api_id = YOUR_API_ID
api_hash = YOUR_API_HASH

[Monitoring]
channels = channel1, channel2, channel3
keywords = keywords1, keywords2, keywords3

[Sound]
alert_sound = sounds/alert.mp4
```

## Usage
- **Monitor Telegram Channels**: The application automatically starts monitoring the configured channels once it is run.
- **Stop Sound**: Click the "Stop" button (with the stop icon) to stop the sound alert.
- **Clear Messages**: Click the "Clear" button (with the clear icon) to clear the displayed messages.

## Customization
- **Icons**: Replace the icons in the `icons` folder with your own (`clear_white.png` and `stop_white.png`) to change the button icons.
- **Alert Sound**: Place your `.mp3` file in the `sounds` folder and update the `config.ini` file to use your custom sound.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements
- [Telethon](https://github.com/LonamiWebs/Telethon) - For Telegram API support.
- [PyQt5](https://pypi.org/project/PyQt5/) - For the GUI framework.
- [Pydub](https://github.com/jiaaro/pydub) - For sound handling.