import os
import time
import argparse

from PIL import Image

starting_directory = os.getcwd()
filename_prefix = 'IMG'
extension = '.jpg'


def parse() -> str:
    parser = argparse.ArgumentParser(description='Renamer - recursively rename all images in current dir '
                                                 'and subdirectories by given extension.'
                                                 'Ex.: path_to_renamer\\renamer.exe -ext .jpeg')
    parser.add_argument('-ext', '--extension',
                        type=str,
                        default='.jpg',
                        help='input file extension')
    args = parser.parse_args()
    return args.extension


def is_corrupted(file_dir, image_file) -> bool:
    try:
        with Image.open(os.path.join(file_dir, image_file)) as img:
            img.verify()
        return False
    except Exception as exception:
        print(exception)
        return True


if __name__ == '__main__':
    extension = extension if not parse() else parse()
    print(extension)
    for path, dirs, files in os.walk(starting_directory):
        # recursively walk all sub dirs starting from current working dir
        for filename in files:
            if filename.lower().endswith(extension) and not is_corrupted(path, filename):
                try:
                    created_at_timestamp = time.ctime(os.path.getmtime(os.path.join(path, filename)))
                except OSError as e:
                    continue
                created_at = time.strptime(created_at_timestamp)  # parsed to date n time object
                timestamp_string = (f'_{created_at.tm_year:04}{created_at.tm_mon:02}{created_at.tm_mday:02}'
                                    f'_{created_at.tm_hour:02}{created_at.tm_min:02}{created_at.tm_sec:02}')

                if timestamp_string not in filename:
                    old_filename_wo_ext = filename[:-len(extension)]

                    revised_filename = (f'{filename_prefix}'
                                        f'{timestamp_string}'
                                        f'_{old_filename_wo_ext}{extension}')
                    os.rename(os.path.join(path, filename), os.path.join(path, revised_filename))
