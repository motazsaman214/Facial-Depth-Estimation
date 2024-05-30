# Import necessary libraries
import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector

# Define constants
KNOWN_WIDTH = 6.3  # Known width of the face in centimeters
FOCAL_LENGTH = 840  # Pre-defined focal length

# Initialize the camera
cap = cv2.VideoCapture(1)

# Create a FaceMeshDetector object
detector = FaceMeshDetector(maxFaces=1)

# Main loop
while True:
    # Read a frame from the camera
    success, img = cap.read()

    # Detect faces and landmarks
    img, faces = detector.findFaceMesh(img, draw=False)

    # Process if a face is detected
    if faces:
        # Get the first face
        face = faces[0]

        # Get the left and right eye corner points
        pointLeft = face[145]
        pointRight = face[374]

        # --- Drawing (Commented for Clarity) ---
        # Draw a line between the eye corners
        # cv2.line(img, pointLeft, pointRight, (0, 200, 0), 3)
        # Draw a circle on the left eye corner
        # cv2.circle(img, pointLeft, 5, (255, 0, 255), cv2.FILLED)
        # Draw a circle on the right eye corner
        # cv2.circle(img, pointRight, 5, (255, 0, 255), cv2.FILLED)

        # Calculate the distance between the eye corners
        w, _ = detector.findDistance(pointLeft, pointRight)

        # --- Debugging (Commented for Clarity) ---
        # Print the distance between the eye corners
        # print(w)

        # --- Finding Focal Length (Commented for Clarity) ---
        # Define a known distance between the camera and the face
        # d = 50
        # Calculate the focal length using the formula: f = (w * d) / W
        # f = (w * d) / KNOWN_WIDTH
        # Print the calculated focal length
        # print(f)

        # Calculate the depth using the formula: d = (W * f) / w
        depth = (KNOWN_WIDTH * FOCAL_LENGTH) / w

        # Display the estimated depth on the image
        cvzone.putTextRect(img, f'Depth: {int(depth)}cm',
                           (face[10][0] - 100, face[10][1] - 50),
                           scale=2)

    # Display the output image
    cv2.imshow("Image", img)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the camera and destroy all windows
cap.release()
cv2.destroyAllWindows()