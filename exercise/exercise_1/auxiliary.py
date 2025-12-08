import numpy as np

def get_labels(points) -> np.ndarray:
    """
    Assigns labels to points based on their quadrant:
    - Label 1 for Quadrants I and III
    - Label 0 for Quadrants II and IV
    Args:
        points (np.ndarray): Array of shape (n_samples, 2) containing the points.
    Returns:
        np.ndarray: Array of shape (n_samples,) containing the labels.
    """
    labels = []
    for point in points:
        x, y = point
        if x > 0 and y >= 0: # Quadrant I
            labels.append(1)
        elif x <= 0 and y < 0: # Quadrant III
            labels.append(1)
        elif x < 0 and y >= 0: # Quadrant II
            labels.append(0)
        elif x >= 0 and y < 0: # Quadrant IV
            labels.append(0)
        else:
            Exception("Invalid point")
    labels = np.array(labels)
    return labels

def build_design_matrix(data, w_x, w_y):
    """
    Builds a design matrix by applying the weight vectors to the input data.
    Args:
        data (np.ndarray): Input data of shape (n_samples, n_features).
        w_x (np.ndarray): Weight vector for the first neuron.
        w_y (np.ndarray): Weight vector for the second neuron.
    Returns:
        np.ndarray: Design matrix of shape (n_samples, 2) with activations.
    """
    x_mat = np.dot(data, w_x)
    y_mat = np.dot(data, w_y)
    return np.column_stack((x_mat, y_mat))