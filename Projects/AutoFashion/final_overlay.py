import numpy as np
from PIL import Image
from io import BytesIO
import random 

def resize_person_image(person):
    width, height = person.size
    if width == 350*2 and height == 500*2:   #Cowboy
        person = person.resize((350, 500), Image.LANCZOS)         
        print(f"Resized to 300x300 due to size being {width}x{height}")
    elif width == 800*2 and height == 800*2: #Rohit Jersey
        person = person.resize((600, 600), Image.LANCZOS) 
        print(f"Resized to 400x400 due to size being {width}x{height}")
    elif width == 464*2 and height == 1000*2: #Racing Suit
        person = person.resize((278, 550), Image.LANCZOS) 
        print(f"Resized to 400x400 due to size being {width}x{height}")
    elif width == 1508*2 and height == 2133*2: #Pink Sherwani
        person = person.resize((450, 600), Image.LANCZOS) 
        print(f"Resized to 400x400 due to size being {width}x{height}")
    elif width == 736*2 and height == 1104*2: #Black Sherwani
        person = person.resize((500, 500), Image.LANCZOS) 
        print(f"Resized to 400x400 due to size being {width}x{height}")
    elif width == 3277*2 and height == 4096*2: #tcs_f1
        person = person.resize((520, 650), Image.LANCZOS) 
        print(f"Resized to 400x400 due to size being {width}x{height}")
    elif width == 400*2 and height == 600*2: #TUX
        person = person.resize((400, 600), Image.LANCZOS) 
        print(f"Resized to 400x400 due to size being {width}x{height}")
    elif width == 1280*2 and height == 1600*2: #wet suit
        person = person.resize((500, 600), Image.LANCZOS) 
        print(f"Resized to 400x400 due to size being {width}x{height}")
    elif width == 1000*2 and height == 1400*2: #Anarkali Black Jitter Long Dress
        person = person.resize((450, 600), Image.LANCZOS) 
        print(f"Resized to 400x400 due to size being {width}x{height}")
    elif width == 768*2 and height == 768*2: #CowGirl with Hat
        person = person.resize((550, 550), Image.LANCZOS) 
        print(f"Resized to 400x400 due to size being {width}x{height}")
    elif width == 988 and height == 988: #Maroon Green Saree
        person = person.resize((300, 300), Image.LANCZOS) 
        print(f"Resized to 400x400 due to size being {width}x{height}")
    elif width == 800*2 and height == 1200*2: #Smriti Mandhana
        person = person.resize((450, 600), Image.LANCZOS) 
        print(f"Resized to 400x400 due to size being {width}x{height}")
    elif width == 351*2 and height == 626*2: #Woman Gray Suit
        person = person.resize((350, 600), Image.LANCZOS) 
        print(f"Resized to 400x400 due to size being {width}x{height}")
    elif width == 600*2 and height == 800*2: #Woman Maroon Suit
        person = person.resize((450, 650), Image.LANCZOS) 
        print(f"Resized to 400x400 due to size being {width}x{height}")   
    else:
        print(f"Size {width}x{height} does not match any conditions for resizing.")
    return person

def blend_images(background_bytes, person_bytes, logo_bytes):
    # Convert bytes to PIL Images
    background = Image.open(BytesIO(background_bytes)).convert("RGBA")
    person_original = Image.open(BytesIO(person_bytes)).convert("RGBA")
    logo = Image.open(BytesIO(logo_bytes)).convert("RGBA")
    
    # Print shapes of the original images
    print(f"Background image size: {background.size}")  # (width, height)
    print(f"Person image size: {person_original.size}")          # (width, height)
    print(f"Logo image size: {logo.size}")              # (width, height)

    # Resize person image to a smaller size 
    person = resize_person_image(person_original)
    
    # Define position where the person will be placed
    # x_pos_person = 600
    # y_pos_person = 400
    person_position = [(600,400),(50,400),(100,400),(550,400),(500,400),(600,350),(400,350),(100,350),(50,350)]
    position_person = random.choice(person_position)
    print("position_person",position_person)
    # Convert images to NumPy arrays
    background_np = np.array(background)
    person_np = np.array(person)
    logo_np = np.array(logo)

    # Create a mask from the alpha channel of the person image
    alpha_mask_person = person_np[:, :, 3] / 255.0
    alpha_mask_person = alpha_mask_person
    # Ensure the person fits within the background dimensions
    y1, y2 = max(0, position_person[1]), min(position_person[1] + person.height, background.height)
    x1, x2 = max(0, position_person[0]), min(position_person[0] + person.width, background.width)
    y1_person, y2_person = max(0, -position_person[1]), min(person.height, background.height - position_person[1])
    x1_person, x2_person = max(0, -position_person[0]), min(person.width, background.width - position_person[0])

    # Blend the person image
    for c in range(0, 3):
        background_np[y1:y2, x1:x2, c] = (
            background_np[y1:y2, x1:x2, c] * (1 - alpha_mask_person[y1_person:y2_person, x1_person:x2_person]) +
            person_np[y1_person:y2_person, x1_person:x2_person, c] * alpha_mask_person[y1_person:y2_person, x1_person:x2_person]
        )

    # Resize the logo image (e.g., 200% of original size)
    logo_resize_factor = 19.0
    logo = logo.resize((int(logo.width / logo_resize_factor), int(logo.height / logo_resize_factor)), Image.LANCZOS)
    # Print shape of the resized logo image
    print(f"Resized logo image size: {logo.size}")
    # Define position where the logo will be placed
    x_pos_logo = background.width - logo.width - 10

    y_pos_logo = 10
    position_logo = (x_pos_logo, y_pos_logo)

    # Convert the resized logo image to a NumPy array
    logo_np = np.array(logo)

    # Create a mask from the alpha channel of the logo image
    alpha_mask_logo = logo_np[:, :, 3] / 255.0

    # Ensure the logo fits within the background dimensions
    y1, y2 = max(0, position_logo[1]), min(position_logo[1] + logo.height, background.height)
    x1, x2 = max(0, position_logo[0]), min(position_logo[0] + logo.width, background.width)
    y1_logo, y2_logo = max(0, -position_logo[1]), min(logo.height, background.height - position_logo[1])
    x1_logo, x2_logo = max(0, -position_logo[0]), min(logo.width, background.width - position_logo[0])

    # Blend the logo image
    for c in range(0, 3):
        background_np[y1:y2, x1:x2, c] = (
            background_np[y1:y2, x1:x2, c] * (1 - alpha_mask_logo[y1_logo:y2_logo, x1_logo:x2_logo]) +
            logo_np[y1_logo:y2_logo, x1_logo:x2_logo, c] * alpha_mask_logo[y1_logo:y2_logo, x1_logo:x2_logo]
        )

    # Convert the result back to a PIL image
    final_image = Image.fromarray(background_np)

    # Convert final image to bytes
    output_buffer = BytesIO()
    final_image.save(output_buffer, format='PNG')
    return output_buffer.getvalue()