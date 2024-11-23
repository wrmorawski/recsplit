import os
import sys
from pydub import AudioSegment

def convert(filename, target_format):
    supported_formats = ['wav', 'mp3', 'm4a']

    if not os.path.isfile(filename):
        print(f"Error: File '{filename}' does not exist.")
        sys.exit(1)

    if target_format in supported_formats:
        base, input_format = os.path.splitext(filename)
        output_file = base + '.' + target_format
        input_format = input_format[1:]
        try:
            if input_format in supported_formats:
                print(f"Converting '{filename}' to '{output_file}'...")

                audio = AudioSegment.from_file(filename, format='m4a')
                audio.export(output_file, format='wav')
                print(f"Conversion successful: '{output_file}' created.")
            else:
                print(f'input format {input_format} is not supported.')
        except Exception as e:
            print(f"Error during conversion: {e}")
            sys.exit(1)
    else:
        print(f'target format {target_format} is not supported.')
        sys.exit(1)

if __name__ == '__main__':
    convert("test.m4a", 'wav')