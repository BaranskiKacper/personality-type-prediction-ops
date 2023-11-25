import os

import cv2
import numpy as np
import pandas as pd
import unidecode
from PIL import Image

# Base directory
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(CURRENT_DIR)

# Directory for storing CSV files.
STATIC_CSV_DIR = os.path.join(BASE_DIR, "static", "csv")
RECORDS_CSV = os.path.join(STATIC_CSV_DIR, "records.csv")
RECORDS_CLEANED_CSV = os.path.join(STATIC_CSV_DIR, "records_cleaned.csv")
RECORDS_CLEANED_PROCESSED_CSV = os.path.join(STATIC_CSV_DIR, "records_cleaned_processed.csv")


def image_exists(row: pd.Series, directory: str) -> bool:
    """Check if an image file exists in a given directory based on a DataFrame row.

    Args:
        row (pd.Series): A row from a DataFrame containing image names.
        directory (str): The directory path where the image files are located.

    Returns:
        bool: True if the image file exists, False otherwise.
    """
    image_path = os.path.join(directory, row["name"] + ".jpg")
    return os.path.isfile(image_path)


def save_image(image: np.ndarray, filename: str, directory: str) -> None:
    """Save an image to a specified directory with a given filename.

    Args:
        image (np.ndarray): The image to be saved.
        filename (str): The name of the file to save the image as.
        directory (str): The directory path where the image will be saved.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_path = os.path.join(directory, filename)
    cv2.imwrite(file_path, image)


def rename_to_ascii_img(directory: str) -> None:
    """Rename all image files in a directory to ASCII, replacing non-ASCII characters.

    Args:
        directory (str): The directory path containing the image files.
    """
    ascii_limit = 128  # Maximum ordinal value for ASCII characters

    for filename in os.listdir(directory):
        if not all(ord(char) < ascii_limit for char in filename):
            ascii_filename = unidecode.unidecode(filename).replace(" ", "_")
            original_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, ascii_filename)
            os.rename(original_path, new_path)
            print(f"Renamed '{filename}' to '{ascii_filename}'")


def rename_to_ascii_csv(directory: str) -> None:
    """Convert 'name' column entries in a CSV file to ASCII and save the changes.

    Args:
        directory (str): The directory path of the CSV file.
    """
    df = pd.read_csv(directory)
    df["name"] = df["name"].apply(lambda name: unidecode.unidecode(name).replace(" ", "_"))
    df.to_csv(directory, index=False)


def find_image_extremes(directory: str) -> tuple[tuple[int, int], tuple[int, int]]:
    """Find the smallest and largest images in a directory.

    Args:
        directory (str): The directory path containing the image files.

    Returns:
        Tuple[Tuple[int, int], Tuple[int, int]]: The dimensions of the smallest and largest images.
    """
    min_dim = None
    max_dim = None
    for filename in os.listdir(directory):
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            with Image.open(os.path.join(directory, filename)) as img:
                width, height = img.size
                if min_dim is None or (width * height < min_dim[0] * min_dim[1]):
                    min_dim = (width, height)
                if max_dim is None or (width * height > max_dim[0] * max_dim[1]):
                    max_dim = (width, height)
    return min_dim, max_dim


def replace_space_with_underscore_image(directory: str) -> None:
    """Rename image files by replacing spaces with underscores.

    Args:
        directory (str): The directory containing the images.
    """
    for filename in os.listdir(directory):
        if " " in filename:
            new_filename = filename.replace(" ", "_")
            old_file_path = os.path.join(directory, filename)
            new_file_path = os.path.join(directory, new_filename)
            os.rename(old_file_path, new_file_path)
            print(f"Renamed '{filename}' to '{new_filename}'")


def replace_space_with_underscore_csv(csv_file_path: str) -> None:
    """Replace spaces with underscores in the 'name' column of a CSV file.

    Args:
        csv_file_path (str): The path to the CSV file.
    """
    try:
        df = pd.read_csv(csv_file_path)
        if "name" in df.columns:
            df["name"] = df["name"].str.replace(" ", "_")
            df.to_csv(csv_file_path, index=False)
            print(f"CSV file '{csv_file_path}' has been modified and overwritten.")
        else:
            print("Column 'name' not found in the CSV file.")

    except Exception as e:
        print(f"An error occurred: {e}")
