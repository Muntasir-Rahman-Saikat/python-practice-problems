import os
import time

def watch_directory(path):
    print(f"Watching directory: {path}")
    existing_files = set(os.listdir(path))

    while True:
        time.sleep(8)  # check every 8 seconds
        current_files = set(os.listdir(path))

        # detect new .txt files
        new_files = [f for f in current_files - existing_files if f.endswith('.txt')]

        if new_files:
            for file in new_files:
                print(f"New text file detected: {file}")

        existing_files = current_files

# Example usage
directory_path = "/home/wsl-ubuntu/Python_task/python-practice-problems/advanced-level/problem-7"  # change path as needed
watch_directory(directory_path)
