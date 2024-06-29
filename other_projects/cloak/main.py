'''

    Steps to Build Invisible Cloak OpenCV Project:
        1. Import necessary packages and Initialize the camera.
        2. Store a single frame before starting the infinite loop.
        3. Detect the color of the cloth and create a mask.
        4. Apply the mask on frames.
        5. Combine masked frames together.
        6. Removing unnecessary noise from masks.

'''

# Step 1: Import Libraries

import numpy as np
import cv2
import time

# Step 2: Using the WebCam to take the Video Feed
# camCount=0
# To use webcam  enter 0 or add in path
cap = cv2.VideoCapture(0)

# two second as the camera needs time to adjust itself according to the environment
time.sleep(3)
background = 0

# Step: Capturing the background
for i in range(60):
    ret, background = cap.read()

# capturing image
background = np.flip(background, axis=1)

# Step 4: Capturing the video feed using Webcam
while (cap.isOpened()):

    ret, img = cap.read()
    if not ret:
        break

    img = np.flip(img, axis=1)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # HSV value bounds
    # Step 5: setting the values for the cloak
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])

    mask1 = cv2.inRange(hsv, lower_red, upper_red)

    lower_red = np.array([170, 120, 70])
    upper_red = np.array([180, 255, 255])

    mask2 = cv2.inRange(hsv, lower_red, upper_red)

    mask1 = mask1 + mask2

    # Step 6: Using Morphological Transformations to remove noise from the cloth and unnecessary Details.
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=2)
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8), iterations=1)

    mask2 = cv2.bitwise_not(mask1)

    # Step 7: Combining the masks and showing them in one frame
    res1 = cv2.bitwise_and(background, background, mask=mask1)
    res2 = cv2.bitwise_and(img, img, mask=mask2)

    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)
    cv2.imshow('Invisible Cloak', final_output)

    if cv2.waitKey(10) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
