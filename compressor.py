import sys
import os
import tarfile
import zipfile
from datetime import datetime

def compress_folder(folder_path, compress_type):
    try:
        if compress_type == 'zip':
            with zipfile.ZipFile(f'{folder_path}_{datetime.now().strftime("%Y_%m_%d")}.zip', 'w') as zipf:
                for root, dirs, files in os.walk(folder_path):
                    for file in files:
                        zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), folder_path))
            print("Compression successful.")
        elif compress_type == 'tar':
            with tarfile.open(f'{folder_path}_{datetime.now().strftime("%Y_%m_%d")}.tar', 'w') as tar:
                tar.add(folder_path, arcname=os.path.basename(folder_path))
            print("Compression successful.")
        elif compress_type == 'tgz':
            with tarfile.open(f'{folder_path}_{datetime.now().strftime("%Y_%m_%d")}.tar.gz', 'w:gz') as tar:
                tar.add(folder_path, arcname=os.path.basename(folder_path))
            print("Compression successful.")
        else:
            print("Invalid compression type. Please choose from 'zip', 'tar', or 'tgz'.")
    except Exception as e:
        print(f"Compression failed: {e}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python compressor.py <folder_path> <compression_type>")
        sys.exit(1)

    folder_path = sys.argv[1]
    compress_type = sys.argv[2]

    compress_folder(folder_path, compress_type)

if __name__ == "__main__":
    main()