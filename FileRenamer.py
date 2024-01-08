import os

def rename_files(directory, prefix='', suffix=''):
    files = os.listdir(directory)

    for file_name in files:
        if os.path.isfile(os.path.join(directory, file_name)):
            base, ext = os.path.splitext(file_name)
            new_name = f"{prefix}{base}{suffix}{ext}"
            os.rename(os.path.join(directory, file_name), os.path.join(directory, new_name))

directory_path = '/path/to/your/directory'

rename_files(directory_path, prefix='new_', suffix='_v2')
