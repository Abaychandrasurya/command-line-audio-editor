# command-line-audio-editor

A command-line audio editor for quickly manipulating audio files.  `command-line-audio-editor` provides essential audio processing functionalities for scripting, automation, and quick edits.

## Features

* **Trimming:** Extract portions of audio files with precise start and end times.
* **Conversion:** Convert between common audio formats (e.g., WAV, MP3).  Powered by FFmpeg.
* **Volume Adjustment:** Increase or decrease the volume of audio (in dB).
* **Normalization:** Adjust the volume to a standard level for consistent loudness.
* **Reversing:** Reverse the audio playback.
* **Fading:** Apply fade-in and fade-out effects.
* **Cross-Platform:** Runs on Windows, macOS, and Linux.
* **Robust:** Includes error handling and prevents accidental file overwriting.
* **Progress Bar:** Displays a progress bar for long audio files.

## Installation

1. **Prerequisites:**
    * Python 3.x
    * FFmpeg (Make sure it's in your system's PATH)
    * `pydub` and `tqdm` Python packages:

2. **Install Python packages:**
    ```bash
    pip install pydub tqdm
    ```

3. **Clone the repository (or download the source code):**
    ```bash
    git clone [https://github.com/Abaychandrasurya/command-line-audio-editor.git](https://www.google.com/search?q=https://github.com/Abaychandrasurya/command-line-audio-editor.git) 

## Usage

```bash
python audio_cli.py -i input.wav -o output.wav [options]
