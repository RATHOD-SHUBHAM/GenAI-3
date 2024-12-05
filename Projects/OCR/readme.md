# Llama OCR
This is an Optical Character Recognition (OCR) web application powered by Streamlit, Groq, and the Llama 3.2 Vision model. The app allows you to upload an image, process it using state-of-the-art OCR technology, and extract text from the image.

The app utilizes the Groq AI accelerator for high-performance inference and the Llama 3.2 Vision model for advanced image processing and text recognition.

## Features
1. Upload an image to perform OCR and extract text.
2. Real-time processing with Groq hardware for optimal speed and efficiency.
3. Built using Streamlit for an interactive and user-friendly interface.
4. Powered by the Llama 3.2 Vision Model, which provides high-quality image-to-text conversion.

## Installation
To set up and run the OCR app, follow these steps:

1. Clone the repository
```
git clone https://github.com/your-username/ocr-app.git
cd ocr-app
```

2. Create a Virtual Environment (Optional but Recommended)
```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install dependencies
Install the required libraries by running:
```
pip install -r requirements.txt
```
This will install all necessary dependencies, including Groq, Streamlit, and the Llama 3.2 Vision model.

4. Running the App
To launch the app, run the following command:
```
streamlit run app.py
```
This will start a local Streamlit server, and you can access the app at http://localhost:8501 in your browser.

## Usage
1. Open the app in your browser.
2. Upload an image that contains text.
3. The OCR model powered by Llama 3.2 will process the image and extract the text.
4. The result will be displayed on the screen for you to copy or use.

## Requirements
* Python 3.10 or higher
* Groq AI accelerator (for enhanced performance)
* Llama 3.2 Vision Model for OCR
* Streamlit for the frontend interface

## Troubleshooting
* If you encounter errors related to missing packages or dependencies, make sure that your virtual environment is active, and you've installed all requirements from the requirements.txt file.
* For Groq or Llama model-specific issues, refer to the official documentation for installation and setup.

## Acknowledgements
1. Groq: High-performance AI accelerator for fast processing.
2. Llama 3.2 Vision Model: Advanced OCR model for accurate text recognition.
3. Streamlit: Simplifies the creation of interactive web applications.

---

![app](https://github.com/user-attachments/assets/4924581b-ef09-4e95-ac9c-e2eb601e8a73)
