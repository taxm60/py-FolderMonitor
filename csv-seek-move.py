import os
import shutil
import time
import getpass   #get current username

def move_csv_files(source_folder, destination_folder):
    # Check if destination folder exists, create if it doesn't
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    # List all files in the source folder
    files = os.listdir(source_folder)
    
    # Iterate through each file
    for file in files:
        # filename is like  (f***.csv) OR (f***.ods)
        if file.startswith('f') and (file.endswith('.csv') or file.endswith('.ods')):
            # Construct full paths for source and destination            
            source_file = os.path.join(source_folder, file)
            destination_file = os.path.join(destination_folder, file)
            
            # Move the file to the destination folde
            try:
                shutil.move(source_file, destination_file)
                #print(f"[O] Moving: {file} -> {destination_folder}")
                print(f"\033[92m[O] Moving: {file} -> {destination_folder}\033[0m")  # Green color for success
            except PermissionError:
                #print(f"[X] PermissionErr: Moving {file} ; keep retry...")
                print(f"\033[91;1m[X] PermissionErr: Moving {file} ; keep retry...\033[0m")  # Light red color for PermissionError
                
            except Exception as e:
                print(f"[X] Unexpected error: {e}")

def main():
    username = getpass.getuser()
    source_folder = os.path.join(r"C:\Users", username, "Downloads")
    destination_folder = os.path.join(source_folder, "done")
    print("------")    
    print("Monitor : " , source_folder)
    print("Target  : " , destination_folder)
    print("FileName: (f*.csv) || (f*.ods)")
    print("------")
    
    while True:
        move_csv_files(source_folder, destination_folder)
        # Check every 2 seconds (adjust as needed)
        time.sleep(3)

if __name__ == "__main__":
    main()
