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

# Example usage
if __name__ == "__main__":
    import sys
    img_path = "tools/sample_workspace.jpg"
    image = cv2.imread(img_path)

    if image is None:
        raise FileNotFoundError(f"Image not found: {img_path}")

    processed = preprocess_image(image)

    # Show the processed image
    cv2.imshow("Preprocessed Image", processed)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
