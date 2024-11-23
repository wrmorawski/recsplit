#!/usr/bin/env python3

import argparse
from pydub import AudioSegment
import os
import sys
import math

def split():
    parser = argparse.ArgumentParser(description='Split an audio file into parts.')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-t', '--time', type=float, help='Duration in minutes for each part')
    group.add_argument('-n', '--number', type=int, help='Number of parts to split into')
    parser.add_argument('filename', help='Input audio file name')
    args = parser.parse_args()

    if not os.path.isfile(args.filename):
        print(f"File {args.filename} does not exist.")
        sys.exit(1)

    try:
        audio = AudioSegment.from_file(args.filename)
    except Exception as e:
        print(f"Error loading audio file: {e}")
        sys.exit(1)

    duration_ms = len(audio)
    print(f"Audio duration: {duration_ms / 1000.0} seconds")

    if args.time:
        segment_duration_ms = args.time * 60 * 1000  # convert minutes to milliseconds
        num_parts = int(math.ceil(duration_ms / segment_duration_ms))
    else:
        num_parts = args.number
        segment_duration_ms = duration_ms / num_parts

    base_filename, ext = os.path.splitext(args.filename)

    for i in range(num_parts):
        start = int(i * segment_duration_ms)
        end = int(start + segment_duration_ms)
        if end > duration_ms:
            end = duration_ms

        segment = audio[start:end]

        output_filename = f"{base_filename}_part{i+1}{ext}"

        segment.export(output_filename, format=ext[1:])
        print(f"Exported {output_filename}")

if __name__ == "__main__":
    split()
