


# Image to Video Converter

This Python script converts a series of PNG images into a video file, where each image is displayed for exactly 5 seconds. The script utilizes the OpenCV library to create the video. The images should be named numerically (e.g., `1.png`, `2.png`, ...) and placed in a directory. The script then sorts and processes the images, ensuring that each image is shown for the desired duration in the final video.

## Features

- Converts a sequence of PNG images into a video
- Customizable frame duration (5 seconds per image)
- Automatically sorts images based on their numeric filenames
- Supports Windows file paths

## Getting Started

### Prerequisites

- Python 3.x
- OpenCV library (`pip install opencv-python`)

### Usage

1. Clone this repository to your local machine or download the script directly.
   
   ```bash
   git clone https://github.com/yourusername/image-to-video-converter.git
2. Place your PNG images (e.g., 1.png, 2.png, ...) in a directory of your choice.

3. Open the convert_images_to_video.py script in a text editor.

4. Update the image_directory variable to point to the directory containing your PNG images. For example:
   ```bash
   image_directory = "C:\\path\\to\\your\\images\\directory"
5. Run the script using the following command:
     ```bash
     python convert_images_to_video.py
6. The script will generate an output video named output_video.mp4 in the same directory as the script.
## Customization
You can adjust the frame_duration variable in the script to change the duration each image is displayed in the video. The default is set to 5 seconds (5000 milliseconds).

Author
Created by **SANAT KUMAR MISHRA**.
