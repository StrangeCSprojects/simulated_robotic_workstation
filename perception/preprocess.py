import cv2

def preprocess_image(image):
    """
    Converts an image to grayscale and applies Gaussian blur.

    Args:
        image (numpy.ndarray): Original color image.

    Returns:
        preprocessed (numpy.ndarray): Grayscale, blurred image.
    """
    # Convert to grayscale to simplify processing
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(grayscale, (5, 5), 0)

    return blurred

