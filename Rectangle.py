import cv2
import numpy as np

# Create a black image
image = np.zeros((500, 500, 3), dtype=np.uint8)

# Draw a green rectangle
cv2.rectangle(image, (100, 100), (400, 300), (0, 255, 0), 3)

# Display the image
cv2.imshow("Rectangle", image)

# Wait until a key is pressed
cv2.waitKey(0)

# Close the window
cv2.destroyAllWindows()