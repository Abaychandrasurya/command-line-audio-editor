from pydub import AudioSegment
from pydub.effects import normalize, reverse, fade_in, fade_out
import argparse
import os
from tqdm import tqdm

def load_audio(input_file):
    """Loads an audio file using pydub."""
    try:
        audio = AudioSegment.from_file(input_file)
        return audio
    except Exception as e:
        print(f"Error loading audio file: {e}")
        return None

def trim_audio(audio, output_file, start_time, end_time):
    """Trims the audio."""
    try:
        if os.path.exists(output_file):
            if not confirm_overwrite(output_file):
                return
        trimmed_audio = audio[start_time * 1000:end_time * 1000]
        trimmed_audio.export(output_file, format="wav")
        print(f"Audio trimmed and saved to {output_file}")
    except Exception as e:
        print(f"Error trimming audio: {e}")

def convert_audio(audio, output_file, format):
    """Converts the audio, handling potential errors."""
    try:
        if os.path.exists(output_file):
            if not confirm_overwrite(output_file):
                return
        audio.export(output_file, format=format)
        print(f"Audio converted and saved to {output_file}")
    except FileNotFoundError:
        print(f"Error: FFmpeg not found. Make sure it's installed and in your PATH.")
    except Exception as e:
        print(f"Error converting audio: {e}")

def adjust_volume(audio, output_file, volume_change):
    """Adjusts the volume (in dB)."""
    try:
        if os.path.exists(output_file):
            if not confirm_overwrite(output_file):
                return
        adjusted_audio = audio + volume_change
        adjusted_audio.export(output_file, format="wav")
        print(f"Volume adjusted and saved to {output_file}")
    except Exception as e:
        print(f"Error adjusting volume: {e}")

def normalize_audio(audio, output_file):
    """Normalizes the audio."""
    try:
        if os.path.exists(output_file):
            if not confirm_overwrite(output_file):
                return
        normalized_audio = normalize(audio)
        normalized_audio.export(output_file, format="wav")
        print(f"Audio normalized and saved to {output_file}")
    except Exception as e:
        print(f"Error normalizing audio: {e}")

def reverse_audio(audio, output_file):
    try:
        if os.path.exists(output_file):
            if not confirm_overwrite(output_file):
                return
        reversed_audio = reverse(audio)
        reversed_audio.export(output_file, format="wav")
        print(f"Audio reversed and saved to {output_file}")
    except Exception as e:
        print(f"Error reversing audio: {e}")

def fade_in_audio(audio, output_file, duration):
    try:
        if os.path.exists(output_file):
            if not confirm_overwrite(output_file):
                return
        faded_audio = fade_in(audio, duration=duration * 1000)
        faded_audio.export(output_file, format="wav")
        print(f"Audio faded in and saved to {output_file}")
    except Exception as e:
        print(f"Error fading in audio: {e}")

def fade_out_audio(audio, output_file, duration):
    try:
        if os.path.exists(output_file):
            if not confirm_overwrite(output_file):
                return
        faded_audio = fade_out(audio, duration=duration * 1000)
        faded_audio.export(output_file, format="wav")
        print(f"Audio faded out and saved to {output_file}")
    except Exception as e:
        print(f"Error fading out audio: {e}")

def confirm_overwrite(file_path):
    """Asks the user for confirmation before overwriting a file."""
    response = input(f"File '{file_path}' already exists. Overwrite? (y/n): ")
    return response.lower() == "y"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Command-line audio editor")
    parser.add_argument("-i", "--input", required=True, help="Input audio file")
    parser.add_argument("--trim", help="Trim audio (start,end) in seconds")
    parser.add_argument("--convert", help="Convert audio to format (e.g., mp3, wav)")
    parser.add_argument("--volume", type=float, help="Adjust volume (dB, e.g., +5, -3)")
    parser.add_argument("--normalize", action="store_true", help="Normalize audio")
    parser.add_argument("--reverse", action="store_true", help="Reverse audio")
    parser.add_argument("--fade_in", type=float, help="Fade in duration in seconds")
    parser.add_argument("--fade_out", type=float, help="Fade out duration in seconds")

    args = parser.parse_args()

    audio = load_audio(args.input)

    if audio:
        print(f"Audio loaded successfully. Duration: {len(audio) / 1000} seconds")
        with tqdm(total=len(audio), desc="Processing audio", unit="ms") as pbar:
            if args.trim:
                try:
                    start, end = map(float, args.trim.split(","))
                    trim_audio(audio, "trimmed.wav", start, end)
                except ValueError:
                    print("Invalid trim format. Use start,end (e.g., 5.0,10.0)")
            elif args.convert:
                convert_audio(audio, "converted." + args.convert, args.convert)
            elif args.volume is not None:
                adjust_volume(audio, "volume_adjusted.wav", args.volume)
            elif args.normalize:
                normalize_audio(audio, "normalized.wav")
            elif args.reverse:
                reverse_audio(audio, "reversed.wav")
            elif args.fade_in:
                fade_in_audio(audio, "fade_in.wav", args.fade_in)
            elif args.fade_out:
                fade_out_audio(audio, "fade_out.wav", args.fade_out)
            pbar.update(len(audio))