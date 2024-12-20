from rembg import remove
from PIL import Image
import io

def remove_background(input_bytes):
    input_image = Image.open(io.BytesIO(input_bytes))
    output_image = remove(input_image)

    # Save the output image to an in-memory file
    output_bytes = io.BytesIO()
    output_image.save(output_bytes, format='PNG')
    output_bytes.seek(0)  # Move the cursor to the start of the BytesIO object
    print("background done......................")
    return output_bytes.getvalue()
    