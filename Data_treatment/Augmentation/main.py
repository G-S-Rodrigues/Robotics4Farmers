from utils import *


def run_yolo_augmentor():
    """
    Run the YOLO augmentor on a set of images.

    This function processes each image in the input directory, applies augmentations,
    and saves the augmented images and labels to the output directories.

    """
    imgs = [img for img in os.listdir(CONSTANTS["inp_img_pth"]) if is_image_by_extension(img)]
    
    for img_num, img_file in enumerate(imgs):
        print(f"{img_file}- is processing...\n")
        image, key_points, aug_file_name = get_input_data(img_file)
        aug_img, aug_label = get_augmented_results(image, key_points)
        if len(aug_img) and len(aug_label):
            save_augmentation(aug_img, aug_label, aug_file_name)


if __name__ == "__main__":
    run_yolo_augmentor()