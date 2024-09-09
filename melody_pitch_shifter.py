import argparse
import librosa
import soundfile as sf

# Function to process the audio file and apply pitch shifting
def modify_melody(input_file, n_steps=4):
    # Load WAV file
    y, sr = librosa.load(input_file, sr=None)  # sr=None to preserve the original sampling rate

    # Extract melody - Using harmonic component for simplicity
    harmonic, _ = librosa.effects.hpss(y)

    # Shift pitch by the number of semitones (default 4)
    pitch_shifted = librosa.effects.pitch_shift(y=harmonic, sr=sr, n_steps=n_steps)

    # Generate output file name
    output_file = f"modified_{input_file}"

    # Save the pitch-shifted audio to a WAV file
    sf.write(output_file, pitch_shifted, sr)

    print(f"Melody has been modified by {n_steps} semitones and saved to {output_file}")

# Command-line interface setup
if __name__ == "__main__":
    # Argument parser setup
    parser = argparse.ArgumentParser(description="Modify the melody of a WAV file by shifting the pitch.")
    parser.add_argument("input_file", type=str, help="Input WAV file name")
    parser.add_argument("--n_steps", type=int, default=4, help="Number of semitones to shift the pitch (default is 4)")

    # Parse arguments
    args = parser.parse_args()

    # Modify the melody with the given inputs
    modify_melody(args.input_file, args.n_steps)
