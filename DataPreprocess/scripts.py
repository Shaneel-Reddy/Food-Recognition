import os
import shutil

# Define paths
dataset_paths = [
    "datasets/dataset_1/training",
    "datasets/dataset_1/validation",
    "datasets/dataset_2/training",
    "datasets/dataset_2/validation",
    "datasets/dataset_3/images"
]

output_dir = "datasets/merged_dataset"
image_dir = os.path.join(output_dir, "images")
label_dir = os.path.join(output_dir, "labels")

os.makedirs(image_dir, exist_ok=True)
os.makedirs(label_dir, exist_ok=True)

# Function to move images and labels
def move_files(src_dir):
    for root, _, files in os.walk(src_dir):
        for file in files:
            if file.endswith(('.jpg', '.png')):
                shutil.copy(os.path.join(root, file), os.path.join(image_dir, file))
            elif file.endswith('.txt'):
                shutil.copy(os.path.join(root, file), os.path.join(label_dir, file))

# Process all datasets
for dataset in dataset_paths:
    move_files(dataset)

print("✅ Images and labels merged into datasets/merged_dataset")
