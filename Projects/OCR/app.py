import streamlit as st
from groq import Groq
from PIL import Image
import io
import os
import base64
from dotenv import load_dotenv

# ---------------------------------------------------------------
# Page configuration
st.set_page_config(
    page_title="Llama OCR",
    page_icon="🦙",
    layout="wide",
    initial_sidebar_state="expanded"
)

# hide hamburger and customize footer
hide_menu = """
    <style>

    #MainMenu {
        visibility:hidden;
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        color: grey;
        text-align: center;
    }

    </style>

    <div class="footer">
        <p>'With ❤️ from Shubham Shankar.'</p>
    </div>

"""

# Styling ----------------------------------------------------------------------
st.image("icon.jpg", width=85)
st.title("Llama OCR 🦙")
st.write("Powered by Llama Vision Model.")
st.markdown(hide_menu, unsafe_allow_html=True)

st.markdown('---')

st.write(
    """
    ### App Interface!!

    :dog: The web app has an easy-to-use interface. 

    1] **:red[Upload Image]**: Easily upload your image to feed into the OCR pipeline for processing.

    2] **:green[Extract Text]**: Extract structured text from image.

    3] **:blue[Clear]**: Click Clear to reset and start fresh.

    """
)

st.markdown('---')

st.error(
    """
    Connect with me on [**Github**](https://github.com/RATHOD-SHUBHAM) and [**LinkedIn**](https://www.linkedin.com/in/shubhamshankar/). ✨
    """,
    icon="🧟‍♂️",
)

st.markdown('---')


HOME = os.getcwd()
load_dotenv()
os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')


client = Groq()


def save_uploadedfile(uploadedfile):
    image_dir = f"{HOME}/input_image"
    with open(os.path.join(image_dir, uploadedfile.name), "wb") as f:
        f.write(uploadedfile.getbuffer())
    return st.success("Saved File:{} to image_dir".format(uploadedfile.name))


# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def main():
    # Add clear button to top right
    col1, col2 = st.columns([6, 1])
    with col2:
        if st.button("Clear 🗑️"):
            if 'ocr_result' in st.session_state:
                del st.session_state['ocr_result']
            st.rerun()

    st.markdown('<p style="margin-top: -20px;">Extract structured text from images using Llama 3.2 Vision!</p>',
                unsafe_allow_html=True)
    st.markdown("---")

    # Move upload controls to sidebar
    with st.sidebar:
        st.header("Upload Image")
        uploaded_file = st.file_uploader("Choose an image...", type=['png', 'jpg', 'jpeg'])

        if uploaded_file is not None:
            # Display the uploaded image
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image")

            save_uploadedfile(uploaded_file)

            if st.button("Extract Text 🔍", type="primary"):
                with st.spinner("Processing image..."):
                    try:
                        image_dir = f"{HOME}/input_image"
                        image_path = os.path.join(image_dir, uploaded_file.name)

                        system_prompt = "Analyze the text in the provided image. Extract all readable contentand present it in a structured Markdown format that is clear, concise, and well-organized. Ensure proper formatting (e.g., headings, lists, orcode blocks) as necessary to represent the content effectively."

                        # Getting the base64 string
                        base64_image = encode_image(image_path)

                        chat_completion = client.chat.completions.create(
                            messages=[
                                {
                                    "role": "user",
                                    "content": [
                                        {"type": "text", "text": system_prompt},
                                        {
                                            "type": "image_url",
                                            "image_url": {
                                                "url": f"data:image/jpeg;base64,{base64_image}",
                                            },
                                        },
                                    ],
                                }
                            ],
                            model="llama-3.2-11b-vision-preview",
                        )

                        st.session_state['ocr_result'] = chat_completion.choices[0].message.content
                    except Exception as e:
                        st.error(f"Error processing image: {str(e)}")

    # Main content area for results
    if 'ocr_result' in st.session_state:
        st.markdown(st.session_state['ocr_result'])
    else:
        st.info("Upload an image and click 'Extract Text' to see the results here.")


if __name__ == "__main__":
    main()
