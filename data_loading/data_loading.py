from typing import Tuple

import numpy as np


def load_txt_data(path: str, attribute_number: int) -> Tuple[np.ndarray, np.ndarray]:
    """
    Loads data from a text file. The following data format is assumed:
    A number of attributes of type float followed by one label of type int.
    Individual columns should be separated by whitespace.

    :param path: The path to the data txt file.
    :param attribute_number: The number of attributes that the data contains.
    :return: A tuple of (x, y):
        - x: Contains the attributes. An array of shape (n, k) where n is the
            number of rows in the txt file and k is the 'attribute_number'.
        - y: Contains the mapped class labels corresponding to x. An array of shape (n,).
    """

    data = np.loadtxt(path)

    # Split data into attributes and labels
    x = data[:, :attribute_number]
    y_labels = data[:, -1]

    # Map labels to class indexes
    [_, y] = np.unique(y_labels, return_inverse=True)

    return x, y
