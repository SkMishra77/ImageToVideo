import cv2
import os
import glob

def create_video_from_images(image_directory, output_filename):
    # Get a list of PNG image files in the specified directory
    image_files = sorted(glob.glob(os.path.join(image_directory, "*.jpg")))

    frames = (60//len(image_files))

    if not image_files:
        print("No PNG image files found in the directory.")
        return

    # Read the first image to determine its size
    first_image = cv2.imread(image_files[0])
    height, width, _ = first_image.shape

    # Initialize VideoWriter
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(output_filename, fourcc, 1, (width, height))

    # Resize and write each image to the video
    for image_file in image_files:
        image = cv2.imread(image_file)

        # Resize the image to the target dimension
        if (height, width) != target_dimension:
            image = cv2.resize(image, (width, height))

        for _ in range(frames):
            out.write(image)

    # Release the VideoWriter
    out.release()
    print(f"Video saved as {output_filename}")

# Example usage:
if __name__ == "__main__":
    fileNames = os.listdir("output")

    for file in fileNames:
        input_path = os.path.join('output', file)
        output_path = os.path.join('videoOut', file) + ".mp4"
        target_dimension = (1280, 720)
        create_video_from_images(input_path, output_path)

