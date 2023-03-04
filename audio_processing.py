from pydub import AudioSegment
import math
import os

def split_audio_file(input_path, output_dir):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Load the audio file
    full_audio = AudioSegment.from_file(input_path)

    # PyDub handles time in milliseconds
    ten_minutes = 10 * 60 * 1000

    # Calculate the number of chunks needed
    num_chunks = math.ceil(len(full_audio) / ten_minutes)

    # Split the audio into chunks and export each chunk
    for i in range(num_chunks):
        print("Audio part ", i+1)
        start_time = i * ten_minutes
        end_time = (i + 1) * ten_minutes
        chunk = full_audio[start_time:end_time]
        output_path = os.path.join(output_dir, f"{os.path.splitext(os.path.basename(input_path))[0]}_{i+1}.mp3")
        chunk.export(output_path, format="mp3")
