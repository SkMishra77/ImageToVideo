import cv2
import os

# Specify the path to the directory containing the images
image_directory = "C:\\Users\\pc\\Documents\\images"

# Get a list of image filenames sorted numerically
image_filenames = sorted(
    [filename for filename in os.listdir(image_directory) if filename.lower().endswith(".png")],
    key=lambda x: int(x.split(".")[0])
)
print(image_filenames)

# Set the frame rate and duration for each image (in milliseconds)
frame_duration = 5000  # 5 seconds per image in milliseconds

# Get the dimensions of the first image
first_image = cv2.imread(os.path.join(image_directory, image_filenames[0]))
height, width, layers = first_image.shape

# Create a VideoWriter object to save the video
video_filename = "Modern.mp4"
fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # Video codec
out = cv2.VideoWriter(video_filename, fourcc, 1, (width, height))  # Set frame rate to 1 fps

# Loop through each image and add it to the video
for image_filename in image_filenames:
    image_path = os.path.join(image_directory, image_filename)
    image = cv2.imread(image_path)
    
    # Repeat each frame for the desired number of frames to achieve the desired duration
    for _ in range(frame_duration // 1000):
        out.write(image)

# Release the VideoWriter
out.release()

print(f"Video saved as {video_filename}")
