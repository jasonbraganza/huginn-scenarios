from pathlib import Path
import shutil


downloads_folder = Path('/path/to/downloaded/episode/directory/')
destination_folder = Path('/path/to/destination/directory/')

for audio_file in downloads_folder.iterdir():
    if audio_file.suffix == '.mp3':
        original_name = audio_file.stem
        original_name = original_name.split('-')[2:]
        episode_number, raw_file_name = f'CNPE{original_name[0]}', (' '.join(original_name[1:])).title()

        new_file_name = episode_number+ ' - ' +raw_file_name +audio_file.suffix

        shutil.move(downloads_folder/audio_file, destination_folder/new_file_name)
