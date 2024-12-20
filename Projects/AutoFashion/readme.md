
---

# Project Name: **AutoFashion: Car & Fashion Imaginer**

## Description

**AutoFashion** is an innovative and fun application that brings your imagination to life by merging your dream car with a stylish outfit. The application uses state-of-the-art AI models to create beautiful, realistic images based on your input. Here’s how it works:

1. **Express Your Imagination**: You provide a description of a car and a location (e.g., "Imagine me a Range Rover in front of Taj Westend").
2. **Upload a Selfie**: You click and upload a selfie for face recognition.
3. **Select a Costume**: Choose a suit or outfit you'd like to see yourself wearing.

The application then uses AI to:
- Generate a detailed image of your dream car in your desired location.
- Extract your face from the selfie.
- Blend your face with the costume you selected.
- Merge both the generated car image and your personalized avatar into one stunning image.

The result is a seamless, customized image of you alongside your dream car, dressed in the outfit you chose!

## Features

- **Robust Prompt Generator**: Creates a detailed and accurate prompt based on your user input.
- **DALL·E Image Generator**: Uses the robust prompt to generate high-quality images of cars and locations.
- **Background Removal**: Removes the background from the selfie for better image processing.
- **SwapSeed Face Swap**: Swaps the user's face and blends the selected costume for a polished look.
- **Final Overlay**: Combines the generated car image and your customized avatar into one beautiful, seamless image.

## Project Workflow

1. **User Input**: Enter a description of your dream car and location (e.g., "Range Rover in front of Taj Westend").
2. **Upload Selfie**: Upload a selfie for face extraction.
3. **Select Costume**: Pick an outfit you’d like to wear (e.g., a suit).
4. **Image Generation & Fusion**: The application generates the car image using DALL·E, removes the background from your selfie, swaps your face into the costume, and finally merges the images into one beautiful output.

## Python Files

- **robust_prompt_generator.py**: Takes user input and creates a detailed prompt for the AI model.
- **dalle_image_generator.py**: Uses the robust prompt to generate an image of the car and location.
- **background_removal.py**: Removes the unnecessary background from the selfie.
- **swapseed.py**: Performs the face swap and integrates the selected costume.
- **final_overlay.py**: Merges the generated car image and the customized avatar into the final output.

## Prerequisites

Before running the project, ensure you have the following installed on your system:

- **Python 3.7+**
- **OpenAI API Key** (for DALL·E integration)
- **Face Recognition Libraries** (e.g., OpenCV, DeepFace, or similar)
- **Additional Python dependencies** (listed in `requirements.txt`)

## Clone & Run the Project

### 1. Clone the Repository

Start by cloning the repository to your local machine:

```bash
git clone https://github.com/your-username/autofashion.git
cd autofashion
```

### 2. Set Up Virtual Environment

It's recommended to use a virtual environment to manage project dependencies. Run the following commands to create and activate a virtual environment:

For **Windows**:

```bash
python -m venv venv
venv\Scripts\activate
```

For **Mac/Linux**:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Install all the required Python packages:

```bash
pip install -r requirements.txt
```

This will install all necessary dependencies, including OpenAI API client, image processing libraries, and more.

Also clone swapseed
```bash
git clone https://github.com/KiranPranay/swapseed
cd swapseed

pip install -r requirements.txt
```
This will install all necessary dependencies required to swapface.

### 4. Set Up OpenAI API Key

You will need to provide your **OpenAI API key** for the DALL·E image generation.

- If you don’t have an API key, you can sign up for access on [OpenAI’s website](https://beta.openai.com/signup/).
- Create a `.env` file in the project root directory and add your API key as follows:

```bash
OPENAI_API_KEY=your-api-key-here
```

### 5. Running the Application

Now that everything is set up, you can run the scripts in sequence. Here is a typical order for using the app:

- **Step 1**: Generate the prompt based on user input.

```bash
python robust_prompt_generator.py
```

- **Step 2**: Generate the car image based on the prompt.

```bash
python dalle_image_generator.py
```

- **Step 3**: Process the selfie to remove the background.

```bash
python background_removal.py
```

- **Step 4**: Swap the user’s face and integrate the selected costume.

```bash
python swapseed.py
```

- **Step 5**: Merge the car image and customized avatar into the final image.

```bash
python final_overlay.py
```

### 6. Output

After running these scripts, you will get a final image where your dream car and customized avatar are combined into one beautiful output.

---

## Notes

- Make sure your selfie is of good quality with clear visibility of your face to get the best results in face swapping.
- Experiment with different outfits to see how well the costume blends with the image.
- The accuracy of the car image and background removal depends on the quality of input (prompt and selfie).

Enjoy creating personalized and imaginative car & fashion images with **AutoFashion**!

--- 
