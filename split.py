#!/usr/bin/env python3

from pydub import AudioSegment
import os
import sys
import math

def split(filename: str, time: int = None, chunks: int = None, overlap: int = 0):
    """

    Arguments:
        filename {str} -- filename
        time {int} -- time of one part
        chunks {int} -- number of chunks
        overlap {int} -- overlap in seconds

    Returns:
        None: creates files.
    """
    if not os.path.isfile(filename):
        print(f"File {filename} does not exist.")
        sys.exit(1)

    try:
        audio = AudioSegment.from_file(filename)
    except Exception as e:
        print(f"Error loading audio file: {e}")
        sys.exit(1)

    duration_ms = len(audio)
    print(f"Audio duration: {duration_ms / 1000.0} seconds")

    if time:
        segment_duration_ms = time * 60 * 1000  # convert minutes to milliseconds
        num_parts = int(math.ceil(duration_ms / segment_duration_ms))
    elif chunks:
        segment_duration_ms = duration_ms / chunks
        num_parts = int(math.ceil(duration_ms / segment_duration_ms))
    else:
        print("No method was given.")
        sys.exit(1)

    base_filename, ext = os.path.splitext(filename)

    for i in range(num_parts):
        start = int(i * segment_duration_ms)
        end = int(start + segment_duration_ms)
        if end > duration_ms:
            end = duration_ms
        segment = audio[start:end+overlap*1000.0]

        output_filename = f"{base_filename}_part{i+1}{ext}"

        segment.export(output_filename, format=ext[1:])
        print(f"Exported {output_filename}")

if __name__ == "__main__":
    filepath = ''

    # split("test.wav", chunks=3)
    split("test.wav", time=10, overlap=30)

