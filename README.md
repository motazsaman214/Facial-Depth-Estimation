# Facial Depth Estimation

This repository contains a Python script that estimates the depth of a face using OpenCV and cvzone. The code utilizes facial landmarks to calculate the distance between the eyes, and then uses that information to estimate the depth.

## Requirements

- Python 3.x
- OpenCV
- cvzone

Install the required packages using:
 
```bash
pip install -r requirements.txt
```
## Usage :
- Run the script:

        python face_depth_estimation.py
        
- The script will open a window displaying the live camera feed.
- The estimated depth will be displayed on the image in centimeters.

## How it works
- The script uses the `FaceMeshDetector` from `cvzone` to detect facial landmarks.
- It calculates the distance between the left and right eye corners.
- This distance is then used to estimate the depth using a pre-defined focal length and a known width of a face.

## Notes
- The script assumes a known width of the face (6.3 cm).
- The accuracy of the depth estimation depends on the quality of the camera and the lighting conditions.
- The script uses a pre-defined focal length, which may need to be calibrated for optimal results.

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.


