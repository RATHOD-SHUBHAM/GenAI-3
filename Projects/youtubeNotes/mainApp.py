import os
import streamlit as st
from summarize.utils import extract_transcript
from summarize.core import generate_notes
from summarize.download_notes import write_to_file

HOME = os.getcwd()

# ----------------------------------------------------------------------
# streamlit code for viewing document
st.set_page_config(layout="wide",
                   page_title="ClipNote",
                   page_icon="✍️",
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
        <p>'With 🫶️ from Shubham Shankar.'</p>
    </div>

"""

# Styling ----------------------------------------------------------------------
st.image("icon.jpg", width=85)
st.title("ClipNote: Comprehensive Notes from Videos")
st.subheader(" ✍️ From Clip to Notes with AI 🧠.")
st.write("Powered by LLM.")
st.markdown(hide_menu, unsafe_allow_html=True)

# Intro ----------------------------------------------------------------------

st.write(
    """
    Hi 👋, I'm **:red[Shubham Shankar]**, and welcome to my **:green[ClipNote]**! :rocket:
    
    Have you ever been in a position where you are listening to a lecture and taking notes at the same time?
    If so, you understand the difficulty, the endless number of **:orange[stop and play and rewind]**, it's insane; a 30-minute video may take 2 hours. 
    
    **:green[ClipNote]** makes use of **:blue[Large Language Model]** and **:violet[cutting-edge AI]** technologies to **simplify the process of extracting key information from videos for effortless note-taking**.✨
    """
)

st.markdown('---')

st.write(
    """
    ### App Interface!!

    :dog: The web app has an easy-to-use interface. 

    1] **:red[Topic]**: Paste the URL of the video lecture you wish to take notes on..

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

# Todo Main Func
if __name__ == '__main__':
    st.subheader(" Clip and Note with Ease..")

    youtube_link = st.text_input("Paste YT Video URL here:")

    if st.button("Make Notes"):
        try:
            # Todo: Thumbnail Generator.
            if youtube_link:
                video_id = youtube_link.split("=")[1]
                # print(video_id)
                video_id = video_id.split('&')[0]
                # print(video_id)
                st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

            with st.spinner('Taking Notes'):
                transcript_text = extract_transcript(youtube_link)

                if transcript_text:
                    summary = generate_notes(transcript_text)
                    write_to_file(transcript=summary)

                    st.markdown("## Notes:")
                    st.write(summary)

                    note_file_path = f"{HOME}/notes.md"
                    print(note_file_path)

                    with open(note_file_path) as f:
                        st.download_button(
                            label="Download Notes :memo:",
                            data=f,
                            file_name='Notes.md',
                        )

        except Exception as e:
            st.warning('Invalid URL')
