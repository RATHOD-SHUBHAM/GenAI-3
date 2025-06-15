import cv2
from moviepy.editor import VideoFileClip
import base64
import os
from langchain.chat_models import AzureChatOpenAI

os.environ["OPENAI_API_TYPE"] = "azure_ad"
os.environ["AZURE_OPENAI_ENDPOINT"] = ""
os.environ["AZURE_OPENAI_API_VERSION"] = "2024-05-01-preview"
os.environ["AZURE_OPENAI_API_KEY"] = ""
os.environ["AZURE_OPENAI_GPT4O_MODEL_NAME"] = "gpt-4o"


class VideoAnalyst:
    def __init__(self, VIDEO_PATH):
        self.llm = AzureChatOpenAI(
            openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
            azure_deployment=os.environ["AZURE_OPENAI_GPT4O_MODEL_NAME"],
            temperature=1,
        )
        self.VIDEO_PATH = VIDEO_PATH

    def process_video(self, video_path, seconds_per_frame=2):
        base64Frames = []
        base_video_path, _ = os.path.splitext(video_path)

        video = cv2.VideoCapture(video_path)
        total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
        fps = video.get(cv2.CAP_PROP_FPS)
        frames_to_skip = int(fps * seconds_per_frame)
        curr_frame = 0

        # Loop through the video and extract frames at specified sampling rate
        while curr_frame < total_frames - 1:
            video.set(cv2.CAP_PROP_POS_FRAMES, curr_frame)
            success, frame = video.read()
            if not success:
                break
            _, buffer = cv2.imencode(".jpg", frame)
            base64Frames.append(base64.b64encode(buffer).decode("utf-8"))
            curr_frame += frames_to_skip

        video.release()

        print(f"Extracted {len(base64Frames)} frames")

        return base64Frames

    def analyzeVideo(self):
        base64Frames = self.process_video(self.VIDEO_PATH, seconds_per_frame=2)

        system_prompt = """
          You are an expert media analyst. Your expertise includes analyzing and understanding every detail that is present in the media.
          Make sure to include every small details and dynamic objects such as traffic signals, historic sites, road signs, and animals.

          Your Task:
          Carefully examine the following media in detail and provide a detailed, factual, and accurate explanation of what the media depicts.
          If this is a well-known location, please provide me with every relevant detail.
          Highlight all the key elements and their significance, and present your analysis in clear, well-structured markdown format.
        """

        messages = [
            {
                "role": "system",
                "content": system_prompt
            },
            {"role": "user", "content": [
                {"type": "text", "text": "These are the frames from the video."},
                *map(lambda x: {"type": "image_url",
                                "image_url": {"url": f'data:image/jpg;base64,{x}', "detail": "low"}}, base64Frames[:9])
            ],
             }
        ]

        video_responce = self.llm.invoke(messages)

        return video_responce.content
