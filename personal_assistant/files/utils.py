import mimetypes

def get_category(filename):
    mime, _ = mimetypes.guess_type(filename)
    if mime:
        if mime.startswith("image/"):
            return "image"
        elif mime.startswith("video/"):
            return "video"
        elif mime.startswith("application/"):
            return "document"
    return "other"