import csv
import os
import shutil

# Define the directories to sort the photos into
dir1 = 'directory1'
dir2 = 'directory2'
dir3 = 'directory3'

# Create the directories if they don't exist already
os.makedirs(dir1, exist_ok=True)
os.makedirs(dir2, exist_ok=True)
os.makedirs(dir3, exist_ok=True)

# Read the mapping from the CSV file
mapping = {}
with open('photo_mapping.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        photo_name, dest_dir = row
        mapping[photo_name] = dest_dir

# Loop through each photo in the directory
for photo_name in os.listdir('.'):
    # If the file is not a photo, skip it
    if not photo_name.endswith('.jpg'):
        continue
    
    # If the photo is in the mapping, move it to the corresponding directory
    if photo_name in mapping:
        dest_dir = mapping[photo_name]
        shutil.move(photo_name, dest_dir)
        print(f"Moved {photo_name} to {dest_dir}")
        
# Save the mapping between photo names and destination directories in a CSV file named photo_mapping.csv.
# The file should have two columns: the first column should contain the photo names (including the .jpg extension), 
# and the second column should contain the corresponding destination directories (directory1, directory2, or directory3 in this case).  
#
# Place the CSV file in the same directory as the photos and the Python script. 
# Then, run the script by typing python sort_photos.py in the command prompt or terminal, and hit Enter. 
# The script should move the photos to the correct directories and print a message for each file that it moves.
