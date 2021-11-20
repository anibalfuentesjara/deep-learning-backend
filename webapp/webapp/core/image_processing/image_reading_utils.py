from PIL import Image
import base64
import io
import numpy as np


def base64_to_numpy(image_base64: str):
    image_base64 = image_base64.split(',')[-1]
    base64_decoded = base64.b64decode(image_base64)
    image = Image.open(io.BytesIO(base64_decoded))
    return np.array(image)
