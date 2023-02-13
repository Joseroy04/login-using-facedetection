

import io
from PIL import Image


import base64
import io
from PIL import Image
import numpy as np
import face_recognition
def convert_base64_to_image(base64_data):
    # Remove the data header from the base64 data
    base64_data = base64_data.split(',')[1]
    # Decode the base64 data to binary
    binary_data = base64.b64decode(base64_data)
    # Open the binary data as an image file
    image = Image.open(io.BytesIO(binary_data))
    # //rgb
    rgb_image = image.convert('RGB')

    # conver to np array    
    np_image = np.array(rgb_image)
    # Return the image
    val = face_recognition.face_encodings(np_image)
    return val


def convert_to_jpeg(input_data):
    # Convert the input data to a bytes object
    input_data = bytes(input_data, 'utf-8')
    # Open the input data as a binary stream
    input_stream = io.BytesIO(input_data)
    # Load the image from the binary stream
    image = Image.open(input_stream)
    # Convert the image to JPEG format
    output_stream = io.BytesIO()
    image.convert("RGB").save(output_stream, "JPEG")
    # Get the JPEG data from the output stream
    jpeg_data = output_stream.getvalue()
    return jpeg_data