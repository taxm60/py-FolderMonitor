import os
import shutil
import time

def move_csv_files(source_folder, destination_folder):
    # Check if destination folder exists, create if it doesn't
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    # List all files in the source folder
    files = os.listdir(source_folder)
    
    # Iterate through each file
    for file in files:
        if file.endswith('.csv'):
            # Construct full paths for source and destination
            source_file = os.path.join(source_folder, file)
            destination_file = os.path.join(destination_folder, file)
            
            # Move the file to the destination folder
            shutil.move(source_file, destination_file)
            print(f"Moved {file} to {destination_folder}")

def main():
    source_folder = r"C:\Users\jack\Downloads"
    destination_folder = os.path.join(source_folder, "done")
    
    while True:
        move_csv_files(source_folder, destination_folder)
        # Check every 2 seconds (adjust as needed)
        time.sleep(2)

if __name__ == "__main__":
    main()
