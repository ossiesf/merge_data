import os
import shutil
import random

# Define source and destination
source_path = ''
train_path = ''
valid_path = ''

validation_split = 0.2 # 20% seems standard

# Initially for single label folders with 60+ images specific to one category
# Set a list to iterate over
folders = []

def find_folder_paths():
    folder_paths = {}
    for folder in folders:
        folder_path = os.path.join(source_path, folder)
        if os.path.isdir(folder_path):
            folder_paths[folder] = folder_path
    return folder_paths

folder_paths = find_folder_paths()

for folder in folder_paths.values():
    print('Folder path: ' + folder)
    images = os.listdir(folder)
    num_valid = int(len(images) * validation_split)
    selected_images = random.sample(images, num_valid)
    
    # Make the directories, exist_ok set to true avoids an error if the folder already exists
    os.makedirs(train_path, exist_ok=True)
    os.makedirs(valid_path, exist_ok=True)

    # Iterate over the images set aside as the validation set to the valid set location
    for image in selected_images:
        try:
            shutil.move(os.path.join(folder, image),  os.path.join(valid_path, image))
            # Remove this item from the list, as we don't want it in both folders (train / valid)
            images.remove(image)
        except Exception as e:
            print(f"Error moving to valid: {e}")    
    # Iterate over the remaining images and move them to the training path
    for image in images:
        try:
            shutil.move(os.path.join(folder, image), os.path.join(train_path, image))
        except Exception as e:
            print('Error moving to train: ', {e})