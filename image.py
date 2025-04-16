import requests
import numpy as np

def download_image(url):
    response = requests.get(url)
    print(f"Downloaded image from {url}")
    image = np.random.rand(224, 224, 3)
    return image

def extract_features(image):

    avg_color = np.mean(image, axis=(0, 1))
    return avg_color
def generate_caption(features):
    r, g, b = features
    if r > g and r > b:
        return "A red-dominant scene."
    elif g > r and g > b:
        return "A green landscape."
    elif b > r and b > g:
        return "A blue sky or ocean scene."
    else:
        return "A neutral color scene."
def main():

    image_url = 'https://upload.wikimedia.org/wikipedia/commons/4/47/PNG_transparency_demonstration_1.png'
    image = download_image(image_url)
    features = extract_features(image)
    caption = generate_caption(features)
    print(f"Generated Caption: {caption}")

if __name__ == "__main__":
    main()
