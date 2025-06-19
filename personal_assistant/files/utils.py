"""Utility functions for the files app."""

import mimetypes

def get_category(filename):
    """
    Determine the category of a file based on its MIME type.

    Args:
        filename (str): The name of the file.

    Returns:
        str: The category ('image', 'video', 'document', or 'other').
    """
    mime, _ = mimetypes.guess_type(filename)
    if mime:
        if mime.startswith("image/"):
            return "image"
        elif mime.startswith("video/"):
            return "video"
        elif mime.startswith("application/"):
            return "document"
    return "other"