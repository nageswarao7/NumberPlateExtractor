Vehicle Number Plate Detection and OCR
This project implements a Vehicle Number Plate Detection system that uses YOLOv8 for real-time object detection and Optical Character Recognition (OCR) to extract alphanumeric characters from the detected number plates. It demonstrates the use of computer vision, deep learning, and OCR technologies for practical applications such as vehicle tracking and automated license plate recognition (ALPR).

Key Features:
Real-time number plate detection using YOLOv8 model.
Text extraction from the number plate using Tesseract OCR.
Accuracy and efficiency in detecting alphanumeric characters.
Designed for automated vehicle recognition applications.
Table of Contents:
Installation
Usage
Requirements
How it Works
License
Installation
To run this project, you'll need to install some dependencies.

Clone the repository:

bash
Copy code
git clone https://github.com/nageswarao7/NumberPlateExtractor.git
cd NumberPlateExtractor
Install the required libraries:

You can install the required dependencies via pip. It’s recommended to use a virtual environment.

bash
Copy code
pip install -r requirements.txt
Install Tesseract OCR:

For Windows: Download Tesseract from here and follow the installation instructions. Make sure to add it to your system’s PATH.

For Linux: Run the following command to install Tesseract:

bash
Copy code
sudo apt install tesseract-ocr
Usage
Prepare the images: The system accepts vehicle images with clear number plates.

Run the detection and OCR extraction:

Once the system is set up, you can start by running the script:

bash
Copy code
python detect_and_extract.py --image <image_path>
Replace <image_path> with the path to your image containing the vehicle's number plate.

Example:

bash
Copy code
python detect_and_extract.py --image vehicle.jpg
Output: The system will display:

The original image with the detected number plate outlined.
The extracted text from the number plate.
Requirements
This project requires the following Python libraries:

opencv-python: For image processing.
yolov8: For object detection using YOLOv8 model.
pytesseract: For OCR text extraction.
imutils: For image resizing and manipulation.
torch (for YOLOv8 and deep learning models).
numpy: For numerical computations.
All dependencies can be installed using the requirements.txt file.

How it Works
1. YOLOv8 for Number Plate Detection:
YOLOv8 (You Only Look Once) is a real-time object detection model that is used to identify the number plate within a vehicle image. The model detects the region of interest (ROI) containing the number plate with high accuracy and efficiency.

Training YOLOv8: If the pre-trained model doesn’t meet your requirements, you can train YOLOv8 on a custom dataset containing vehicle images with visible number plates.
2. OCR for Text Extraction:
Once the number plate is detected, Tesseract OCR is used to extract the alphanumeric characters from the number plate region. Tesseract is an open-source OCR engine that works well for extracting text from images.

Text Preprocessing: The detected number plate image is processed (thresholding, resizing, etc.) before being fed into the OCR engine for better accuracy.
Example
Input Image:

Output:
Detected number plate area in the image and video.
Extracted text from the number plate: AB123CD
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
YOLOv8 for object detection.
Tesseract OCR for text extraction.
OpenCV for image processing.
imutils for easier image manipulation.
