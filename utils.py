import os
import math
from pydub import AudioSegment

def check_audio_length(filename):
    audio = AudioSegment.from_file(filename)
    duration_s = len(audio) / 1000
    duration_min = math.floor(duration_s / 60.0)
    print(f'{filename} audio duration is  {duration_min} min and {math.ceil(duration_s % 60)} seconds')

if __name__ == '__main__':
    check_audio_length('test_part2.wav')