import os
import numpy as np
import keras
from keras import layers
import tensorflow as tf
import matplotlib.pyplot as plt

tf.get_logger().setLevel('INFO') 

def filter_corrupted():
    num_skipped = 0
    # todo change these to the correct folder names
    for folder_name in ("Cat", "Dog"):
        # todo change this to the correct folder path
        folder_path = os.path.join("PetImages", folder_name)
        print('Scanning folder:', folder_name)
        for fname in os.listdir(folder_path):
            fpath = os.path.join(folder_path, fname)
            try:
                fobj = open(fpath, "rb")
                is_jfif = b"JFIF" in fobj.peek(10)
            finally:
                fobj.close()

            if not is_jfif:
                num_skipped += 1
                # Delete corrupted image
                os.remove(fpath)

    print(f"Deleted {num_skipped} images.")


def generate_dataset():
    image_size = (180, 180)
    batch_size = 128

    train_ds, val_ds = keras.utils.image_dataset_from_directory(
        "PetImages",
        validation_split=0.2,
        subset="both",
        seed=1337,
        image_size=image_size,
        batch_size=batch_size,
    )
    return train_ds, val_ds


def visualize_data(train_ds, val_ds):
    plt.figure(figsize=(10, 10))

    for images, labels in train_ds.take(1):
        print('Images:')
        # for i in range(9):
        #     print('Image:', i)
            # ax = plt.subplot(3, 3, i + 1)
            # plt.imshow(np.array(images[i]).astype("uint8"))
            # plt.title(int(labels[i]))
            # plt.axis("off")


# Running the script
# filter_corrupted()
train_ds, val_ds = generate_dataset()
print('Data: ----', train_ds)
visualize_data(train_ds, val_ds)
