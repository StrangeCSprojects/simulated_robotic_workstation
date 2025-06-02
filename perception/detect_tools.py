import cv2

def detect_tools(preprocessed_image, min_area=1000, aspect_ratio_range=(0.2, 5.0)):
    """
    Detects contours in a preprocessed image and filters them based on shape.

    Args:
        preprocessed_image (numpy.ndarray): Grayscale and blurred image.
        min_area (int): Minimum area to consider a valid contour.
        aspect_ratio_range (tuple): (min, max) range for aspect ratio filtering.

    Returns:
        list: List of detected tool bounding boxes [(x, y, w, h), ...]
    """
    # Detect edges
    edged = cv2.Canny(preprocessed_image, 50, 150)

    # Find contours from the edge map
    contours, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    detected_tools = []

    for contour in contours:
        area = cv2.contourArea(contour)
        if area < min_area:
            continue  # Too small — likely noise

        # Bounding box of the contour
        x, y, w, h = cv2.boundingRect(contour)
        aspect_ratio = w / h if h != 0 else 0

        if not (aspect_ratio_range[0] <= aspect_ratio <= aspect_ratio_range[1]):
            continue  # Not the right shape

        detected_tools.append((x, y, w, h))

    return detected_tools
