import cv2
from perception.preprocess import preprocess_image
from perception.detect_tools import detect_tools

# Load and preprocess the image
image = cv2.imread("tools/sample_workspace.jpg")
processed = preprocess_image(image)

# Detect tools
tool_boxes = detect_tools(processed)

# Draw results
for (x, y, w, h) in tool_boxes:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Show the result
cv2.imshow("Detected Tools", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
