import os

# Define dataset paths
food101_path = "datasets/dataset_1/"
uec256_path = "datasets/dataset_2/"
food11_path = "datasets/dataset_3/"
food= "datasets/merged_dataset/"

def count_images(directory):
    image_count = sum([len(files) for _, _, files in os.walk(directory) if any(f.endswith(('.jpg', '.png')) for f in files)])
    return image_count

# Count images in each dataset
food101_count = count_images(food101_path)
uec256_count = count_images(uec256_path)
food11_count = count_images(food11_path)
food= count_images(food)

print(f"📌 Food101: {food101_count} images")
print(f"📌 UEC256: {uec256_count} images")
print(f"📌 Food11: {food11_count} images")
print(f"✅ Total Images: {food101_count + uec256_count + food11_count}")
print(f"✅ Total Images merged: {food}")
