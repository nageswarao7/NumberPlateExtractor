import streamlit as st
import cv2
import pytesseract
from ultralytics import YOLO
import re
import time

# Specify the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update this path as necessary

# Load YOLO model
model = YOLO('best.pt')  # Load your YOLO model

# Function to detect and extract text from number plates
def extract_number_plates(video_path):
    detected_numbers = []  # List to keep track of detected numbers
    cap = cv2.VideoCapture(video_path)
    st.write("Processing video...")

    # Create a placeholder for the output
    output_placeholder = st.empty()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Perform inference with YOLO
        results = model(frame)

        # Extract bounding boxes for detected number plates
        for box in results[0].boxes.xyxy:  # Adjust indexing based on YOLO version
            x1, y1, x2, y2 = map(int, box[:4])  # Get coordinates

            roi = frame[y1:y2, x1:x2]  # Region of Interest (ROI)

            # Use pytesseract to extract text from the number plate region
            text = pytesseract.image_to_string(roi, config='--psm 8')
            
            # Use regex to find a pattern that matches your desired format
            match = re.search(r'#?\d{2}-[A-Z]{2}-\d{2}|#?[A-Z]-\d{3}-[A-Z]{2}', text)
            if match:
                number = match.group(0)
                if number not in detected_numbers:
                    detected_numbers.append(number)  # Save the detected number
                    
                    # Update the output display with the new number
                    output_placeholder.markdown("### Detected Number Plates:")
                    
                    # Use two spaces at the end of each line for line breaks
                    output_text = "  \n".join(detected_numbers)  # Double space for line breaks
                    output_placeholder.markdown(output_text)

                    time.sleep(1)  # Delay for readability (1 second)

    cap.release()
    return detected_numbers

# Streamlit app layout
st.title("Number Plate Extraction from Video")

uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov"])

if uploaded_file is not None:
    # Save uploaded file to a temporary location
    with open("uploaded_video.mp4", "wb") as f:
        f.write(uploaded_file.read())

    st.video(uploaded_file)

    if st.button("Extract Number Plates"):
        extract_number_plates("uploaded_video.mp4")
